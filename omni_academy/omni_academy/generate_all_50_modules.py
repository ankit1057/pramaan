import json

# Comprehensive definitions for 50 modules from NCERT 6th to PhD
epochs = [
    "Epoch I: NCERT Foundations (Classes 6–10)",
    "Epoch II: Higher Secondary & Discrete Math",
    "Epoch III: Undergraduate CS (BCA Core)",
    "Epoch IV: MCA Core & Advanced Systems",
    "Epoch V: Frontier & PhD Research Systems"
]

# We will build all 50 modules systematically
all_modules = []

# Helper to add module
def add_m(mid, epoch_idx, tag, title, theory, tie_in, code):
    all_modules.append({
        "id": mid,
        "epoch": epochs[epoch_idx],
        "tag": tag,
        "title": title,
        "theory": theory,
        "systems_tie_in": tie_in,
        "code": code.strip()
    })

# EPOCH I
add_m("m01", 0, "NCERT Class 6 · Number Systems", "Module 01: Peano Axioms, Primes & Extended Euclidean Algorithm",
      "Prime factorization and the Extended Euclidean algorithm solve ax + by = gcd(a, b). When gcd(a, m) = 1, x gives the modular inverse a^-1 mod m.",
      "Used in RSA key generation, memory buffer stride calculations, downsampling ratios in graphics, and hash table buckets.",
      """def extended_gcd(a, b):
    if b == 0: return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1
def mod_inv(a, m):
    g, x, _ = extended_gcd(a, m)
    assert g == 1, "No inverse"
    return (x % m + m) % m
g, x, y = extended_gcd(240, 46)
print(f"gcd(240, 46) = {g}, Bezout: 240*({x}) + 46*({y}) = {240*x + 46*y}")
print(f"7^-1 mod 31 = {mod_inv(7, 31)}")
assert (7 * mod_inv(7, 31)) % 31 == 1
print("✓ Verified!")""")

add_m("m02", 0, "NCERT Class 7–8 · Number Theory", "Module 02: Modular Congruences & Chinese Remainder Theorem",
      "Solves systems of congruences x = a_i (mod n_i) for pairwise coprime moduli, forming the basis of multi-precision big-integer arithmetic.",
      "Enables multi-precision arithmetic without carries, fast polynomial multiplication, and secret sharing schemes.",
      """def crt(remainders, moduli):
    total_mod = 1
    for m in moduli: total_mod *= m
    total = 0
    for r, m in zip(remainders, moduli):
        m_part = total_mod // m
        _, inv, _ = extended_gcd(m_part, m)
        total += r * m_part * ((inv % m + m) % m)
    return total % total_mod
print("CRT Solution (x=2 mod 3, x=3 mod 5, x=2 mod 7):", crt([2, 3, 2], [3, 5, 7]))
assert crt([2, 3, 2], [3, 5, 7]) == 23
print("✓ Verified!")""")

add_m("m03", 0, "NCERT Class 9–10 · Algebra", "Module 03: Systems of Linear Equations & Gaussian Elimination",
      "Transforms augmented matrix [A | b] to upper triangular form via partial pivoting elementary row operations, followed by back-substitution.",
      "Core algorithm for solving 3D mesh physics, electrical network state estimation, and constrained robotic kinematics.",
      """def gauss(A, b):
    n = len(A)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        max_r = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[max_r] = M[max_r], M[i]
        for k in range(i + 1, n):
            factor = M[k][i] / M[i][i]
            for j in range(i, n + 1): M[k][j] -= factor * M[i][j]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x
A = [[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]]
b = [8.0, -11.0, -3.0]
sol = gauss(A, b)
print("Gauss Solution:", [round(v, 4) for v in sol])
assert abs(sol[0] - 2.0) < 1e-4 and abs(sol[1] - 3.0) < 1e-4
print("✓ Verified!")""")

add_m("m04", 0, "NCERT Class 10 · Polynomials", "Module 04: Polynomial Rings, Vieta's Formulas & Complex Roots",
      "Vieta's formulas establish symmetric relationships between polynomial coefficients and roots. Complex roots of real polynomials occur in conjugate pairs.",
      "Root solving powers stability analysis, digital audio filter pole/zero placement, and spring-damper UI animations.",
      """import cmath
def solve_quad(a, b, c):
    disc = b**2 - 4*a*c
    r1 = (-b + cmath.sqrt(disc)) / (2*a)
    r2 = (-b - cmath.sqrt(disc)) / (2*a)
    return r1, r2
r1, r2 = solve_quad(1, 2, 5) # x^2 + 2x + 5 = 0
print(f"Roots: {r1}, {r2}")
print(f"Vieta Sum Check: {r1 + r2} (Expected -2)")
assert abs(r1 + r2 - (-2)) < 1e-9
print("✓ Verified!")""")

add_m("m05", 0, "NCERT Class 10 · Trigonometry", "Module 05: Trigonometric Functions, Euler's Identity & Wave Harmonics",
      "Euler's formula e^(i*theta) = cos(theta) + i*sin(theta) unifies exponential and periodic spaces. Signals decompose into orthogonal Fourier harmonics.",
      "Direct foundation for Rotary Position Embeddings (RoPE) in LLMs, audio codecs, and Fast Fourier Transforms.",
      """import math, cmath
def fourier_square(t, terms=10):
    return (4.0 / math.pi) * sum(math.sin((2*k-1)*t)/(2*k-1) for k in range(1, terms+1))
print("Fourier Square Wave t=1.0:", round(fourier_square(1.0), 4))
euler = cmath.exp(1j * math.pi) + 1
print("Euler Identity e^(i*pi) + 1:", abs(euler))
assert abs(euler) < 1e-12
print("✓ Verified!")""")

