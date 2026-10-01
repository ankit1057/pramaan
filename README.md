# प्रमाण · Pramaan

**Proof, not assertion.** An interactive mathematics and computer-science
curriculum that runs Python in your browser — 135 modules from NCERT Class 6
arithmetic to research-level verification, statistics and systems.

**→ [Open the site](https://ankit1057.github.io/pramaan/)**

Nothing to install. Python runs in the page itself via
[Pyodide](https://pyodide.org) (CPython 3.13 compiled to WebAssembly). The first
load fetches the runtime and takes 10–20 seconds; after that it is instant.

---

## Why "Pramaan"

*Pramaan* (प्रमाण) is the Sanskrit and Hindi word for **proof** or **evidence** —
in Indian philosophy, the means by which knowledge is validly acquired.

That is the method here. Every module carries:

- an **Oracle lab** that computes the same answer two genuinely independent
  ways, and a deliberately broken version so you can watch a check catch a bug;
- an **Experiment lab** where theory states a prediction *first* and the code
  then measures reality — sometimes contradicting the prediction, which is the
  interesting case;
- **exercises with mutants** — plausible wrong solutions that the tests must
  reject for a real reason, not by crashing.

A lesson that only asserts things is not finished. A lesson that lets you check
it is.

## How a module works

1. **Story** — read it as if you were six. If it doesn't surprise you, you
   haven't got it yet.
2. **Simply**, then **Precisely** — say the idea in one sentence, then write the
   precise statement from memory.
3. **Why it's true** — work through the proof with a pen. Find the one
   non-obvious step.
4. **Oracle lab** — run it, then press *Run the broken version* and read why the
   check fails.
5. **Experiment lab** — change a parameter and predict the result *before*
   rerunning.
6. **Exercises** — warm-up, core, boss. Run the starter first; it fails, and
   that is the point. Use the hints before the solution. Press *Watch a bug get
   caught* to see a plausible wrong answer rejected.
7. **Misconceptions** and **Where it breaks** — these are the interview
   questions.
8. **Flash cards** — the Review page brings each card back when it is due.
9. **Stop when** — once you meet the stop rule, move on. Don't polish.

**Placement:** if you think you already know a module, do its boss exercise and
its cards first. Pass without hints and mark it known.

## Tracks

| | Track | Modules |
|---|---|---|
| **M** | Mathematics — arithmetic through real analysis, probability, optimisation, information theory, algebra, Fourier, Markov chains | 40 |
| **P** | Computing foundations — architecture, OS, networks, databases, compilers, security | 25 |
| **D** | Algorithms and the interview loop | 21 |
| **S** | Android, Flutter and edge systems | 17 |
| **L** | Learning machines — classical ML through on-device LLMs | 12 |
| **V** | Verification and science — statistics, experiment design, testing theory, formal methods | 20 |

Four reading paths are offered on the index: the **full path** in prerequisite
order, a **verification spine**, an **interview fast track**, and an
**Android / edge-AI** route.

## What is guaranteed, and what is not

Every published module passes an automated validator:

- each reference solution passes its own tests, and a second run is identical;
- each starter fails;
- each mutant fails **for a real reason** — not a `NameError` or a timeout;
- each oracle and experiment runs clean, and its broken version trips its own
  assertions;
- nothing imports anything the browser lacks;
- every page is then loaded in a real headless Chrome and every lab is executed
  in Pyodide, checking for page errors and unrendered mathematics.

**Not guaranteed:** that every sentence is free of error. Automated checks
reduce mistakes; they cannot remove them. If a claim looks wrong, check it
against the sources listed at the foot of each module. Building that habit is
the entire point of the V track.

## Built with

[Pyodide](https://pyodide.org) · [KaTeX](https://katex.org) ·
[CodeMirror](https://codemirror.net) — all from CDN. The site itself is static
HTML, CSS and JavaScript with no build step and no tracking.

## Contributing

Corrections are very welcome, particularly factual ones. Open an issue with the
module id (for example `M35`), the claim you think is wrong, and a source.
