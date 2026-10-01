/* Academy v2 runtime: Pyodide in a Blob worker, exercises, demos, progress, cards, index, review.
   Works from file:// (no fetch of local files; the worker is built from a Blob URL). */
(function () {
  "use strict";

  // ---------- storage (per-viewer convenience only; every call guarded) ----------
  const LS = {
    get(k, d) { try { const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* private mode */ } },
  };
  const PKEY = "av2.progress", CKEY = "av2.cards", DKEY = "av2.draft.";
  const progress = () => LS.get(PKEY, {});
  function saveModule(mid, fn) { const p = progress(); p[mid] = p[mid] || { ex: {} }; fn(p[mid]); LS.set(PKEY, p); }
  const $ = (sel, root) => (root || document).querySelector(sel);
  const $$ = (sel, root) => Array.from((root || document).querySelectorAll(sel));
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  // ---------- Python runtime ----------
  function workerSource() {
    const url = window.AV2_PYODIDE;
    return [
      "importScripts(" + JSON.stringify(url + "pyodide.js") + ");",
      "let py = null; const loaded = new Set();",
      "const ready = (async () => {",
      "  py = await loadPyodide({ indexURL: " + JSON.stringify(url) + " });",
      "  const ns = py.toPy({ __name__: 'academy_harness' });",
      "  py.runPython(" + JSON.stringify(window.AV2_HARNESS) + ", { globals: ns });",
      "  self.runJson = ns.get('run_json');",
      "})();",
      "self.onmessage = async (e) => {",
      "  const { id, payload, packages } = e.data;",
      "  try {",
      "    await ready;",
      "    const need = (packages || []).filter((p) => !loaded.has(p));",
      "    if (need.length) { await py.loadPackage(need); need.forEach((p) => loaded.add(p)); }",
      "    const req = JSON.parse(payload); await py.loadPackagesFromImports(req.code + '\\n' + (req.tests || ''));",
      "    self.postMessage({ id, ok: true, out: self.runJson(payload) });",
      "  } catch (err) { self.postMessage({ id, ok: false, err: String((err && err.message) || err) }); }",
      "};",
    ].join("\n");
  }

  class Py {
    constructor() { this.w = null; this.seq = 0; this.pending = new Map(); this.warm = false; this.chain = Promise.resolve(); }
    start() {
      const blob = new Blob([workerSource()], { type: "text/javascript" });
      this.w = new Worker(URL.createObjectURL(blob));
      this.warm = false;
      this.w.onmessage = (e) => {
        const p = this.pending.get(e.data.id);
        if (!p) return;
        clearTimeout(p.t); this.pending.delete(e.data.id); this.warm = true; p.resolve(e.data);
      };
      this.w.onerror = (e) => { this.failAll("The Python worker failed to start: " + (e.message || "network or CDN problem")); };
    }
    failAll(msg) {
      for (const [id, p] of this.pending) { clearTimeout(p.t); p.resolve({ id, ok: false, err: msg }); }
      this.pending.clear();
    }
    restart() { try { this.w && this.w.terminate(); } catch (e) { /* ignore */ } this.w = null; this.failAll("restarted"); }
    _run(payload, packages) {
      if (!this.w) this.start();
      const id = ++this.seq;
      const limit = this.warm ? window.AV2_TIMEOUT_MS : 180000; // the first call downloads Python
      return new Promise((resolve) => {
        const t = setTimeout(() => {
          this.pending.delete(id); this.restart();
          resolve({ id, ok: false, timeout: true, err: "Stopped after " + Math.round(limit / 1000) + " s. An infinite loop? Python was restarted." });
        }, limit);
        this.pending.set(id, { resolve, t });
        this.w.postMessage({ id, payload: JSON.stringify(payload), packages: packages || [] });
      });
    }
    run(payload, packages) {
      const job = this.chain.then(() => this._run(payload, packages));
      this.chain = job.catch(() => {});
      return job.then((r) => (r.ok ? Object.assign({ ok: true }, JSON.parse(r.out)) : r));
    }
  }
  const py = new Py();

  // ---------- editors ----------
  function makeEditor(ta, value, onRun) {
    ta.value = value;
    if (window.CodeMirror) {
      const cm = window.CodeMirror.fromTextArea(ta, {
        mode: "python", lineNumbers: true, indentUnit: 4, tabSize: 4, viewportMargin: Infinity,
        extraKeys: {
          Tab: (c) => (c.somethingSelected() ? c.indentSelection("add") : c.replaceSelection("    ")),
          "Shift-Tab": (c) => c.indentSelection("subtract"),
          "Cmd-Enter": () => onRun && onRun(), "Ctrl-Enter": () => onRun && onRun(),
        },
      });
      return { get: () => cm.getValue(), set: (v) => cm.setValue(v), onChange: (f) => cm.on("change", () => f(cm.getValue())) };
    }
    ta.addEventListener("keydown", (e) => {
      if (e.key === "Tab") { e.preventDefault(); const s = ta.selectionStart; ta.setRangeText("    ", s, ta.selectionEnd, "end"); }
      if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) { e.preventDefault(); onRun && onRun(); }
    });
    return { get: () => ta.value, set: (v) => { ta.value = v; }, onChange: (f) => ta.addEventListener("input", () => f(ta.value)) };
  }

  function busy(el, on) {
    const s = $(".spin", el); if (s) s.hidden = !on;
    $$("button", $(".actions", el)).forEach((b) => { b.disabled = on; });
  }
  const firstRunNote = () => (py.warm ? "" : " (the first run downloads Python, about 10 to 20 seconds)");

  // ---------- exercises ----------
  function renderResults(box, res, heading) {
    box.hidden = false;
    if (!res.ok) { box.innerHTML = "<div class='no'>" + esc(res.err || "could not run") + "</div>"; return; }
    let h = heading ? "<div><b>" + esc(heading) + "</b></div>" : "";
    if (res.load_error) {
      h += "<div class='no'>The code crashed before any test ran: <b>" + esc(res.load_error.type) + "</b> " +
        esc(res.load_error.message) + esc(res.load_error.where || "") + "</div>";
    }
    for (const t of res.tests || []) {
      h += "<div class='t'><span class='" + (t.ok ? "ok'>✓" : "no'>✗") + "</span><span>" + esc(t.name) + "</span>" +
        (t.ok ? "" : "<span class='m'>" + esc((t.type && t.type !== "AssertionError" ? t.type + ": " : "") + (t.message || "")) + "</span>") + "</div>";
    }
    const n = (res.tests || []).length, k = (res.tests || []).filter((t) => t.ok).length;
    h += "<p class='note'>" + k + " of " + n + " tests pass" + (res.passed ? ". Solved." : ".") + "</p>";
    if (res.stdout) h += "<pre>" + esc(res.stdout) + "</pre>";
    box.innerHTML = h;
  }

  function setStatus(el, mid) {
    const st = $("[data-status]", el);
    const rec = ((progress()[mid] || {}).ex || {})[el.dataset.ex];
    if (rec && rec.passed) { st.textContent = "solved"; st.className = "ex-status pass"; }
    else if (rec) { st.textContent = "attempted"; st.className = "ex-status fail"; }
  }

  function updateChip(mid, data) {
    const chip = $("[data-progress]"); if (!chip) return;
    const ex = (progress()[mid] || {}).ex || {};
    const total = Object.keys(data.exercises).length;
    const done = Object.keys(data.exercises).filter((k) => ex[k] && ex[k].passed).length;
    chip.textContent = done + " / " + total + " exercises" + ((progress()[mid] || {}).known ? " · known" : "");
  }

  function setupExercise(el, data) {
    const mid = data.id, id = el.dataset.ex, x = data.exercises[id];
    const ta = $("textarea.code", el);
    const draftKey = DKEY + mid + ":" + id;
    const draft = LS.get(draftKey, null);
    const run = async () => {
      busy(el, true); const box = $(".results", el); box.hidden = false; box.innerHTML = "<span class='muted'>Running tests" + firstRunNote() + "…</span>";
      const res = await py.run({ kind: "exercise", code: ed.get(), tests: x.tests }, data.packages);
      busy(el, false); renderResults(box, res);
      if (res.ok) {
        saveModule(mid, (m) => { const prev = m.ex[id] || {}; m.ex[id] = { passed: !!(res.passed || prev.passed), at: Date.now(), tries: (prev.tries || 0) + 1 }; });
        setStatus(el, mid); updateChip(mid, data);
      }
    };
    const ed = makeEditor(ta, draft != null ? draft : x.starter || "", run);
    ed.onChange((v) => LS.set(draftKey, v));
    let hintN = 0, bugN = 0;
    el.addEventListener("click", async (e) => {
      const b = e.target.closest("button[data-act]"); if (!b) return;
      const act = b.dataset.act;
      if (act === "run") run();
      if (act === "hint") {
        if (hintN < x.hints.length) {
          const li = document.createElement("li"); li.innerHTML = esc(x.hints[hintN]); $("ol.hints", el).appendChild(li);
          hintN++; b.textContent = "Hint (" + hintN + "/" + x.hints.length + ")";
          if (window.renderMathInElement) window.renderMathInElement(li, mathOpts);
        }
      }
      if (act === "bug") {
        const m = x.mutants[bugN % x.mutants.length]; bugN++;
        busy(el, true); const box = $(".results", el); box.hidden = false; box.innerHTML = "<span class='muted'>Running a wrong solution" + firstRunNote() + "…</span>";
        const res = await py.run({ kind: "exercise", code: m, tests: x.tests }, data.packages);
        busy(el, false);
        renderResults(box, res, "A plausible wrong solution (" + bugN + " of " + x.mutants.length + "). A good test suite must fail on it:");
        box.insertAdjacentHTML("beforeend", "<details><summary>See the wrong code</summary><pre>" + esc(m) + "</pre></details>");
      }
      if (act === "solution") {
        if (!$(".solution", el) && window.confirm("Show the reference solution? Try the hints first. Reading a solution teaches far less than getting stuck.")) {
          $(".actions", el).insertAdjacentHTML("afterend", "<details class='solution' open><summary>Reference solution</summary><pre>" + esc(x.solution) + "</pre></details>");
          saveModule(mid, (m) => { m.ex[id] = Object.assign({ tries: 0 }, m.ex[id] || {}, { sawSolution: true }); });
        }
      }
      if (act === "reset") { if (window.confirm("Replace your code with the starter?")) { ed.set(x.starter || ""); LS.set(draftKey, x.starter || ""); } }
    });
    setStatus(el, mid);
  }

  // ---------- demos ----------
  function setupDemo(el, data) {
    const d = data.demos[el.dataset.demo];
    const ta = $("textarea.code", el);
    const out = $("pre.out", el);
    const show = (res, label) => {
      out.hidden = false;
      if (!res.ok) { out.className = "out bad"; out.textContent = res.err || "could not run"; return; }
      let t = label ? label + "\n\n" : "";
      t += res.stdout || "";
      if (res.error) t += (t ? "\n" : "") + res.error.type + ": " + res.error.message + (res.error.where || "");
      else t += (t && !t.endsWith("\n") ? "\n" : "") + "✓ every check passed";
      out.textContent = t; out.className = "out " + (res.passed ? "good" : "bad");
    };
    const run = async () => { busy(el, true); out.hidden = false; out.textContent = "Running" + firstRunNote() + "…"; show(await py.run({ kind: "demo", code: ed.get() }, data.packages)); busy(el, false); };
    const ed = makeEditor(ta, d.code, run);
    let mN = 0;
    el.addEventListener("click", async (e) => {
      const b = e.target.closest("button[data-act]"); if (!b) return;
      if (b.dataset.act === "run") run();
      if (b.dataset.act === "reset") ed.set(d.code);
      if (b.dataset.act === "mutant") {
        const m = d.mutants[mN % d.mutants.length]; mN++;
        busy(el, true); out.hidden = false; out.textContent = "Running" + firstRunNote() + "…";
        const res = await py.run({ kind: "demo", code: m }, data.packages); busy(el, false);
        show(res, "The broken version. Its own checks should fail:");
        out.insertAdjacentHTML("afterend", "");
      }
    });
  }

  // ---------- cards ----------
  const INTERVAL_DAYS = [0, 1, 3, 7, 16, 35];
  function gradeCard(key, g) {
    const all = LS.get(CKEY, {});
    const c = all[key] || { box: 0 };
    const now = Date.now();
    if (g === 0) { c.box = 1; c.due = now + 10 * 60 * 1000; }
    else { c.box = Math.min(5, (c.box || 0) + (g === 2 ? 2 : 1)); c.due = now + INTERVAL_DAYS[c.box] * 86400000; }
    c.seen = now; all[key] = c; LS.set(CKEY, all);
  }
  function setupCards(data) {
    $$(".card[data-card]").forEach((el) => {
      const key = data.id + ":" + el.dataset.card;
      el.addEventListener("click", (e) => {
        const b = e.target.closest("button"); if (!b) return;
        if (b.dataset.act === "flip") { $(".a", el).hidden = false; b.hidden = true; $(".grade", el).hidden = false; }
        if (b.dataset.grade) { gradeCard(key, +b.dataset.grade); el.classList.add("done"); $(".grade", el).hidden = true; }
      });
    });
  }

  // ---------- math ----------
  const mathOpts = {
    delimiters: [{ left: "$$", right: "$$", display: true }, { left: "$", right: "$", display: false }, { left: "\\(", right: "\\)", display: false }],
    throwOnError: false,
  };
  function renderMath(root) { if (window.renderMathInElement) { try { window.renderMathInElement(root, mathOpts); } catch (e) { /* leave raw */ } } }

  // ---------- self-test (used by the headless smoke test) ----------
  async function selfTest(data) {
    const report = { module: data.id, checks: [], ok: true };
    const add = (what, pass, detail) => { report.checks.push({ what, pass, detail }); if (!pass) report.ok = false; };
    for (const [id, d] of Object.entries(data.demos)) {
      const r = await py.run({ kind: "demo", code: d.code }, data.packages);
      add("demo " + id + " passes", !!(r.ok && r.passed), r.err || (r.error && r.error.type) || "");
      for (let i = 0; i < d.mutants.length; i++) {
        const m = await py.run({ kind: "demo", code: d.mutants[i] }, data.packages);
        add("demo " + id + " mutant " + (i + 1) + " trips an assert", !!(m.ok && m.error && m.error.type === "AssertionError"), m.err || (m.error && m.error.type) || "ran clean");
      }
    }
    for (const [id, x] of Object.entries(data.exercises)) {
      const s = await py.run({ kind: "exercise", code: x.solution, tests: x.tests }, data.packages);
      add("exercise " + id + " solution passes", !!(s.ok && s.passed), s.err || JSON.stringify((s.tests || []).filter((t) => !t.ok)).slice(0, 300));
      const st = await py.run({ kind: "exercise", code: x.starter, tests: x.tests }, data.packages);
      add("exercise " + id + " starter fails", !!(st.ok && !st.passed), st.err || "");
      for (let i = 0; i < x.mutants.length; i++) {
        const m = await py.run({ kind: "exercise", code: x.mutants[i], tests: x.tests }, data.packages);
        add("exercise " + id + " mutant " + (i + 1) + " fails", !!(m.ok && !m.passed), m.err || "");
      }
    }
    window.__selftest = report;
    document.body.dataset.selftest = report.ok ? "passed" : "failed";
  }

  // ---------- module page ----------
  function modulePage() {
    const data = JSON.parse($("#av2-data").textContent);
    renderMath(document.body);
    $$(".lab.ex").forEach((el) => setupExercise(el, data));
    $$(".lab.demo").forEach((el) => setupDemo(el, data));
    setupCards(data);
    updateChip(data.id, data);
    saveModule(data.id, (m) => { m.visited = Date.now(); });
    const known = $("button[data-act=known]");
    if (known) known.addEventListener("click", () => { saveModule(data.id, (m) => { m.known = !m.known; }); updateChip(data.id, data); known.textContent = (progress()[data.id] || {}).known ? "unmark as known" : "mark this module as known"; });
    if (known && (progress()[data.id] || {}).known) known.textContent = "unmark as known";
    if (/[?&]selftest=1\b/.test(location.search)) selfTest(data);
  }

  // ---------- index ----------
  function moduleDone(p, m) {
    const rec = p[m.id]; if (!rec) return false; if (rec.known) return true;
    if (!m.exercises) return false;
    return Object.values(rec.ex || {}).filter((e) => e.passed).length >= m.exercises;
  }
  function indexPage() {
    const D = window.AV2_INDEX, root = $("#index-root");
    const byId = Object.fromEntries(D.modules.map((m) => [m.id, m]));
    let tab = LS.get("av2.tab", "path"), q = "";
    const draw = () => {
      const p = progress();
      const built = D.modules.filter((m) => m.built);
      const passed = Object.values(p).reduce((a, r) => a + Object.values(r.ex || {}).filter((e) => e.passed).length, 0);
      const done = D.modules.filter((m) => moduleDone(p, m)).length;
      const cards = LS.get(CKEY, {}); const now = Date.now();
      const due = Object.values(cards).filter((c) => c.due && c.due <= now).length;
      const list = tab === "path" ? D.order : tab === "grid" ? [] : D.order.filter((k) => D.paths[tab].includes(k));
      const nextId = list.find((k) => byId[k].built && !moduleDone(p, byId[k]) && byId[k].prereqs.every((x) => moduleDone(p, byId[x]) || !byId[x].built));
      let h = "<h1>From NCERT Class 6 to research</h1>" +
        "<p class='muted'>Every lesson: a story first, then the idea said simply and precisely, why it is true, an oracle that checks it two ways, an experiment against reality, graded exercises whose tests are proven able to fail, and a rule for when to stop. Python runs in your browser (Pyodide " + esc(D.pyodide) + ").</p>" +
        "<div class='stats'>" +
        "<div class='stat'><b>" + built.length + " / " + D.modules.length + "</b><span>modules built</span></div>" +
        "<div class='stat'><b>" + built.reduce((a, m) => a + m.exercises, 0) + "</b><span>exercises available</span></div>" +
        "<div class='stat'><b>" + passed + "</b><span>exercises you solved</span></div>" +
        "<div class='stat'><b>" + done + "</b><span>modules done or known</span></div>" +
        "<div class='stat'><b>" + due + "</b><span>cards due · <a href='review.html'>review</a></span></div></div>" +
        "<details class='meta'><summary><b>How to study here</b></summary><ol>" +
        "<li>Read the story as if you were six. Then say the idea simply, then precisely, from memory.</li>" +
        "<li>Work the proof with a pen and find the one non-obvious step.</li>" +
        "<li>Run the oracle and the experiment, then run their broken versions and see why the checks fail.</li>" +
        "<li>Exercises ramp from warm-up to boss. Run the starter first (it fails), use hints before the solution, and press <i>Watch a bug get caught</i>.</li>" +
        "<li>Grade the flash cards honestly; the Review page brings them back when due.</li>" +
        "<li>Stop when the module's stop rule is met. Already know a module? Do its boss and cards first, then mark it known.</li>" +
        "<li>A sustainable rhythm: weekdays 90 min (10 cards, 60 lesson, 20 on yesterday's failure); weekends two bosses and one explain-it-to-a-child write-up; every fourth week, no new modules, only redoing bosses from a blank editor.</li>" +
        "</ol></details>" +
        "<div class='tabs'>" + [["path", "Full path"], ["spine", "Verification spine"], ["l5", "L5 fast track"], ["edge", "Android and edge AI"], ["grid", "Map"]]
          .map(([k, l]) => "<button data-tab='" + k + "' class='" + (tab === k ? "on" : "") + "'>" + l + "</button>").join("") +
        " <input type='search' placeholder='Filter by title or id' value='" + esc(q) + "'></div>";
      if (tab === "grid") {
        h += "<div class='grid'><table><tr><th>Level</th>" + Object.values(D.tracks).map((t) => "<th>" + esc(t) + "</th>").join("") + "</tr>" +
          D.levels.map((lv) => "<tr><th>" + esc(lv) + "</th>" + Object.keys(D.tracks).map((t) => "<td>" +
            D.modules.filter((m) => m.level === lv && m.track === t).map((m) => m.built
              ? "<a href='" + m.id + ".html'>" + (moduleDone(p, m) ? "✓ " : "") + esc(m.id + " " + m.title) + "</a>"
              : "<span class='muted'>" + esc(m.id + " " + m.title) + "</span>").join("") + "</td>").join("") + "</tr>").join("") +
          "</table></div>";
      } else {
        const ql = q.toLowerCase();
        h += "<div class='path'>" + list.filter((k) => !ql || (k + " " + byId[k].title).toLowerCase().includes(ql)).map((k, i) => {
          const m = byId[k], rec = p[k] || {}, n = Object.values(rec.ex || {}).filter((e) => e.passed).length;
          const isDone = moduleDone(p, m);
          const st = !m.built ? (m.status === "failing" ? "being fixed" : "not built yet") : isDone ? (rec.known ? "✓ known" : "✓ done") : n + " / " + m.exercises;
          return "<div class='row" + (m.built ? "" : " unbuilt") + (isDone ? " done" : "") + (k === nextId ? " next" : "") + "'>" +
            "<span class='id'>" + (i + 1) + ". " + k + "</span><span class='t'>" +
            (m.built ? "<a href='" + k + ".html'>" + esc(m.title) + "</a>" : "<span class='title'>" + esc(m.title) + "</span>") +
            (k === nextId ? " <b>← next</b>" : "") +
            "<div class='sub'>" + esc(D.tracks[m.track]) + " · " + esc(m.level) + (m.prereqs.length ? " · needs " + m.prereqs.join(", ") : "") + "</div></span>" +
            "<span class='st'>" + st + "</span></div>";
        }).join("") + "</div>";
      }
      h += "<div class='tools'><button data-act='export'>Export my progress</button><label><button data-act='import'>Import progress</button>" +
        "<input type='file' accept='application/json' hidden></label></div>" +
        "<p class='muted'>Progress, drafts and card schedules live only in this browser. Export them to keep a copy.</p>";
      root.innerHTML = h;
    };
    root.addEventListener("click", (e) => {
      const b = e.target.closest("button"); if (!b) return;
      if (b.dataset.tab) { tab = b.dataset.tab; LS.set("av2.tab", tab); draw(); }
      if (b.dataset.act === "export") {
        const blob = new Blob([JSON.stringify({ progress: progress(), cards: LS.get(CKEY, {}) }, null, 1)], { type: "application/json" });
        const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = "academy-v2-progress.json"; a.click();
      }
      if (b.dataset.act === "import") $("input[type=file]", root).click();
    });
    root.addEventListener("input", (e) => { if (e.target.type === "search") { q = e.target.value; draw(); const s = $("input[type=search]", root); s.focus(); s.setSelectionRange(q.length, q.length); } });
    root.addEventListener("change", async (e) => {
      if (e.target.type !== "file" || !e.target.files[0]) return;
      try { const j = JSON.parse(await e.target.files[0].text()); if (j.progress) LS.set(PKEY, j.progress); if (j.cards) LS.set(CKEY, j.cards); draw(); }
      catch (err) { window.alert("That file is not an Academy progress export."); }
    });
    draw();
  }

  // ---------- review ----------
  function reviewPage() {
    const root = $("#review-root"), all = window.AV2_CARDS || [];
    const queue = () => {
      const st = LS.get(CKEY, {}), now = Date.now();
      const due = all.filter((c) => st[c.key] && st[c.key].due <= now);
      const fresh = all.filter((c) => !st[c.key]).slice(0, 20);
      return { due, fresh, list: due.concat(fresh) };
    };
    const draw = () => {
      const { due, fresh, list } = queue();
      if (!list.length) { root.innerHTML = "<h1>Nothing due</h1><p class='muted'>Come back tomorrow, or open a module and study its cards.</p>"; return; }
      const c = list[0];
      root.innerHTML = "<h1>Review</h1><p class='muted'>" + due.length + " due · " + fresh.length + " new in this session · from <a href='" + c.module + ".html'>" + c.module + "</a></p>" +
        "<div class='card'><div class='q'>" + c.q + "</div><div class='a' hidden>" + c.a + "</div>" +
        "<div class='card-actions'><button data-act='flip' class='primary'>Show answer</button><span class='grade' hidden>" +
        "<button data-grade='0'>Again</button><button data-grade='1'>Good</button><button data-grade='2'>Easy</button></span></div></div>";
      renderMath(root);
      root.onclick = (e) => {
        const b = e.target.closest("button"); if (!b) return;
        if (b.dataset.act === "flip") { $(".a", root).hidden = false; b.hidden = true; $(".grade", root).hidden = false; }
        if (b.dataset.grade) { gradeCard(c.key, +b.dataset.grade); draw(); }
      };
    };
    draw();
  }

  const kind = document.body.dataset.page;
  const start = () => { if (kind === "module") modulePage(); else if (kind === "index") indexPage(); else if (kind === "review") reviewPage(); };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
