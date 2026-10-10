import json

with open("omni_academy/curriculum_data.js") as f:
    text = f.read()
data = json.loads(text.split("window.OMNI_MODULES = ")[1].rstrip(";\n"))

for m in data:
    if m["id"] == "m31":
        # Standard safe banker state
        m["code"] = """def bankers_algorithm():
    avail = [3, 3, 2]
    max_claim = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    n = len(alloc); num_res = len(avail)
    need = [[max_claim[i][j] - alloc[i][j] for j in range(num_res)] for i in range(n)]
    work = avail[:]
    finish = [False] * n
    safe_seq = []
    while len(safe_seq) < n:
        found = False
        for p in range(n):
            if not finish[p] and all(need[p][j] <= work[j] for j in range(num_res)):
                for j in range(num_res): work[j] += alloc[p][j]
                finish[p] = True
                safe_seq.append(p)
                found = True
                break
        if not found: return False, []
    return True, safe_seq
safe, seq = bankers_algorithm()
print(f"Banker's Algorithm Safe: {safe}, Sequence: {seq}")
assert safe is True
print("✓ Verified!")"""
    elif m["id"] == "m39":
        # Adam optimizer with 35 steps
        m["code"] = """import math
def adam_step(w, grad, m, v, t, lr=0.1, beta1=0.9, beta2=0.999, eps=1e-8):
    m = beta1 * m + (1.0 - beta1) * grad
    v = beta2 * v + (1.0 - beta2) * (grad ** 2)
    m_hat = m / (1.0 - beta1 ** t)
    v_hat = v / (1.0 - beta2 ** t)
    w = w - lr * m_hat / (math.sqrt(v_hat) + eps)
    return w, m, v
w, m, v = 5.0, 0.0, 0.0
for step in range(1, 40):
    grad = 2.0 * w
    w, m, v = adam_step(w, grad, m, v, step, lr=0.15)
print(f"Adam Optimized Weight after 40 steps: {w:.4f} (Converged to near 0.0)")
assert abs(w) < 0.2
print("✓ Verified!")"""
    elif m["id"] == "m41":
        # Full topological autograd
        m["code"] = """class Value:
    def __init__(self, data, children=()):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(children)
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other))
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward
        return out
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other))
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out
    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev: build_topo(child)
                topo.append(v)
        build_topo(self)
        self.grad = 1.0
        for v in reversed(topo):
            v._backward()

# Test f(x, y) = x * y + x at x=2, y=3 -> df/dx = y + 1 = 4.0
x = Value(2.0); y = Value(3.0)
z = x * y + x
z.backward()
print(f"Autograd: z = {z.data}, dz/dx = {x.grad} (Expected 4.0), dz/dy = {y.grad} (Expected 2.0)")
assert x.grad == 4.0 and y.grad == 2.0
print("✓ Verified!")"""

with open("omni_academy/curriculum_data.js", "w") as f:
    f.write("// Complete 50-Module Omni-Curriculum Database: NCERT 6th to PhD\n")
    f.write("window.OMNI_MODULES = " + json.dumps(data, indent=2) + ";\n")

print("Fixed the 3 modules cleanly!")
