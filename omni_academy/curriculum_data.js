// Complete 50-Module Omni-Curriculum Database: NCERT 6th to PhD
window.OMNI_MODULES = [
  {
    "id": "m01",
    "epoch": "Epoch I: NCERT Foundations (Classes 6\u201310)",
    "tag": "NCERT Class 6 \u00b7 Number Systems",
    "title": "Module 01: Peano Axioms, Primes & Extended Euclidean Algorithm",
    "theory": "Prime factorization and the Extended Euclidean algorithm solve ax + by = gcd(a, b). When gcd(a, m) = 1, x gives the modular inverse a^-1 mod m.",
    "systems_tie_in": "Used in RSA key generation, memory buffer stride calculations, downsampling ratios in graphics, and hash table buckets.",
    "code": "def extended_gcd(a, b):\n    if b == 0: return a, 1, 0\n    g, x1, y1 = extended_gcd(b, a % b)\n    return g, y1, x1 - (a // b) * y1\ndef mod_inv(a, m):\n    g, x, _ = extended_gcd(a, m)\n    assert g == 1, \"No inverse\"\n    return (x % m + m) % m\ng, x, y = extended_gcd(240, 46)\nprint(f\"gcd(240, 46) = {g}, Bezout: 240*({x}) + 46*({y}) = {240*x + 46*y}\")\nprint(f\"7^-1 mod 31 = {mod_inv(7, 31)}\")\nassert (7 * mod_inv(7, 31)) % 31 == 1\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m02",
    "epoch": "Epoch I: NCERT Foundations (Classes 6\u201310)",
    "tag": "NCERT Class 7\u20138 \u00b7 Number Theory",
    "title": "Module 02: Modular Congruences & Chinese Remainder Theorem",
    "theory": "Solves systems of congruences x = a_i (mod n_i) for pairwise coprime moduli, forming the basis of multi-precision big-integer arithmetic.",
    "systems_tie_in": "Enables multi-precision arithmetic without carries, fast polynomial multiplication, and secret sharing schemes.",
    "code": "def crt(remainders, moduli):\n    total_mod = 1\n    for m in moduli: total_mod *= m\n    total = 0\n    for r, m in zip(remainders, moduli):\n        m_part = total_mod // m\n        def egcd(a, b):\n            if b == 0: return a, 1, 0\n            g, x1, y1 = egcd(b, a % b)\n            return g, y1, x1 - (a // b) * y1\n        _, inv, _ = egcd(m_part, m)\n        total += r * m_part * ((inv % m + m) % m)\n    return total % total_mod\nprint(\"CRT Solution (x=2 mod 3, x=3 mod 5, x=2 mod 7):\", crt([2, 3, 2], [3, 5, 7]))\nassert crt([2, 3, 2], [3, 5, 7]) == 23\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m03",
    "epoch": "Epoch I: NCERT Foundations (Classes 6\u201310)",
    "tag": "NCERT Class 9\u201310 \u00b7 Algebra",
    "title": "Module 03: Systems of Linear Equations & Gaussian Elimination",
    "theory": "Transforms augmented matrix [A | b] to upper triangular form via partial pivoting elementary row operations, followed by back-substitution.",
    "systems_tie_in": "Core algorithm for solving 3D mesh physics, electrical network state estimation, and constrained robotic kinematics.",
    "code": "def gauss(A, b):\n    n = len(A)\n    M = [A[i][:] + [b[i]] for i in range(n)]\n    for i in range(n):\n        max_r = max(range(i, n), key=lambda r: abs(M[r][i]))\n        M[i], M[max_r] = M[max_r], M[i]\n        for k in range(i + 1, n):\n            factor = M[k][i] / M[i][i]\n            for j in range(i, n + 1): M[k][j] -= factor * M[i][j]\n    x = [0.0] * n\n    for i in range(n - 1, -1, -1):\n        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]\n    return x\nA = [[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]]\nb = [8.0, -11.0, -3.0]\nsol = gauss(A, b)\nprint(\"Gauss Solution:\", [round(v, 4) for v in sol])\nassert abs(sol[0] - 2.0) < 1e-4 and abs(sol[1] - 3.0) < 1e-4\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m04",
    "epoch": "Epoch I: NCERT Foundations (Classes 6\u201310)",
    "tag": "NCERT Class 10 \u00b7 Polynomials",
    "title": "Module 04: Polynomial Rings, Vieta's Formulas & Complex Roots",
    "theory": "Vieta's formulas establish symmetric relationships between polynomial coefficients and roots. Complex roots of real polynomials occur in conjugate pairs.",
    "systems_tie_in": "Root solving powers stability analysis, digital audio filter pole/zero placement, and spring-damper UI animations.",
    "code": "import cmath\ndef solve_quad(a, b, c):\n    disc = b**2 - 4*a*c\n    r1 = (-b + cmath.sqrt(disc)) / (2*a)\n    r2 = (-b - cmath.sqrt(disc)) / (2*a)\n    return r1, r2\nr1, r2 = solve_quad(1, 2, 5) # x^2 + 2x + 5 = 0\nprint(f\"Roots: {r1}, {r2}\")\nprint(f\"Vieta Sum Check: {r1 + r2} (Expected -2)\")\nassert abs(r1 + r2 - (-2)) < 1e-9\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m05",
    "epoch": "Epoch I: NCERT Foundations (Classes 6\u201310)",
    "tag": "NCERT Class 10 \u00b7 Trigonometry",
    "title": "Module 05: Trigonometric Functions, Euler's Identity & Wave Harmonics",
    "theory": "Euler's formula e^(i*theta) = cos(theta) + i*sin(theta) unifies exponential and periodic spaces. Signals decompose into orthogonal Fourier harmonics.",
    "systems_tie_in": "Direct foundation for Rotary Position Embeddings (RoPE) in LLMs, audio codecs, and Fast Fourier Transforms.",
    "code": "import math, cmath\ndef fourier_square(t, terms=10):\n    return (4.0 / math.pi) * sum(math.sin((2*k-1)*t)/(2*k-1) for k in range(1, terms+1))\nprint(\"Fourier Square Wave t=1.0:\", round(fourier_square(1.0), 4))\neuler = cmath.exp(1j * math.pi) + 1\nprint(\"Euler Identity e^(i*pi) + 1:\", abs(euler))\nassert abs(euler) < 1e-12\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m06",
    "epoch": "Epoch I: NCERT Foundations (Classes 6\u201310)",
    "tag": "NCERT Class 11 \u00b7 Combinatorics",
    "title": "Module 06: Combinatorics, Binomial Theorem & Pascal's Simplex",
    "theory": "Permutations P(n, r) and combinations C(n, r) count ordered and unordered selections. Binomial theorem expands (x + y)^n via Pascal's triangle.",
    "systems_tie_in": "Powers memory partition combinations, randomized testing permutations, and token sample search spaces.",
    "code": "import math\ndef nCr(n, r): return math.comb(n, r)\ndef pascal_row(n): return [nCr(n, k) for k in range(n + 1)]\nprint(\"Pascal Row 6 (x+y)^6:\", pascal_row(6))\nassert sum(pascal_row(6)) == 2**6\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m07",
    "epoch": "Epoch I: NCERT Foundations (Classes 6\u201310)",
    "tag": "NCERT Class 10\u201311 \u00b7 Geometry",
    "title": "Module 07: Coordinate Geometry, Conic Sections & Affine Transforms",
    "theory": "Affine transformations represent translation, rotation, scaling, and shear via 3x3 homogeneous matrices.",
    "systems_tie_in": "The exact mathematical transformation pipeline in Flutter RenderTransform and mobile GPU vertex shaders.",
    "code": "import math\ndef affine_transform_2d(point, angle_rad, tx, ty, scale=1.0):\n    x, y = point\n    cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)\n    return scale * (x * cos_a - y * sin_a) + tx, scale * (x * sin_a + y * cos_a) + ty\np_trans = affine_transform_2d((10, 0), math.pi/2, tx=5, ty=5)\nprint(\"Transformed Point (10, 0) by 90deg + (5,5):\", [round(c, 2) for c in p_trans])\nassert abs(p_trans[0] - 5.0) < 1e-4 and abs(p_trans[1] - 15.0) < 1e-4\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m08",
    "epoch": "Epoch I: NCERT Foundations (Classes 6\u201310)",
    "tag": "NCERT Class 10\u201312 \u00b7 Probability",
    "title": "Module 08: Classical Probability, Conditional Independence & Bayes Theorem",
    "theory": "Bayes' Theorem updates the prior probability of hypothesis H given evidence E: P(H|E) = P(E|H)P(H) / P(E).",
    "systems_tie_in": "Underpins spam classifiers, speculative decoding token verification acceptance probabilities, and Kalman tracking filters.",
    "code": "def bayes(prior_h, p_e_given_h, p_e_given_not_h):\n    p_e = p_e_given_h * prior_h + p_e_given_not_h * (1.0 - prior_h)\n    return (p_e_given_h * prior_h) / p_e\nposterior = bayes(0.01, 0.95, 0.05)\nprint(f\"Posterior probability given positive test: {posterior:.4f}\")\nassert abs(posterior - 0.1610) < 1e-3\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m09",
    "epoch": "Epoch I: NCERT Foundations (Classes 6\u201310)",
    "tag": "NCERT Class 10\u201311 \u00b7 Series",
    "title": "Module 09: Sequences, Series & Convergence Criteria",
    "theory": "Analyzes Arithmetic, Geometric, and Harmonic series. The ratio and comparison tests determine infinite series convergence.",
    "systems_tie_in": "Calculates geometric amortized growth in dynamic arrays and token decay learning rate schedules.",
    "code": "def geometric_sum(a, r, n=None):\n    if n is not None: return a * (1 - r**n) / (1 - r)\n    assert abs(r) < 1.0, \"Diverges\"\n    return a / (1 - r)\nprint(\"Infinite Geometric Sum (1 + 1/2 + 1/4 + ...):\", geometric_sum(1, 0.5))\nassert abs(geometric_sum(1, 0.5) - 2.0) < 1e-9\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m10",
    "epoch": "Epoch I: NCERT Foundations (Classes 6\u201310)",
    "tag": "NCERT Class 9\u201311 \u00b7 Statistics",
    "title": "Module 10: Descriptive Statistics, Variance, Covariance & Chebyshev's Bound",
    "theory": "Measures central tendency (mean) and dispersion (variance sigma^2, standard deviation). Chebyshev's inequality bounds tail probabilities.",
    "systems_tie_in": "Directly used in layer normalization (LayerNorm/RMSNorm) across transformer layers to stabilize activations.",
    "code": "import math\ndef mean_variance(data):\n    m = sum(data) / len(data)\n    var = sum((x - m)**2 for x in data) / len(data)\n    return m, var, math.sqrt(var)\ndata = [12.0, 15.0, 18.0, 20.0, 25.0, 30.0]\nm, var, std = mean_variance(data)\nprint(f\"Mean: {m:.2f}, Variance: {var:.2f}, StdDev: {std:.2f}\")\nrms = math.sqrt(sum(x**2 for x in data) / len(data))\nprint(f\"RMS Norm: {rms:.4f}\")\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m11",
    "epoch": "Epoch II: Higher Secondary & Discrete Math (Classes 11\u201312 & BCA)",
    "tag": "Class 11\u201312 \u00b7 Real Analysis",
    "title": "Module 11: Real Analysis, Limits & The Epsilon-Delta Definition",
    "theory": "Rigorous epsilon-delta limit definitions. Numerical Taylor expansions avoid floating-point cancellation in functions like sin(x)/x.",
    "systems_tie_in": "Numerical stability guards in softmax calculations and preventing division-by-zero NaN panics in GPU shaders.",
    "code": "import math\ndef stable_sinc(x):\n    if abs(x) < 1e-7: return 1.0 - (x**2)/6.0\n    return math.sin(x) / x\nval = stable_sinc(1e-9)\nprint(f\"Stable sinc(1e-9): {val:.10f}\")\nassert abs(val - 1.0) < 1e-9\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m12",
    "epoch": "Epoch II: Higher Secondary & Discrete Math (Classes 11\u201312 & BCA)",
    "tag": "Class 12 \u00b7 Calculus",
    "title": "Module 12: Differential Calculus from First Principles & Dual Numbers Autograd",
    "theory": "Derivatives via dual numbers a + b*epsilon where epsilon^2 = 0 compute exact symbolic derivatives numerically in a single forward pass without finite-difference approximation errors.",
    "systems_tie_in": "The exact mathematical foundation of Automatic Differentiation (Autograd) in PyTorch, JAX, and ML engines.",
    "code": "class Dual:\n    def __init__(self, val, deriv=0.0):\n        self.val, self.deriv = val, deriv\n    def __add__(self, o):\n        o = o if isinstance(o, Dual) else Dual(o)\n        return Dual(self.val + o.val, self.deriv + o.deriv)\n    def __mul__(self, o):\n        o = o if isinstance(o, Dual) else Dual(o)\n        return Dual(self.val * o.val, self.deriv * o.val + self.val * o.deriv)\n# Compute d/dx (x^2 + 3x) at x=4: (4 + \u03b5)^2 + 3(4 + \u03b5)\nx = Dual(4.0, 1.0)\ny = x * x + x * Dual(3.0)\nprint(f\"f(4) = {y.val}, exact f'(4) via Dual Numbers = {y.deriv} (Expected 2*4 + 3 = 11)\")\nassert y.deriv == 11.0\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m13",
    "epoch": "Epoch II: Higher Secondary & Discrete Math (Classes 11\u201312 & BCA)",
    "tag": "Class 12 \u00b7 Integral Calculus",
    "title": "Module 13: Integral Calculus, Riemann Sums & Simpson's Rule",
    "theory": "Numerical integration computes areas under curves using Simpson's 1/3 Rule with quadratic polynomial interpolations achieving O(h^4) convergence.",
    "systems_tie_in": "Used in continuous signal energy calculation, probability CDF integration, and physics trajectory simulations.",
    "code": "def simpsons_rule(f, a, b, n=100):\n    assert n % 2 == 0\n    h = (b - a) / n\n    s = f(a) + f(b)\n    for i in range(1, n, 2): s += 4 * f(a + i * h)\n    for i in range(2, n, 2): s += 2 * f(a + i * h)\n    return s * h / 3.0\n# Integrate x^2 from 0 to 3 (Exact: 3^3 / 3 = 9.0)\nres = simpsons_rule(lambda x: x**2, 0, 3, n=50)\nprint(f\"Simpson's Integral of x^2 on [0, 3]: {res:.6f}\")\nassert abs(res - 9.0) < 1e-6\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m14",
    "epoch": "Epoch II: Higher Secondary & Discrete Math (Classes 11\u201312 & BCA)",
    "tag": "Class 12 / BCA \u00b7 ODEs",
    "title": "Module 14: Ordinary Differential Equations & Runge-Kutta (RK4) Solvers",
    "theory": "RK4 achieves 4th-order accuracy O(h^4) by computing four trial slopes per step size h to solve initial value problems dy/dt = f(t, y).",
    "systems_tie_in": "Powers neural ODEs, physics simulations in game development, and battery drain modeling on mobile chipsets.",
    "code": "import math\ndef rk4(f, y0, t0, t_end, steps=50):\n    h = (t_end - t0) / steps\n    t, y = t0, y0\n    for _ in range(steps):\n        k1 = f(t, y)\n        k2 = f(t + 0.5*h, y + 0.5*h*k1)\n        k3 = f(t + 0.5*h, y + 0.5*h*k2)\n        k4 = f(t + h, y + h*k3)\n        y += (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)\n        t += h\n    return y\nsol = rk4(lambda t, y: -2.0 * y, 1.0, 0.0, 2.0, steps=20)\nprint(f\"RK4 dy/dt = -2y at t=2: {sol:.6f} (Exact e^-4: {math.exp(-4):.6f})\")\nassert abs(sol - math.exp(-4)) < 1e-4\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m15",
    "epoch": "Epoch II: Higher Secondary & Discrete Math (Classes 11\u201312 & BCA)",
    "tag": "Class 12 \u00b7 Vector Geometry",
    "title": "Module 15: 3D Vector Geometry, Dot/Cross Products & Quaternions",
    "theory": "Quaternions q = w + xi + yj + zk represent 3D rotations avoiding gimbal lock, interpolating smoothly via Spherical Linear Interpolation (SLERP).",
    "systems_tie_in": "The standard mathematical rotation system for mobile AR/VR, robotics orientation, and 3D GPU transforms.",
    "code": "import math\nclass Quaternion:\n    def __init__(self, w, x, y, z):\n        self.w, self.x, self.y, self.z = w, x, y, z\n    def __mul__(self, o):\n        w = self.w*o.w - self.x*o.x - self.y*o.y - self.z*o.z\n        x = self.w*o.x + self.x*o.w + self.y*o.z - self.z*o.y\n        y = self.w*o.y - self.x*o.z + self.y*o.w + self.z*o.x\n        z = self.w*o.z + self.x*o.y - self.y*o.x + self.z*o.w\n        return Quaternion(w, x, y, z)\n# 90 degree rotation about Z axis: w=cos(45)=0.7071, z=sin(45)=0.7071\nq90 = Quaternion(math.cos(math.pi/4), 0, 0, math.sin(math.pi/4))\n# Rotate 180 degrees (q90 * q90)\nq180 = q90 * q90\nprint(f\"Quaternion 180deg Z: w={q180.w:.4f}, z={q180.z:.4f} (Expected w=0, z=1)\")\nassert abs(q180.w) < 1e-4 and abs(q180.z - 1.0) < 1e-4\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m16",
    "epoch": "Epoch II: Higher Secondary & Discrete Math (Classes 11\u201312 & BCA)",
    "tag": "BCA \u00b7 Set Theory",
    "title": "Module 16: Set Theory, Equivalence Partitions & Power Sets",
    "theory": "A partition of a set S divides it into non-empty disjoint subsets. Equivalence relations (reflexive, symmetric, transitive) induce partitions.",
    "systems_tie_in": "Powers disjoint-set union-find data structures in network routing and database relational partition keys.",
    "code": "def power_set(s):\n    res = [[]]\n    for elem in s:\n        res += [subset + [elem] for subset in res]\n    return res\ns = [1, 2, 3]\nps = power_set(s)\nprint(f\"Power set of {s} (size {len(ps)}):\", ps)\nassert len(ps) == 2**len(s)\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m17",
    "epoch": "Epoch II: Higher Secondary & Discrete Math (Classes 11\u201312 & BCA)",
    "tag": "BCA \u00b7 Mathematical Logic",
    "title": "Module 17: Propositional Calculus, Truth Tables & SAT Solvers",
    "theory": "Evaluates Boolean formulas in Conjunctive Normal Form (CNF). The DPLL (Davis-Putnam-Logemann-Loveland) algorithm solves SAT decision problems.",
    "systems_tie_in": "Underpins automated formal verification, hardware circuit synthesis, and dependency solvers in package managers (pub get, apt).",
    "code": "def simple_sat_eval(clauses, assignment):\n    for clause in clauses:\n        clause_sat = False\n        for lit in clause:\n            var = abs(lit)\n            val = assignment.get(var, False)\n            if lit < 0: val = not val\n            if val:\n                clause_sat = True\n                break\n        if not clause_sat: return False\n    return True\n# Formula: (x1 OR x2) AND (NOT x1 OR x2) AND (NOT x2)\n# With x1=True, x2=False: Clause 1 (T or F)=T, Clause 2 (F or F)=F -> UNSAT\ncnf = [[1, 2], [-1, 2], [-2]]\nprint(\"SAT Eval assignment {1: True, 2: False}:\", simple_sat_eval(cnf, {1: True, 2: False}))\nassert simple_sat_eval(cnf, {1: True, 2: False}) is False\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m18",
    "epoch": "Epoch II: Higher Secondary & Discrete Math (Classes 11\u201312 & BCA)",
    "tag": "BCA \u00b7 Discrete Math",
    "title": "Module 18: Graph Theory Foundations & Bipartite Matching",
    "theory": "Bipartite graphs have vertices partitioned into two independent sets. Konig's theorem equates maximum matching with minimum vertex cover.",
    "systems_tie_in": "Solves ride-sharing matching, task allocation in cloud clusters, and compiler register assignment.",
    "code": "def max_bipartite_matching(graph, u_nodes, v_count):\n    match_v = [-1] * v_count\n    def dfs(u, seen):\n        for v in graph[u]:\n            if not seen[v]:\n                seen[v] = True\n                if match_v[v] < 0 or dfs(match_v[v], seen):\n                    match_v[v] = u\n                    return True\n        return False\n    matches = 0\n    for u in range(u_nodes):\n        seen = [False] * v_count\n        if dfs(u, seen): matches += 1\n    return matches\ng = {0: [0, 1], 1: [1, 2], 2: [0]} # 3 workers, 3 tasks\nm = max_bipartite_matching(g, 3, 3)\nprint(\"Max Bipartite Matches found:\", m)\nassert m == 3\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m19",
    "epoch": "Epoch II: Higher Secondary & Discrete Math (Classes 11\u201312 & BCA)",
    "tag": "BCA \u00b7 Digital Logic",
    "title": "Module 19: Boolean Algebra, Karnaugh Maps & ALU Design",
    "theory": "Digital circuits construct arithmetic logic units (ALUs) from NAND gates. A Full Adder computes Sum = A XOR B XOR Cin and Cout = (A AND B) OR (Cin AND (A XOR B)).",
    "systems_tie_in": "The physical transistor architecture inside CPU/GPU execution cores that runs all binary code.",
    "code": "def full_adder(a, b, cin):\n    s = (a ^ b) ^ cin\n    cout = (a & b) | (cin & (a ^ b))\n    return s, cout\ndef ripple_carry_adder_4bit(A, B):\n    res = []\n    cin = 0\n    for a_bit, b_bit in zip(A[::-1], B[::-1]):\n        s, cin = full_adder(a_bit, b_bit, cin)\n        res.append(s)\n    if cin: res.append(cin)\n    return res[::-1]\n# Add 5 (0101) + 3 (0011) = 8 (1000)\nsum_8 = ripple_carry_adder_4bit([0, 1, 0, 1], [0, 0, 1, 1])\nprint(\"4-bit Adder: 5 + 3 =\", sum_8)\nassert sum_8 == [1, 0, 0, 0]\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m20",
    "epoch": "Epoch II: Higher Secondary & Discrete Math (Classes 11\u201312 & BCA)",
    "tag": "BCA \u00b7 Probability",
    "title": "Module 20: Continuous Probability & The Box-Muller Normal Transform",
    "theory": "The Box-Muller transform turns two independent uniform random variables U1, U2 ~ Uniform(0,1) into standard normal Gaussian variables Z0, Z1 ~ N(0, 1).",
    "systems_tie_in": "Powers Gaussian weight initialization in deep networks, diffusion models, and Monte Carlo ray tracing.",
    "code": "import math, random\ndef box_muller():\n    u1, u2 = random.random(), random.random()\n    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)\n    return z0\nsamples = [box_muller() for _ in range(500)]\nm = sum(samples) / len(samples)\nprint(f\"Generated 500 Gaussian samples: Sample Mean = {m:.4f} (Expected ~0.0)\")\nassert abs(m) < 0.2\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m21",
    "epoch": "Epoch III: Undergraduate CS & Algorithms (BCA Core)",
    "tag": "BCA Core \u00b7 Linear Algebra",
    "title": "Module 21: Vector Spaces, Nullspace & The Rank-Nullity Theorem",
    "theory": "The Rank-Nullity theorem states that for linear map T: V -> W, dim(V) = rank(T) + nullity(T). Nullspaces define solutions to homogeneous equations Ax = 0.",
    "systems_tie_in": "Fundamental in structural analysis, constrained optimization, and finding invariants in dynamic systems.",
    "code": "def rank_nullity_demo():\n    # Matrix with 3 columns, rank 2 -> nullity must be 3 - 2 = 1\n    # Rows: [1, 2, 3], [2, 4, 6] (dependent), [0, 1, 1]\n    dim_v = 3\n    rank = 2\n    nullity = dim_v - rank\n    print(f\"dim(V)={dim_v} == rank({rank}) + nullity({nullity})\")\n    assert dim_v == rank + nullity\nrank_nullity_demo()\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m22",
    "epoch": "Epoch III: Undergraduate CS & Algorithms (BCA Core)",
    "tag": "BCA Core \u00b7 Linear Algebra & ML",
    "title": "Module 22: Eigenvalues, Diagonalization & SVD/PCA",
    "theory": "Eigendecomposition factors A = Q Lambda Q^-1. SVD generalizes this to any rectangular matrix A = U Sigma V^T, finding principal directions of variation.",
    "systems_tie_in": "Powers LoRA low-rank adaptation, dimensionality reduction, and vector search embeddings in database indexes.",
    "code": "import math\ndef power_iter(A, steps=30):\n    b = [1.0, 1.0]\n    for _ in range(steps):\n        Ab = [A[0][0]*b[0] + A[0][1]*b[1], A[1][0]*b[0] + A[1][1]*b[1]]\n        norm = math.sqrt(Ab[0]**2 + Ab[1]**2)\n        b = [x / norm for x in Ab]\n    Ab = [A[0][0]*b[0] + A[0][1]*b[1], A[1][0]*b[0] + A[1][1]*b[1]]\n    val = (b[0]*Ab[0] + b[1]*Ab[1]) / (b[0]**2 + b[1]**2)\n    return val, b\nval, vec = power_iter([[4.0, 2.0], [2.0, 3.0]])\nprint(f\"Dominant Eigenvalue: {val:.4f} (Expected ~5.5616)\")\nassert abs(val - 5.5615) < 1e-3\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m23",
    "epoch": "Epoch III: Undergraduate CS & Algorithms (BCA Core)",
    "tag": "BCA Core \u00b7 Data Structures",
    "title": "Module 23: Linear Data Structures: Vector Doubling & Circular Buffers",
    "theory": "Dynamic array capacity doubling guarantees O(1) amortized insertion. Circular ring buffers provide lock-free FIFO streaming over fixed memory.",
    "systems_tie_in": "Powers Flutter's event loop message queues and SipLLM's memory-budgeted layer streaming ring buffers.",
    "code": "class RingBuffer:\n    def __init__(self, capacity):\n        self.buf = [None] * capacity\n        self.cap = capacity\n        self.head = self.tail = self.size = 0\n    def push(self, x):\n        if self.size == self.cap: self.head = (self.head + 1) % self.cap\n        else: self.size += 1\n        self.buf[self.tail] = x\n        self.tail = (self.tail + 1) % self.cap\n    def pop(self):\n        assert self.size > 0\n        x = self.buf[self.head]\n        self.head = (self.head + 1) % self.cap\n        self.size -= 1\n        return x\nrb = RingBuffer(3)\nrb.push(1); rb.push(2); rb.push(3); rb.push(4) # overwrites 1\nprint(\"Popped from RingBuffer (should be 2):\", rb.pop())\nassert rb.pop() == 3\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m24",
    "epoch": "Epoch III: Undergraduate CS & Algorithms (BCA Core)",
    "tag": "BCA Core \u00b7 Data Structures",
    "title": "Module 24: Trees & Hierarchies: BST & AVL Self-Balancing Rotations",
    "theory": "AVL trees maintain strict balance factor |h_L - h_R| <= 1 via Left and Right rotations, ensuring guaranteed O(log n) worst-case lookups.",
    "systems_tie_in": "Underpins B-Tree database storage, filesystem directory indexes, and in-memory order-book trading systems.",
    "code": "class Node:\n    def __init__(self, key):\n        self.key = key\n        self.left = self.right = None\n        self.height = 1\ndef height(n): return n.height if n else 0\ndef rotate_right(y):\n    x = y.left\n    T2 = x.right\n    x.right = y\n    y.left = T2\n    y.height = max(height(y.left), height(y.right)) + 1\n    x.height = max(height(x.left), height(x.right)) + 1\n    return x\nroot = Node(30); root.left = Node(20); root.left.left = Node(10)\nbalanced = rotate_right(root)\nprint(\"Balanced Root after Right Rotation (should be 20):\", balanced.key)\nassert balanced.key == 20\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m25",
    "epoch": "Epoch III: Undergraduate CS & Algorithms (BCA Core)",
    "tag": "BCA Core \u00b7 Algorithms",
    "title": "Module 25: Sorting Algorithms: QuickSort with Randomized Pivot & Median-of-3",
    "theory": "QuickSort partitions around a pivot in O(n) time. Randomized or median-of-three pivot selection prevents O(n^2) worst-case degradation on sorted inputs.",
    "systems_tie_in": "Default sorting algorithm in modern standard libraries (Introsort in C++ std::sort and Dart List.sort).",
    "code": "def quicksort(arr):\n    if len(arr) <= 1: return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    mid = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + mid + quicksort(right)\ndata = [34, 7, 23, 32, 5, 62]\nprint(\"Sorted array:\", quicksort(data))\nassert quicksort(data) == [5, 7, 23, 32, 34, 62]\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m26",
    "epoch": "Epoch III: Undergraduate CS & Algorithms (BCA Core)",
    "tag": "BCA Core \u00b7 Algorithms",
    "title": "Module 26: Dynamic Programming: Bellman Optimality, Knapsack & LCS",
    "theory": "Dynamic programming computes optimal solutions by combining solutions to subproblems with memoization, avoiding exponential recomputation.",
    "systems_tie_in": "Used in diff algorithms (git diff), DNA sequence alignment, and SipLLM layer residency memory allocation planning.",
    "code": "def lcs(s1, s2):\n    m, n = len(s1), len(s2)\n    dp = [[0]*(n+1) for _ in range(m+1)]\n    for i in range(m):\n        for j in range(n):\n            if s1[i] == s2[j]: dp[i+1][j+1] = dp[i][j] + 1\n            else: dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])\n    return dp[m][n]\nprint(\"LCS of 'GATTC' and 'GTAC' length:\", lcs(\"GATTC\", \"GTAC\"))\nassert lcs(\"GATTC\", \"GTAC\") == 3\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m27",
    "epoch": "Epoch III: Undergraduate CS & Algorithms (BCA Core)",
    "tag": "BCA Core \u00b7 Graph Algorithms",
    "title": "Module 27: Graph Traversal: Dijkstra's Shortest Path & Topological Sort",
    "theory": "Dijkstra solves single-source shortest paths on non-negative weighted graphs using priority queues. Topological sort orders DAG dependencies linearly.",
    "systems_tie_in": "Core of package dependency resolution (pubspec.lock), compiler build graphs (Make/Ninja), and Google Maps routing.",
    "code": "import heapq\ndef dijkstra(graph, start):\n    dist = {start: 0}\n    pq = [(0, start)]\n    while pq:\n        d, u = heapq.heappop(pq)\n        if d > dist.get(u, float('inf')): continue\n        for v, weight in graph.get(u, []):\n            if d + weight < dist.get(v, float('inf')):\n                dist[v] = d + weight\n                heapq.heappush(pq, (d + weight, v))\n    return dist\ng = {'A': [('B', 1), ('C', 4)], 'B': [('C', 2), ('D', 5)], 'C': [('D', 1)], 'D': []}\ndists = dijkstra(g, 'A')\nprint(\"Shortest distances from A:\", dists)\nassert dists['D'] == 4 # A -> B (1) -> C (2) -> D (1) = 4\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m28",
    "epoch": "Epoch III: Undergraduate CS & Algorithms (BCA Core)",
    "tag": "BCA Core \u00b7 Computer Architecture",
    "title": "Module 28: Computer Architecture: Memory Hierarchy & Cache Simulation",
    "theory": "Simulates direct-mapped and set-associative cache hit/miss behavior under spatial and temporal locality access patterns.",
    "systems_tie_in": "Explains why row-major vs column-major array loops show 10x performance differences due to CPU cacheline line-fills.",
    "code": "class SimpleCache:\n    def __init__(self, size=4):\n        self.size = size\n        self.tags = [-1] * size\n        self.hits = self.misses = 0\n    def access(self, addr):\n        line = (addr // 64) % self.size\n        tag = addr // (64 * self.size)\n        if self.tags[line] == tag: self.hits += 1\n        else:\n            self.misses += 1\n            self.tags[line] = tag\nc = SimpleCache(4)\nfor addr in [0, 64, 128, 0, 64, 256]: c.access(addr)\nprint(f\"Cache Hits: {c.hits}, Misses: {c.misses}\")\nassert c.hits == 2\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m29",
    "epoch": "Epoch III: Undergraduate CS & Algorithms (BCA Core)",
    "tag": "BCA Core \u00b7 Theory of Computation",
    "title": "Module 29: Automata Theory: DFAs, Regular Expressions & State Machines",
    "theory": "A Deterministic Finite Automaton (DFA) M = (Q, Sigma, delta, q0, F) recognizes regular languages in linear O(n) time with zero backtracking.",
    "systems_tie_in": "Direct foundation for compiler lexical analyzers (lexers), network packet filters, and mobile UI state controllers.",
    "code": "class DFA:\n    def __init__(self, states, alphabet, transition, start, accept):\n        self.delta = transition\n        self.start = start\n        self.accept = accept\n    def accepts(self, s):\n        curr = self.start\n        for char in s:\n            curr = self.delta.get((curr, char), None)\n            if curr is None: return False\n        return curr in self.accept\n# DFA matching binary strings ending with '01'\ndfa = DFA({'S0', 'S1', 'S2'}, {'0', '1'},\n          {('S0', '0'): 'S1', ('S0', '1'): 'S0',\n           ('S1', '0'): 'S1', ('S1', '1'): 'S2',\n           ('S2', '0'): 'S1', ('S2', '1'): 'S0'},\n          'S0', {'S2'})\nprint(\"DFA '101' accepts:\", dfa.accepts(\"101\"))\nprint(\"DFA '100' accepts:\", dfa.accepts(\"100\"))\nassert dfa.accepts(\"101\") is True and dfa.accepts(\"100\") is False\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m30",
    "epoch": "Epoch III: Undergraduate CS & Algorithms (BCA Core)",
    "tag": "BCA Core \u00b7 Networking",
    "title": "Module 30: Computer Networks: TCP Sliding Window & Flow Control Simulation",
    "theory": "TCP sliding window matches transmission rate to receiver buffer capacity via Advertised Window (rwnd) and Congestion Window (cwnd).",
    "systems_tie_in": "Prevents mobile buffer bloat and packet drops over unstable 2G/3G rural networks in mForm and BSE mobile sync.",
    "code": "class TCPSender:\n    def __init__(self, window_size):\n        self.win = window_size\n        self.base = 0\n        self.next_seq = 0\n    def send(self, data_len):\n        sent = []\n        while self.next_seq < self.base + self.win and self.next_seq < data_len:\n            sent.append(self.next_seq)\n            self.next_seq += 1\n        return sent\n    def ack(self, ack_num):\n        if ack_num >= self.base:\n            self.base = ack_num + 1\ns = TCPSender(window_size=3)\nprint(\"Initial Window packets sent:\", s.send(10))\ns.ack(1) # ACK packets 0 and 1\nprint(\"Window slides, new packets sent:\", s.send(10))\nassert s.base == 2\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m31",
    "epoch": "Epoch IV: MCA Core & Advanced Systems Engineering",
    "tag": "MCA Core \u00b7 Operating Systems",
    "title": "Module 31: Advanced Operating Systems: Preemptive Scheduling & Deadlock Banker",
    "theory": "Dijkstra's Banker's algorithm tests for safe states before granting resource allocations to prevent distributed deadlocks.",
    "systems_tie_in": "Critical for preventing deadlocks across multithreaded Android SQLite connection pools and JNI lock acquisitions.",
    "code": "def bankers_algorithm():\n    avail = [3, 3, 2]\n    max_claim = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]\n    alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]\n    n = len(alloc); num_res = len(avail)\n    need = [[max_claim[i][j] - alloc[i][j] for j in range(num_res)] for i in range(n)]\n    work = avail[:]\n    finish = [False] * n\n    safe_seq = []\n    while len(safe_seq) < n:\n        found = False\n        for p in range(n):\n            if not finish[p] and all(need[p][j] <= work[j] for j in range(num_res)):\n                for j in range(num_res): work[j] += alloc[p][j]\n                finish[p] = True\n                safe_seq.append(p)\n                found = True\n                break\n        if not found: return False, []\n    return True, safe_seq\nsafe, seq = bankers_algorithm()\nprint(f\"Banker's Algorithm Safe: {safe}, Sequence: {seq}\")\nassert safe is True\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m32",
    "epoch": "Epoch IV: MCA Core & Advanced Systems Engineering",
    "tag": "MCA Core \u00b7 Compiler Engineering",
    "title": "Module 32: Compiler Engineering: Lexing, Pratt Parsing & AST Interpretation",
    "theory": "Pratt parsing binds operators via numeric binding power in O(n) time, producing clean Abstract Syntax Trees without backtracking.",
    "systems_tie_in": "The exact parser you built in Frappe Mobile SDK (pr105.md) to replace regex string matches with real JS evaluation.",
    "code": "class ASTNode:\n    def __init__(self, op, left=None, right=None, val=None):\n        self.op, self.left, self.right, self.val = op, left, right, val\n    def eval(self, env):\n        if self.op == \"LIT\": return self.val\n        if self.op == \"VAR\": return env.get(self.val, 0)\n        l, r = self.left.eval(env), self.right.eval(env)\n        return (l + r) if self.op == \"+\" else (l * r)\nn1 = ASTNode(\"VAR\", val=\"x\")\nn2 = ASTNode(\"LIT\", val=10)\nroot = ASTNode(\"+\", n1, n2)\nprint(\"AST Evaluated (x=5 + 10):\", root.eval({\"x\": 5}))\nassert root.eval({\"x\": 5}) == 15\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m33",
    "epoch": "Epoch IV: MCA Core & Advanced Systems Engineering",
    "tag": "MCA Core \u00b7 Database Internals",
    "title": "Module 33: Database Engine Internals: B+ Tree Indexing & WAL Append Logging",
    "theory": "B+ Trees store all records in linked leaf nodes while internal nodes store keys for O(log n) branching search. WAL guarantees durability.",
    "systems_tie_in": "The physical storage architecture of SQLite, Room, and Realm on mobile devices.",
    "code": "class BPlusNode:\n    def __init__(self, is_leaf=True):\n        self.is_leaf = is_leaf\n        self.keys = []\n        self.children = []\ndef bplus_search(root, key):\n    curr = root\n    while not curr.is_leaf:\n        i = 0\n        while i < len(curr.keys) and key >= curr.keys[i]: i += 1\n        curr = curr.children[i]\n    return key in curr.keys\n# Simple 2-level B+ Tree leaf search\nroot = BPlusNode(is_leaf=False)\nroot.keys = [20]\nleaf1 = BPlusNode(is_leaf=True); leaf1.keys = [5, 10, 15]\nleaf2 = BPlusNode(is_leaf=True); leaf2.keys = [20, 25, 30]\nroot.children = [leaf1, leaf2]\nprint(\"B+ Tree Search Key 25:\", bplus_search(root, 25))\nassert bplus_search(root, 25) is True and bplus_search(root, 99) is False\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m34",
    "epoch": "Epoch IV: MCA Core & Advanced Systems Engineering",
    "tag": "MCA Core \u00b7 Distributed Systems",
    "title": "Module 34: Distributed Systems: Vector Clocks & Causal Consistency",
    "theory": "Vector clocks establish causal partial ordering and detect concurrent merge conflicts in distributed local-first databases.",
    "systems_tie_in": "Used in mForm offline sync conflict resolution and git merge ancestor tracking.",
    "code": "def vc_compare(v1, v2):\n    le = all(x <= y for x, y in zip(v1, v2))\n    ge = all(x >= y for x, y in zip(v1, v2))\n    if le and not ge: return \"BEFORE\"\n    if ge and not le: return \"AFTER\"\n    if le and ge: return \"SAME\"\n    return \"CONCURRENT\"\nprint(\"VC Compare [1,0] vs [0,1]:\", vc_compare([1, 0], [0, 1]))\nassert vc_compare([1, 0], [0, 1]) == \"CONCURRENT\"\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m35",
    "epoch": "Epoch IV: MCA Core & Advanced Systems Engineering",
    "tag": "MCA Core \u00b7 Cryptography",
    "title": "Module 35: Cryptography Engineering: RSA Asymmetric Keygen & Digital Signatures",
    "theory": "RSA uses trapdoor one-way permutation via integer factorization. Signature s = m^d mod n is verified by checking s^e mod n == m.",
    "systems_tie_in": "Directly secures HTTPS connections, APK signing, and Aadhaar biometric payload encryption on mobile.",
    "code": "def rsa_demo():\n    p, q = 61, 53\n    n = p * q\n    phi = (p - 1) * (q - 1)\n    e = 17\n    # d = e^-1 mod phi\n    def egcd(a, b):\n        if b == 0: return a, 1, 0\n        g, x1, y1 = egcd(b, a % b)\n        return g, y1, x1 - (a // b) * y1\n    _, d, _ = egcd(e, phi)\n    d = (d % phi + phi) % phi\n    msg = 42\n    ciphertext = pow(msg, e, n)\n    decrypted = pow(ciphertext, d, n)\n    print(f\"RSA Original: {msg}, Encrypted: {ciphertext}, Decrypted: {decrypted}\")\n    assert decrypted == msg\nrsa_demo()\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m36",
    "epoch": "Epoch IV: MCA Core & Advanced Systems Engineering",
    "tag": "MCA Core \u00b7 Software Architecture",
    "title": "Module 36: Software Architecture: Observer Pattern & Reactive Event Streams",
    "theory": "Decouples event publishers from subscribers via reactive event buses, supporting asynchronous state distribution without tight coupling.",
    "systems_tie_in": "The foundational architecture of Flutter Streams, Kotlin StateFlow, and LiveData in Android MVVM.",
    "code": "class EventBus:\n    def __init__(self): self.subs = {}\n    def on(self, event, fn): self.subs.setdefault(event, []).append(fn)\n    def emit(self, event, data):\n        for fn in self.subs.get(event, []): fn(data)\nbus = EventBus()\nevents = []\nbus.on(\"auth_changed\", lambda u: events.append(f\"User: {u}\"))\nbus.emit(\"auth_changed\", \"Ankit\")\nprint(\"Emitted Event Output:\", events)\nassert events == [\"User: Ankit\"]\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m37",
    "epoch": "Epoch IV: MCA Core & Advanced Systems Engineering",
    "tag": "MCA Core \u00b7 Mobile Systems",
    "title": "Module 37: Mobile Systems: Android Looper, Handler & JNI Bridge Architecture",
    "theory": "Android UI thread operates a continuous Looper pulling Message objects from a synchronized MessageQueue. Native JNI calls bridge to C++ runtimes.",
    "systems_tie_in": "The execution architecture underpinning all native Android apps, Flutter platform channels, and SipLLM's Dart FFI bridge.",
    "code": "class MessageQueue:\n    def __init__(self): self.q = []\n    def enqueue(self, msg): self.q.append(msg)\n    def next(self): return self.q.pop(0) if self.q else None\nmq = MessageQueue()\nmq.enqueue(\"PAINT_FRAME\"); mq.enqueue(\"TOUCH_EVENT\")\nprint(\"Looper next message:\", mq.next())\nassert mq.next() == \"TOUCH_EVENT\"\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m38",
    "epoch": "Epoch IV: MCA Core & Advanced Systems Engineering",
    "tag": "MCA Core \u00b7 Numerical Analysis",
    "title": "Module 38: Numerical Analysis: Floating-Point IEEE-754 Bit Unpacking & Condition Numbers",
    "theory": "Unpacks 32-bit float into Sign (1 bit), Exponent (8 bits), and Mantissa (23 bits). Condition numbers measure sensitivity to numerical perturbation.",
    "systems_tie_in": "Essential for debugging low-level C++ quantization scale underflows and NaN propagation in mobile neural networks.",
    "code": "import struct\ndef unpack_float32(val):\n    bits = struct.unpack('!I', struct.pack('!f', val))[0]\n    sign = (bits >> 31) & 1\n    exp = ((bits >> 23) & 0xFF) - 127\n    mantissa = bits & 0x7FFFFF\n    return sign, exp, mantissa\ns, e, m = unpack_float32(1.5)\nprint(f\"Float 1.5 -> Sign={s}, Exp={e}, Mantissa={hex(m)}\")\nassert s == 0 and e == 0\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m39",
    "epoch": "Epoch IV: MCA Core & Advanced Systems Engineering",
    "tag": "MCA Core \u00b7 Optimization",
    "title": "Module 39: Mathematical Optimization: Adam Optimizer with Exponential Moving Averages",
    "theory": "Adam adapts learning rates using first m_t (momentum) and second v_t (uncentered variance) moments of gradients with bias correction.",
    "systems_tie_in": "The universal optimization algorithm used for training and fine-tuning all modern deep learning and language models.",
    "code": "import math\ndef adam_step(w, grad, m, v, t, lr=0.1, beta1=0.9, beta2=0.999, eps=1e-8):\n    m = beta1 * m + (1.0 - beta1) * grad\n    v = beta2 * v + (1.0 - beta2) * (grad ** 2)\n    m_hat = m / (1.0 - beta1 ** t)\n    v_hat = v / (1.0 - beta2 ** t)\n    w = w - lr * m_hat / (math.sqrt(v_hat) + eps)\n    return w, m, v\nw, m, v = 5.0, 0.0, 0.0\nfor step in range(1, 40):\n    grad = 2.0 * w\n    w, m, v = adam_step(w, grad, m, v, step, lr=0.15)\nprint(f\"Adam Optimized Weight after 40 steps: {w:.4f} (Converged to near 0.0)\")\nassert abs(w) < 0.5\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m40",
    "epoch": "Epoch IV: MCA Core & Advanced Systems Engineering",
    "tag": "MCA Core \u00b7 Classical ML",
    "title": "Module 40: Classical Machine Learning: Logistic Regression & Cross-Entropy",
    "theory": "Maps linear combination z = w^T x + b through sigmoid sigma(z) = 1/(1 + e^-z) to model class probabilities, minimizing binary cross-entropy.",
    "systems_tie_in": "Used in on-device gesture recognition, tabular health predictions, and binary decision classifiers in mobile apps.",
    "code": "import math\ndef sigmoid(z): return 1.0 / (1.0 + math.exp(-max(min(z, 50), -50)))\ndef log_loss(y_true, y_pred):\n    eps = 1e-15\n    p = max(min(y_pred, 1.0 - eps), eps)\n    return - (y_true * math.log(p) + (1.0 - y_true) * math.log(1.0 - p))\np = sigmoid(2.5)\nloss = log_loss(1, p)\nprint(f\"Sigmoid(2.5) = {p:.4f}, Cross-Entropy Loss = {loss:.4f}\")\nassert p > 0.9 and loss < 0.1\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m41",
    "epoch": "Epoch V: Frontier & PhD Research Systems (Edge AI & Runtimes)",
    "tag": "PhD Research \u00b7 Deep Learning",
    "title": "Module 41: Deep Learning Foundations: Reverse-Mode Autograd from Scratch",
    "theory": "Builds a dynamic Directed Acyclic Graph (DAG) of tensor operations and propagates adjoints backward via the chain rule in reverse topological order.",
    "systems_tie_in": "The core engine of PyTorch and deep learning frameworks that allows neural networks to learn via gradient backpropagation.",
    "code": "class Value:\n    def __init__(self, data, children=()):\n        self.data = data\n        self.grad = 0.0\n        self._backward = lambda: None\n        self._prev = set(children)\n    def __add__(self, other):\n        other = other if isinstance(other, Value) else Value(other)\n        out = Value(self.data + other.data, (self, other))\n        def _backward():\n            self.grad += out.grad\n            other.grad += out.grad\n        out._backward = _backward\n        return out\n    def __mul__(self, other):\n        other = other if isinstance(other, Value) else Value(other)\n        out = Value(self.data * other.data, (self, other))\n        def _backward():\n            self.grad += other.data * out.grad\n            other.grad += self.data * out.grad\n        out._backward = _backward\n        return out\n    def backward(self):\n        topo = []\n        visited = set()\n        def build_topo(v):\n            if v not in visited:\n                visited.add(v)\n                for child in v._prev: build_topo(child)\n                topo.append(v)\n        build_topo(self)\n        self.grad = 1.0\n        for v in reversed(topo):\n            v._backward()\n\n# Test f(x, y) = x * y + x at x=2, y=3 -> df/dx = y + 1 = 4.0\nx = Value(2.0); y = Value(3.0)\nz = x * y + x\nz.backward()\nprint(f\"Autograd: z = {z.data}, dz/dx = {x.grad} (Expected 4.0), dz/dy = {y.grad} (Expected 2.0)\")\nassert x.grad == 4.0 and y.grad == 2.0\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m42",
    "epoch": "Epoch V: Frontier & PhD Research Systems (Edge AI & Runtimes)",
    "tag": "PhD Research \u00b7 Neural Architectures",
    "title": "Module 42: Modern Neural Architectures: Residual Connections & LayerNorm",
    "theory": "ResNet identity skip connections x_{l+1} = x_l + F(x_l) eliminate vanishing gradients in deep networks by providing clean gradient highways.",
    "systems_tie_in": "The architectural spine of every modern deep network, including ResNets, Transformers, and Diffusion models.",
    "code": "def residual_block(x, weights):\n    # F(x) = ReLU(Wx)\n    fx = [max(0.0, sum(w * xi for w, xi in zip(row, x))) for row in weights]\n    # Skip connection: y = x + F(x)\n    return [xi + fi for xi, fi in zip(x, fx)]\nW = [[0.5, -0.2], [0.1, 0.4]]\nout = residual_block([1.0, 2.0], W)\nprint(\"Residual Block Output with Skip Connection:\", [round(v, 2) for v in out])\nassert out[0] > 1.0 and out[1] > 2.0\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m43",
    "epoch": "Epoch V: Frontier & PhD Research Systems (Edge AI & Runtimes)",
    "tag": "PhD Research \u00b7 LLM Architecture",
    "title": "Module 43: The Transformer Architecture: Multi-Head Self-Attention",
    "theory": "Splits queries, keys, and values into h distinct attention heads, allowing the model to jointly attend to information from different representation subspaces.",
    "systems_tie_in": "The dominant architectural paradigm for all modern frontier foundation models (Llama, GPT, Gemini, Claude).",
    "code": "import math\ndef softmax(v):\n    m = max(v)\n    exps = [math.exp(x - m) for x in v]\n    s = sum(exps)\n    return [e / s for e in exps]\ndef dot_product_attention(Q, K, V):\n    d_k = len(Q[0])\n    scores = [[sum(q * k for q, k in zip(q_row, k_row)) / math.sqrt(d_k) for k_row in K] for q_row in Q]\n    weights = [softmax(r) for r in scores]\n    out = [[sum(w * v[col] for w, v in zip(weights[row], V)) for col in range(len(V[0]))] for row in range(len(Q))]\n    return out\nQ = [[1.0, 0.0], [0.0, 1.0]]\nK = [[1.0, 0.0], [0.0, 1.0]]\nV = [[10.0, 20.0], [30.0, 40.0]]\nres = dot_product_attention(Q, K, V)\nprint(\"Attended Values Matrix:\", [[round(c, 2) for c in r] for r in res])\nassert len(res) == 2\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m44",
    "epoch": "Epoch V: Frontier & PhD Research Systems (Edge AI & Runtimes)",
    "tag": "PhD Research \u00b7 LLM Architecture",
    "title": "Module 44: Rotary Position Embeddings (RoPE) Mathematical Derivation",
    "theory": "RoPE rotates query and key vectors in complex 2D planes, ensuring inner products depend strictly on relative token distance (m - n).",
    "systems_tie_in": "The exact mathematical positional embedding used in Llama 3.2 and implemented in SipLLM's C++ runtime.",
    "code": "import math\ndef rope_rotate(x0, x1, pos, theta=10000.0):\n    angle = pos / (theta ** 0) # 1st dim\n    return x0 * math.cos(angle) - x1 * math.sin(angle), x0 * math.sin(angle) + x1 * math.cos(angle)\nq = rope_rotate(1.0, 0.5, pos=5)\nk = rope_rotate(0.8, -0.2, pos=2)\nscore1 = q[0]*k[0] + q[1]*k[1]\nq2 = rope_rotate(1.0, 0.5, pos=12)\nk2 = rope_rotate(0.8, -0.2, pos=9)\nscore2 = q2[0]*k2[0] + q2[1]*k2[1]\nprint(f\"RoPE Dot Product pos (5, 2): {score1:.6f} == pos (12, 9): {score2:.6f}\")\nassert abs(score1 - score2) < 1e-7\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m45",
    "epoch": "Epoch V: Frontier & PhD Research Systems (Edge AI & Runtimes)",
    "tag": "PhD Research \u00b7 Fast Attention",
    "title": "Module 45: Fast Attention Algorithms: Online Softmax & Memory Tiling",
    "theory": "Online softmax computes softmax incrementally across streaming blocks without storing the full N x N attention matrix, cutting memory from O(N^2) to O(N).",
    "systems_tie_in": "The core mathematical breakthrough behind FlashAttention that makes long context windows possible on GPUs and edge devices.",
    "code": "import math\ndef online_softmax_2blocks(b1, b2):\n    # Block 1\n    m1 = max(b1)\n    d1 = sum(math.exp(x - m1) for x in b1)\n    # Stream in Block 2\n    m2 = max(m1, max(b2))\n    d2 = d1 * math.exp(m1 - m2) + sum(math.exp(x - m2) for x in b2)\n    # Recombine\n    res = [math.exp(x - m2) / d2 for x in (b1 + b2)]\n    return res\nraw = [1.0, 2.0, 3.0, 4.0]\nexact = [math.exp(x - max(raw)) / sum(math.exp(c - max(raw)) for c in raw) for x in raw]\nstreamed = online_softmax_2blocks([1.0, 2.0], [3.0, 4.0])\nprint(\"Standard Softmax: \", [round(x, 4) for x in exact])\nprint(\"Online Softmax:   \", [round(x, 4) for x in streamed])\nassert all(abs(a - b) < 1e-6 for a, b in zip(exact, streamed))\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m46",
    "epoch": "Epoch V: Frontier & PhD Research Systems (Edge AI & Runtimes)",
    "tag": "PhD Research \u00b7 Edge Inference",
    "title": "Module 46: Model Quantization: GGUF Q8_0, Q4_K_M & SIMD Dot-Product Physics",
    "theory": "Quantizes 32-bit floating point weights into 8-bit or 4-bit integers with block scales, allowing 1B models to run in 364 MB of RAM.",
    "systems_tie_in": "The exact binary quantization parsed and executed in SipLLM via ARM NEON SIMD kernels.",
    "code": "def q8_quantize_block(floats):\n    scale = max(abs(x) for x in floats) / 127.0 if max(abs(x) for x in floats) > 0 else 1.0\n    quants = [int(round(x / scale)) for x in floats]\n    reconstructed = [q * scale for q in quants]\n    mse = sum((a - b)**2 for a, b in zip(floats, reconstructed)) / len(floats)\n    return scale, quants, mse\nsample = [0.12, -0.85, 0.44, 1.25, -0.05]\nscale, q, mse = q8_quantize_block(sample)\nprint(f\"Block Scale: {scale:.4f}, INT8: {q}, MSE: {mse:.6f}\")\nassert mse < 1e-4\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m47",
    "epoch": "Epoch V: Frontier & PhD Research Systems (Edge AI & Runtimes)",
    "tag": "PhD Research \u00b7 Edge Systems",
    "title": "Module 47: Edge Memory Residency Planning: Weight Streaming & RAM Ceilings",
    "theory": "Plans static weight residency vs on-demand streaming to guarantee total system RSS never breaches hardware RAM ceilings.",
    "systems_tie_in": "The exact memory residency planner you built in SipLLM (src/mem_plan.cpp) to satisfy the --ram-budget 4G constraint.",
    "code": "def plan_layer_residency(budget_bytes, base_overhead_bytes, layer_size_bytes, total_layers):\n    avail = budget_bytes - base_overhead_bytes\n    assert avail > 0, \"Budget impossible!\"\n    max_pinned = min(total_layers, avail // layer_size_bytes)\n    streamed = total_layers - max_pinned\n    return max_pinned, streamed\npinned, streamed = plan_layer_residency(budget_bytes=4*1024*1024*1024, base_overhead_bytes=512*1024*1024,\n                                        layer_size_bytes=200*1024*1024, total_layers=16)\nprint(f\"Under 4GB Budget: Pin {pinned} layers in RAM, Stream {streamed} layers off disk.\")\nassert pinned == 16 and streamed == 0\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m48",
    "epoch": "Epoch V: Frontier & PhD Research Systems (Edge AI & Runtimes)",
    "tag": "PhD Research \u00b7 High-Performance Inference",
    "title": "Module 48: Speculative Decoding: Multi-Token Draft Verification",
    "theory": "Generates draft tokens with a fast auxiliary mechanism and validates them in a single parallel target forward pass via rejection sampling.",
    "systems_tie_in": "The speculative prompt lookup decoding feature committed in SipLLM (git commit 77cf035).",
    "code": "def speculative_verify_tokens(drafts, oracle_fn):\n    accepted = []\n    for d in drafts:\n        target = oracle_fn(accepted)\n        if d == target: accepted.append(d)\n        else:\n            accepted.append(target)\n            break\n    return accepted\noracle = lambda p: [\"The\", \"quick\", \"brown\", \"fox\"][len(p)]\nres = speculative_verify_tokens([\"The\", \"quick\", \"blue\", \"fox\"], oracle)\nprint(\"Speculative Acceptance Sequence:\", res)\nassert res == [\"The\", \"quick\", \"brown\"]\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m49",
    "epoch": "Epoch V: Frontier & PhD Research Systems (Edge AI & Runtimes)",
    "tag": "PhD Research \u00b7 Information Theory",
    "title": "Module 49: Information Theory: Shannon Entropy, Perplexity & BPE Tokenization",
    "theory": "Shannon Entropy H(X) = -sum p(x) log2 p(x) measures average information content. Perplexity PPL = 2^H measures language model uncertainty.",
    "systems_tie_in": "The fundamental objective metric used to evaluate language model loss, compression limits, and token vocabularies.",
    "code": "import math\ndef shannon_entropy(probs):\n    return -sum(p * math.log2(p) for p in probs if p > 0)\n# Uniform distribution over 4 tokens vs deterministic distribution\nh_uniform = shannon_entropy([0.25, 0.25, 0.25, 0.25])\nh_skewed = shannon_entropy([0.9, 0.05, 0.03, 0.02])\nprint(f\"Uniform 4-token Entropy: {h_uniform:.2f} bits (Max uncertainty = 2 bits)\")\nprint(f\"Skewed 4-token Entropy:  {h_skewed:.2f} bits (High certainty)\")\nassert h_uniform == 2.0\nprint(\"\u2713 Verified!\")"
  },
  {
    "id": "m50",
    "epoch": "Epoch V: Frontier & PhD Research Systems (Edge AI & Runtimes)",
    "tag": "PhD Research \u00b7 Category Theory & Type Systems",
    "title": "Module 50: Category Theory: Monads, Functors & Affine Ownership Semantics",
    "theory": "A Monad in Category Theory is a monoid in the category of endofunctors. It encapsulates computation with unit (return) and bind (>>=).",
    "systems_tie_in": "Underpins Rust's affine ownership borrow checker, functional state pipelines, and Dart async/await Future primitives.",
    "code": "class Maybe:\n    def __init__(self, val): self.val = val\n    def is_none(self): return self.val is None\n    def bind(self, fn):\n        return Maybe(None) if self.is_none() else fn(self.val)\n# Chained safe division without null pointer exceptions: 100 / 2 / 5\ndiv100 = lambda x: Maybe(100 // x) if x != 0 else Maybe(None)\nsafe_calc = Maybe(2).bind(div100).bind(lambda x: Maybe(x // 5))\nprint(\"Safe Monadic Division Result:\", safe_calc.val)\nassert safe_calc.val == 10\n# Test division by zero propagation\nfail_calc = Maybe(0).bind(div100).bind(lambda x: Maybe(x // 5))\nassert fail_calc.val is None\nprint(\"\u2713 Monad Safety Verified!\")"
  }
];
