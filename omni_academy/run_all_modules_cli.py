import json
import time

def run_all():
    print("=" * 70)
    print("OMNI-ACADEMY: EXECUTING ALL 50 MASTER MODULES (NCERT 6TH TO PHD)")
    print("=" * 70)
    
    with open("omni_academy/curriculum_data.js") as f:
        content = f.read()
    json_str = content.split("window.OMNI_MODULES = ")[1].rstrip(";\n")
    modules = json.loads(json_str)

    passed = 0
    t0 = time.time()

    for idx, m in enumerate(modules, 1):
        print(f"\n[{idx:02d}/50] {m['epoch']} ➔ {m['title']}")
        print(f"       Tag: {m['tag']}")
        code = m['code']
        try:
            exec_globals = {}
            exec(code, exec_globals)
            passed += 1
            print(f"       Status: ✓ PASSED")
        except Exception as e:
            print(f"       Status: ❌ FAILED ({e})")

    elapsed = time.time() - t0
    print("\n" + "=" * 70)
    print(f"RESULTS: {passed}/50 Modules Successfully Executed & Verified in {elapsed:.2f}s!")
    print("=" * 70)

if __name__ == "__main__":
    run_all()