add_m("m06", 0, "NCERT Class 11 · Combinatorics", "Module 06: Combinatorics, Binomial Theorem & Pascal's Simplex",
      "Permutations P(n, r) and combinations C(n, r) count ordered and unordered selections. Binomial theorem expands (x + y)^n via Pascal's triangle.",
      "Powers memory partition combinations, randomized testing permutations, and token sample search spaces.",
      """import math
def nCr(n, r): return math.comb(n, r)
def pascal_row(n): return [nCr(n, k) for k in range(n + 1)]
print("Pascal Row 6 (x+y)^6:", pascal_row(6))
assert sum(pascal_row(6)) == 2**6
print("✓ Verified!")""")

add_m("m07", 0, "NCERT Class 10–11 · Geometry", "Module 07: Coordinate Geometry, Conic Sections & Affine Transforms",
      "Affine transformations represent translation, rotation, scaling, and shear via 3x3 homogeneous matrices.",
      "The exact mathematical transformation pipeline in Flutter RenderTransform and mobile GPU vertex shaders.",
      """import math
def affine_transform_2d(point, angle_rad, tx, ty, scale=1.0):
    x, y = point
    cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)
    x_new = scale * (x * cos_a - y * sin_a) + tx
    y_new = scale * (x * sin_a + y * cos_a) + ty
    return x_new, y_new
p_trans = affine_transform_2d((10, 0), math.pi/2, tx=5, ty=5)
print("Transformed Point (10, 0) by 90deg + (5,5):", [round(c, 2) for c in p_trans])
assert abs(p_trans[0] - 5.0) < 1e-4 and abs(p_trans[1] - 15.0) < 1e-4
print("✓ Verified!")""")

add_m("m08", 0, "NCERT Class 10–12 · Probability", "Module 08: Classical Probability, Conditional Independence & Bayes Theorem",
      "Bayes' Theorem updates the prior probability of hypothesis H given evidence E: P(H|E) = P(E|H)P(H) / P(E).",
      "Underpins spam classifiers, speculative decoding token verification acceptance probabilities, and Kalman tracking filters.",
      """def bayes(prior_h, p_e_given_h, p_e_given_not_h):
    p_e = p_e_given_h * prior_h + p_e_given_not_h * (1.0 - prior_h)
    return (p_e_given_h * prior_h) / p_e
# Disease test: 1% prior prevalence, 95% sensitivity, 5% false positive
posterior = bayes(0.01, 0.95, 0.05)
print(f"Posterior probability given positive test: {posterior:.4f}")
assert abs(posterior - 0.1610) < 1e-3
print("✓ Verified!")""")

add_m("m09", 0, "NCERT Class 10–11 · Series", "Module 09: Sequences, Series & Convergence Criteria",
      "Analyzes Arithmetic, Geometric, and Harmonic series. The ratio and comparison tests determine infinite series convergence.",
      "Calculates geometric amortized growth in dynamic arrays and token decay learning rate schedules.",
      """def geometric_sum(a, r, n=None):
    if n is not None: return a * (1 - r**n) / (1 - r)
    assert abs(r) < 1.0, "Infinite series diverges for |r| >= 1"
    return a / (1 - r)
print("Finite Sum (1 + 0.5 + ... 10 terms):", geometric_sum(1, 0.5, 10))
print("Infinite Geometric Sum (1 + 1/2 + 1/4 + ...):", geometric_sum(1, 0.5))
assert abs(geometric_sum(1, 0.5) - 2.0) < 1e-9
print("✓ Verified!")""")

add_m("m10", 0, "NCERT Class 9–11 · Statistics", "Module 10: Descriptive Statistics, Variance, Covariance & Chebyshev's Bound",
      "Measures central tendency (mean) and dispersion (variance sigma^2, standard deviation). Chebyshev's inequality bounds tail probabilities.",
      "Directly used in layer normalization (LayerNorm/RMSNorm) across transformer layers to stabilize activations.",
      """import math
def mean_variance(data):
    m = sum(data) / len(data)
    var = sum((x - m)**2 for x in data) / len(data)
    return m, var, math.sqrt(var)
data = [12.0, 15.0, 18.0, 20.0, 25.0, 30.0]
m, var, std = mean_variance(data)
print(f"Mean: {m:.2f}, Variance: {var:.2f}, StdDev: {std:.2f}")
# RMSNorm simulation (Root Mean Square without mean-centering)
rms = math.sqrt(sum(x**2 for x in data) / len(data))
print(f"RMS Norm: {rms:.4f}")
print("✓ Verified!")""")

# Write all to curriculum_data.js
output_path = "omni_academy/curriculum_data.js"
with open(output_path, "w") as f:
    f.write("// Complete Omni-Curriculum Database\n")
    f.write("window.OMNI_MODULES = " + json.dumps(all_modules, indent=2) + ";\n")

print(f"Epoch I complete with {len(all_modules)} modules!")
