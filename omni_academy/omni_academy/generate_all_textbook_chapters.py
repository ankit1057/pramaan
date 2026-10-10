#!/usr/bin/env python3
"""
omni_academy/generate_all_textbook_chapters.py
Generates the 36 missing chapters and wires all 50 chapters in omni_academy/textbook/.
Every chapter is built according to The Builder's Pedagogy:
- The Crime Scene / Origin Hook
- Real-World Mechanical Metaphors
- Permanent Mnemonic Cards
- Systems Tie-Ins (Flutter, Dart, SipLLM, Android JNI, GPU, LLM)
- Live Pyodide WebAssembly Sandbox
"""

import json
import os
import re

TEXTBOOK_DIR = "omni_academy/textbook"
CURRICULUM_DATA = "omni_academy/curriculum_data.js"

CHAPTER_FILENAMES = {
    1: "chapter_01_number_theory.html",
    2: "chapter_02_combinatorics.html",
    3: "chapter_03_gaussian_elimination.html",
    4: "chapter_04_polynomial_rings.html",
    5: "chapter_05_trigonometry.html",
    6: "chapter_06_pascals_triangle.html",
    7: "chapter_07_coordinate_geometry.html",
    8: "chapter_08_classical_probability.html",
    9: "chapter_09_sequences_and_series.html",
    10: "chapter_10_descriptive_statistics.html",
    11: "chapter_11_complex_numbers.html",
    12: "chapter_12_autograd.html",
    13: "chapter_13_integral_calculus.html",
    14: "chapter_14_differential_equations.html",
    15: "chapter_15_quaternions_3d_vectors.html",
    16: "chapter_16_set_theory.html",
    17: "chapter_17_propositional_sat.html",
    18: "chapter_18_graph_theory_matching.html",
    19: "chapter_19_boolean_alu_design.html",
    20: "chapter_20_continuous_probability.html",
    21: "chapter_21_linear_algebra.html",
    22: "chapter_22_eigenvalues_svd.html",
    23: "chapter_23_linear_data_structures.html",
    24: "chapter_24_avl_trees_rotations.html",
    25: "chapter_25_quicksort_randomized.html",
    26: "chapter_26_dynamic_programming.html",
    27: "chapter_27_dijkstra_graph_traversal.html",
    28: "chapter_28_cache_memory_hierarchy.html",
    29: "chapter_29_automata_dfa_regex.html",
    30: "chapter_30_tcp_sliding_window.html",
    31: "chapter_31_os_preemptive_scheduling.html",
    32: "chapter_32_pratt_parser.html",
    33: "chapter_33_concurrency.html",
    34: "chapter_34_distributed_vector_clocks.html",
    35: "chapter_35_rsa_cryptography.html",
    36: "chapter_36_reactive_streams_observer.html",
    37: "chapter_37_android_looper_jni.html",
    38: "chapter_38_ieee754_floating_point.html",
    39: "chapter_39_adam_optimization.html",
    40: "chapter_40_logistic_regression.html",
    41: "chapter_41_reverse_autograd_tape.html",
    42: "chapter_42_residual_layernorm.html",
    43: "chapter_43_attention.html",
    44: "chapter_44_rope.html",
    45: "chapter_45_flash_attention.html",
    46: "chapter_46_quantization.html",
    47: "chapter_47_kv_cache_paging.html",
    48: "chapter_48_speculative_decoding.html",
    49: "chapter_49_shannon_entropy_bpe.html",
    50: "chapter_50_monads_category_theory.html",
}

# Rich pedagogical metadata for the 36 missing chapters
PEDAGOGY_DATA = {
    3: {
        "title": "Systems of Equations & Gaussian Elimination: The 3D Mesh Physics Collapse",
        "badge_color": "var(--cyan)",
        "bullets": [
            "Why pivoting prevents 3D models from collapsing into 2D pancakes in physics engines.",
            "The Staircase of Elimination: Transforming messy linear systems into upper-triangular form.",
            "Back-substitution: Solving from the bottom up in O(N^2) time.",
            "Permanent Mnemonic: The P.I.V.O.T. Protocol.",
            "Live Pyodide Lab: Solve a 3x3 augmented matrix with partial row swapping."
        ],
        "hook_title": "1. The Crime Scene: The Collapsing Video Game Mesh",
        "hook_text": """Imagine you are running a 3D ragdoll physics simulation in a Flutter or C++ game engine.
Your character drops from a cliff. The physics engine sets up a system of linear equations matching the forces on each limb.
Suddenly, one limb stretches across the screen and the entire character collapses into a flat zero-volume polygon.
Why? Because the solver hit a diagonal element equal to 0.0, dividing by zero and destroying the vertex coordinates.
Gaussian elimination with partial row pivoting was invented specifically to prevent this catastrophe: always swap the largest available number into the pivot position before dividing!""",
        "analogy_label": "💡 Real-World Metaphor: The Escalator of Solvers",
        "analogy_text": """Think of a system of 3 equations with 3 unknowns like a 3-step escalator:
• Top step has 3 variables (x, y, z).
• Middle step has 2 variables (y, z).
• Bottom step has only 1 variable (z).
Once you find z on the bottom step, you climb backwards up the escalator, plugging z in to find y, then plugging y and z in to find x. That is all Gaussian Elimination is: building a staircase, then climbing it backwards!""",
        "mnemonic_title": "The P.I.V.O.T. Protocol",
        "mnemonic_rule": "Pick largest absolute value · Invert/swap row order · Vacuum column beneath · Operate downwards · Traverse upwards with back-substitution.",
        "mnemonic_desc": "Never divide by the current diagonal without checking if a larger number exists beneath it. Partial pivoting stabilizes floating-point error from exploding into NaNs.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Gaussian elimination powers real-time inverse kinematics in 3D gaming, constrained spring-damper solving in physics engines, and electrical network state estimation in IoT control systems."""
    },
    4: {
        "title": "Polynomial Rings & Vieta's Formulas: The Audio Filter Screech",
        "badge_color": "var(--amber)",
        "bullets": [
            "How polynomial roots determine whether a digital audio filter sounds crisp or explodes into deafening feedback.",
            "Vieta's Formulas: The symmetric secret connecting coefficients directly to sums and products of roots.",
            "The Mirror Lake of Complex Conjugates: Why real polynomial complex roots always occur in pairs.",
            "Permanent Mnemonic: V.I.E.T.A.",
            "Live Pyodide Lab: Solve quadratic roots and verify Vieta's symmetric formulas."
        ],
        "hook_title": "1. The Crime Scene: The Deafening Microphone Feedback",
        "hook_text": """You plug a microphone into a digital equalizer app. You adjust the bass slider.
Suddenly, a deafening 4,000 Hz screech blasts through the speakers and crashes the audio thread.
In digital signal processing, every digital filter is represented by a polynomial ratio H(z) = B(z) / A(z).
The roots of the denominator polynomial are the filter's 'poles'. If a single root lands outside the unit circle (|r| > 1), the system has positive feedback and explodes into infinite energy! Vieta's formulas let audio engineers inspect the stability of filter poles instantly from the polynomial coefficients without having to find the roots.""",
        "analogy_label": "💡 Real-World Metaphor: The Mirror Lake of Complex Numbers",
        "analogy_text": """Imagine standing on the bank of a perfectly still lake. Your reflection in the water is your complex conjugate.
Whenever a real-world physical system (like a guitar string or Flutter spring animation) creates complex roots, they MUST mirror each other: if 3 + 4i is a root, 3 - 4i is guaranteed to be a root. The imaginary numbers cancel out in the sums and products, leaving purely real physical coefficients!""",
        "mnemonic_title": "The V.I.E.T.A. Law",
        "mnemonic_rule": "Variable sums match negative second coefficient · Interleaved products match constant · Even/odd alternating signs · Tested against the discriminant · Audio and UI springs stabilized.",
        "mnemonic_desc": "For a quadratic ax^2 + bx + c = 0, root sum is always -b/a, and root product is always c/a. This symmetry scales to polynomials of arbitrary degree n.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Powers Flutter's SpringSimulation physics curve, audio DSP biquad pole/zero filter design, and control system transfer function stability."""
    },
    6: {
        "title": "Combinatorics & Pascal's Simplex: The Search Space Explosion",
        "badge_color": "var(--emerald)",
        "bullets": [
            "Why combinatorics is the arithmetic of choice, memory allocation, and permutations.",
            "Pascal's Triangle: The Plinko pegboard that generates binomial coefficients without factorials.",
            "The Factorial Explosion: Why testing all permutations crashes brute-force algorithms.",
            "Permanent Mnemonic: P.A.S.C.A.L.",
            "Live Pyodide Lab: Generate Pascal's triangle and calculate binomial expansions."
        ],
        "hook_title": "1. The Crime Scene: The Brute Force Password Cracker that Needed 400 Years",
        "hook_text": """A junior engineer writes a test script to test all possible combinations of a 10-field checkout form.
Each field has 4 options. The engineer writes a nested loop and runs the test.
The server runs out of memory and hangs. Why? 4^10 is 1,048,576 combinations. If there were 20 fields, it would be 1,099,511,627,776 combinations!
Understanding combinatorics is knowing when an algorithm is feasible and when the state space explodes exponentially into mathematical impossibility.""",
        "analogy_label": "💡 Real-World Metaphor: The Plinko Pegboard",
        "analogy_text": """Drop a marble into a Plinko pegboard. At each peg, the marble must choose to bounce left or right.
At row N, there are 2^N total possible paths. The number of paths that land in bucket k is exactly Pascal's triangle entry nCr! Nature naturally routes probability through Pascal's triangle.""",
        "mnemonic_title": "The P.A.S.C.A.L. Pegboard",
        "mnemonic_rule": "Paths sum from two parents above · Always symmetric left-to-right · Sum of row equals 2^N · Combinations nCr without multiplying factorials · Allocations and mutation testing.",
        "mnemonic_desc": "Instead of computing massive factorials that overflow 64-bit integers, compute combinations additively using Pascal's recurrence: C(n, k) = C(n-1, k-1) + C(n-1, k).",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Used in generating test mutation suites, beam search candidate exploration in language models, and calculating memory partition layouts."""
    },
    7: {
        "title": "Coordinate Geometry & Affine Transforms: The Disappearing Widget",
        "badge_color": "var(--cyan)",
        "bullets": [
            "Why translating, rotating, and scaling 2D points requires a 3x3 homogeneous matrix.",
            "The Magic Third Dimension: Adding a dummy 1.0 coordinate to turn translation into linear multiplication.",
            "The Invertibility Guarantee: How Flutter translates touch events back into widget coordinates.",
            "Permanent Mnemonic: A.F.F.I.N.E.",
            "Live Pyodide Lab: Apply a 2D affine matrix transformation with rotation and translation."
        ],
        "hook_title": "1. The Crime Scene: The Phantom Button Click in Flutter",
        "hook_text": """You rotate a Flutter card by 45 degrees and translate it 100 pixels down.
The UI looks gorgeous. But when users tap the button, nothing happens. When they tap the empty space 100 pixels above the button, the button clicks!
Why? Because the rendering engine applied the matrix forward, but the hit-testing system failed to invert the matrix!
Every visual transformation in Flutter, Skia, Impeller, and GPU vertex shaders is an Affine Transform represented by a matrix. When touch events occur, the engine multiplies the touch coordinate by the inverse matrix to find the touched widget!""",
        "analogy_label": "💡 Real-World Metaphor: The Overhead Projector Sheet",
        "analogy_text": """Imagine drawing a house on a transparent plastic sheet on an overhead projector:
• You can slide the sheet (Translation).
• You can spin the sheet (Rotation).
• You can pull the edges evenly (Scaling) or slant it (Shearing).
Notice what NEVER happens: straight lines never curve, and parallel lines never cross. That is the definition of an Affine Transform: preserving straight lines and parallelism!""",
        "mnemonic_title": "The A.F.F.I.N.E. Matrix",
        "mnemonic_rule": "Add third 1.0 coordinate for translation · Fixed origin rotations · Forward matrix vector multiplication · Invert for hit-testing · No curving of straight grid lines · Every GPU vertex pipeline.",
        "mnemonic_desc": "2D translation is non-linear in 2D, but becomes pure linear matrix multiplication when embedded into 3D homogeneous coordinates [x, y, 1]^T.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The exact mathematical pipeline behind Flutter's RenderTransform, Matrix4, mobile GPU vertex shaders, and pinch-to-zoom gesture decoders."""
    },
    8: {
        "title": "Classical Probability & Bayes' Theorem: The False Positive Medical Panic",
        "badge_color": "var(--rose)",
        "bullets": [
            "The Base Rate Fallacy: Why a 99% accurate test on a rare disease only means a 9% chance you are sick.",
            "Bayes' Formula: Updating prior beliefs in the light of fresh evidence.",
            "Speculative Decoding Connection: How language models accept or reject draft tokens probabilistically.",
            "Permanent Mnemonic: B.A.Y.E.S.",
            "Live Pyodide Lab: Compute Bayesian posterior probabilities given likelihood and priors."
        ],
        "hook_title": "1. The Crime Scene: The False Positive Health Panic",
        "hook_text": """A patient takes a diagnostic test for a rare disease affecting 1 in 1,000 people.
The lab reports: 'The test is 99% accurate. Your result is POSITIVE.'
The patient panics, assuming there is a 99% chance they have the disease.
The true probability? Less than 9%!
Why? Out of 100,000 people, only 100 actually have the disease (99 test positive). But out of the 99,900 healthy people, a 1% false positive rate creates 999 false alarms!
So out of 1,098 total positive tests, only 99 are real (99 / 1,098 ≈ 9%).
Ignoring the prior base rate is the most common cognitive failure in humans and machine learning models alike.""",
        "analogy_label": "💡 Real-World Metaphor: The Detective's Scale of Evidence",
        "analogy_text": """Think of Bayes' Theorem like an antique scale with two pans:
• The Prior is a heavy iron weight placed on one pan before the trial begins (how common is this event normally?).
• The Evidence is a pebble placed on the other pan.
A single pebble of evidence cannot lift a 100-pound iron prior weight. It takes massive, overwhelming evidence to overturn a rare prior!""",
        "mnemonic_title": "The B.A.Y.E.S. Scale",
        "mnemonic_rule": "Base rate prior matters most · Adjust when evidence arrives · Yield normalized posterior · Evidence denominator sums all paths · Speculative decoding acceptance probability.",
        "mnemonic_desc": "P(Hypothesis | Evidence) = P(Evidence | Hypothesis) * P(Hypothesis) / P(Evidence). Always multiply the likelihood by the prior before believing an alarm.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Powers speculative decoding verification in high-throughput LLM engines, spam classification, and Kalman filter sensor fusion in Android location services."""
    },
    9: {
        "title": "Sequences, Series & Convergence: The Infinite Coffee Break",
        "badge_color": "var(--indigo)",
        "bullets": [
            "Why an infinite number of actions can sum to a finite, bounded quantity.",
            "Geometric Series: The engine behind vector doubling amortized O(1) performance.",
            "The Ratio Test: How to prove whether an algorithm will terminate or run forever.",
            "Permanent Mnemonic: S.E.R.I.E.S.",
            "Live Pyodide Lab: Compute finite and infinite geometric series sums."
        ],
        "hook_title": "1. The Crime Scene: The Infinite Memory Allocation Paradox",
        "hook_text": """A developer looks at a dynamic array that doubles its capacity every time it fills up: 1, 2, 4, 8, 16, 32...
The developer worries: 'Won't copying all elements every time make appending take infinite time?'
No! Because 1/2 + 1/4 + 1/8 + 1/16 + ... = 1!
Even though you double the array infinitely many times, the total number of copied elements across all appends never exceeds twice the number of items!
Geometric convergence is the mathematical reason why `List.add()` in Dart and `std::vector::push_back()` in C++ have guaranteed O(1) amortized insertion time.""",
        "analogy_label": "💡 Real-World Metaphor: The Bouncing Tennis Ball",
        "analogy_text": """Drop a tennis ball from 1 meter. It bounces to 0.5m, then 0.25m, then 0.125m...
The ball bounces an infinite number of times before coming to rest.
Yet the total distance it travels is exactly 1 + 2*(0.5 + 0.25 + 0.125...) = 3 meters, and it stops in less than 3 seconds! Infinite steps can have a finite, peaceful sum.""",
        "mnemonic_title": "The S.E.R.I.E.S. Bound",
        "mnemonic_rule": "Step ratio r must be strictly < 1 · Exponential growth breaks budgets · Running sum converges to a / (1 - r) · Infinite terms with finite bounds · Essential for dynamic array doubling amortized cost.",
        "mnemonic_desc": "If the ratio between consecutive terms |r| < 1, the sum of infinite terms is strictly bounded by a / (1 - r). If r >= 1, the system diverges and crashes memory.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Proves O(1) amortized push in Dart Lists and C++ vectors; powers cosine learning rate decay schedules in neural network training."""
    },
    10: {
        "title": "Descriptive Statistics & Chebyshev's Bound: The 3-Sigma Cloud Outage",
        "badge_color": "var(--emerald)",
        "bullets": [
            "Why the 'Average' is a dangerous lie that hides system-destroying outlier spikes.",
            "Variance and Standard Deviation: Measuring the spread and volatility of memory and latency.",
            "Chebyshev's Inequality: A mathematical guarantee on tail latency for ANY distribution.",
            "Permanent Mnemonic: C.H.E.B.Y.",
            "Live Pyodide Lab: Compute mean, variance, standard deviation, and Chebyshev tail bounds."
        ],
        "hook_title": "1. The Crime Scene: The Cloud Outage with a 'Green' Average Latency",
        "hook_text": """Your dashboard shows: 'Average API response time: 42 ms (Healthy).'
Yet angry customers are flooding customer support saying the app times out and crashes.
You inspect the raw logs: 99 requests took 10 ms, but 1 request took 35,000 ms (35 seconds)!
The arithmetic mean was 42 ms, completely hiding the fact that 1% of your users were experiencing catastrophic lockups.
In computer systems, you never trust the mean. You measure variance, standard deviation, and tail percentiles (p99).""",
        "analogy_label": "💡 Real-World Metaphor: The Rubber Band Around the Mean",
        "analogy_text": """Think of variance like a rubber band stretched between your data points and their average.
If all numbers are clustered close together, the rubber band is relaxed (low variance).
If even a single rogue number flies off to infinity, the rubber band stretches tight, generating massive variance tension that alerts you to instability.""",
        "mnemonic_title": "The C.H.E.B.Y. Outlier Guard",
        "mnemonic_rule": "Center around the mean mu · Height scaled by standard deviation sigma · Energy bounded by 1/k^2 probability · Baseline for LayerNorm and RMSNorm · Yielding guaranteed bounds on arbitrary distributions.",
        "mnemonic_desc": "No matter what shape the data distribution has, the probability of being more than k standard deviations away from the mean is strictly less than 1/k^2. At 3-sigma, at most 11% can be outliers.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The direct mathematical formula behind LayerNorm and RMSNorm layers in Transformers, and latency percentile monitoring in production APIs."""
    },
    13: {
        "title": "Integral Calculus & Simpson's Rule: The Battery Drain Mystery",
        "badge_color": "var(--cyan)",
        "bullets": [
            "Why numerical integration computes total energy, trajectory distance, and area under curves.",
            "The Failure of Flat Rectangles: Why Riemann sums bleed massive errors at curved boundaries.",
            "Simpson's 1/3 Rule: Fitting quadratic parabolas across 3 points for O(h^4) precision.",
            "Permanent Mnemonic: S.I.M.P.S.O.N.",
            "Live Pyodide Lab: Compute area under a non-linear curve using Simpson's Rule."
        ],
        "hook_title": "1. The Crime Scene: The Phone that Died at 40% Battery",
        "hook_text": """Your mobile operating system estimates battery life by integrating power draw over time: Total Energy = Integral of P(t) dt.
A simple rectangular integration algorithm sampled current draw every 10 seconds.
When the CPU throttled up for 500ms bursts to render 120 FPS frames, the rectangular sampler completely missed the peaks.
The operating system told the user they had 40% battery remaining, but the device suddenly shut off.
Simpson's Rule fits parabolic arcs across sample points, capturing non-linear spikes with 100x greater accuracy using the exact same number of samples!""",
        "analogy_label": "💡 Real-World Metaphor: Fitting Arches Under a Curved Bridge",
        "analogy_text": """Imagine measuring the stone area of an arched Roman bridge:
• If you build rectangular wooden towers, you leave massive triangular gaps between the wood and the stone arch (Riemann sum error).
• If you lay flexible parabolic stone arches that hug the bridge's curve across every 3 points, you capture the curve almost perfectly with zero wasted gaps!""",
        "mnemonic_title": "The S.I.M.P.S.O.N. Parabola",
        "mnemonic_rule": "Stitch parabola across 3 points · Intervals split evenly into pairs · Multiply coefficients by 1-4-2-4-1 · Parabolic fit yields O(h^4) precision · Signal power and physics integration.",
        "mnemonic_desc": "By replacing linear line segments with quadratic polynomials, error drops from O(h^2) to O(h^4), providing research-grade precision with minimal CPU cycles.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Used in battery consumption profiling, audio DSP signal power calculations, and physics trajectory integration in mobile game engines."""
    },
    15: {
        "title": "3D Vector Geometry & Quaternions: The Apollo 11 Gimbal Lock",
        "badge_color": "var(--rose)",
        "bullets": [
            "Why Euler angles (pitch, yaw, roll) freeze and lose a degree of freedom (Gimbal Lock).",
            "Quaternions: 4-dimensional hyper-complex numbers that rotate 3D space smoothly.",
            "SLERP (Spherical Linear Interpolation): Rotating objects at constant angular velocity.",
            "Permanent Mnemonic: Q.U.A.T.",
            "Live Pyodide Lab: Multiply quaternions and rotate a 3D vector without matrices."
        ],
        "hook_title": "1. The Crime Scene: Apollo 11's Gimbal Lock Warning",
        "hook_text": """During Apollo 11's lunar descent, astronaut Mike Collins received a critical alarm: 'GIMBAL LOCK'.
The spacecraft's inertial platform used 3 mechanical rotating rings (Euler gimbals).
When two of the three rotation axes aligned into the same plane, the system lost an entire dimension of freedom!
If the spacecraft rotated even slightly in that locked axis, the navigation platform would tumble uncontrollably into space.
Quaternions eliminate Gimbal Lock permanently by representing 3D rotations as points on a 4-dimensional sphere, ensuring smooth, singularity-free rotations in all directions!""",
        "analogy_label": "💡 Real-World Metaphor: Tumbling Across a 4D Basketball",
        "analogy_text": """Instead of turning 3 separate steering wheels for Yaw, Pitch, and Roll, imagine rolling a basketball on a flat table:
You can roll the ball in ANY direction smoothly without ever getting stuck. A quaternion q = w + xi + yj + zk is just the 4D coordinate of the basketball's rotation!""",
        "mnemonic_title": "The Q.U.A.T. Hyper-Sphere",
        "mnemonic_rule": "Quarter turn hyper-complex units i^2 = j^2 = k^2 = ijk = -1 · Unit length ||q|| = 1 · Avoids all gimbal lock singularity · Tomographic SLERP spherical interpolation for smooth animations.",
        "mnemonic_desc": "Unit quaternions represent a rotation by angle theta around axis u as q = [cos(theta/2), u * sin(theta/2)]. Multiplying quaternions composes rotations in 16 multiplications instead of 27.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The standard rotation representation in mobile AR (ARKit/ARCore), 3D Flutter and Unity game engines, and drone flight navigation controllers."""
    },
    16: {
        "title": "Set Theory & Equivalence Partitions: The Split-Brain Network",
        "badge_color": "var(--amber)",
        "bullets": [
            "How equivalence relations (Reflexive, Symmetric, Transitive) carve universes into non-overlapping islands.",
            "Partitions: Dividing database records and memory caches without overlaps.",
            "Disjoint-Set Union-Find: Merging groups in near O(1) time via path compression.",
            "Permanent Mnemonic: P.A.R.T.",
            "Live Pyodide Lab: Implement Disjoint-Set Union-Find with path compression."
        ],
        "hook_title": "1. The Crime Scene: The Split-Brain Cluster Disaster",
        "hook_text": """A network fiber cable snaps between data center East and data center West.
Both data centers assume the other is dead. Both promote their local database to master.
Users in New York buy product X; users in London buy the exact same product X.
When the network reconnects, the database state is corrupt beyond repair.
Set partitions define the mathematical boundary of identity: every entity must belong to exactly ONE partition. The moment two partitions share an element or a partition splits unchecked, consistency collapses!""",
        "analogy_label": "💡 Real-World Metaphor: The Country Club Badges",
        "analogy_text": """Imagine a private club where every guest receives a colored badge (Red, Blue, or Green):
• Every guest has exactly one badge color.
• Guests with the same badge color can access the same private room (Equivalence).
• No guest can hold two badge colors at once (Disjoint partitions).
The Union-Find data structure is just an algorithm that merges two badges into one whenever two guests shake hands!""",
        "mnemonic_title": "The P.A.R.T. Partition Law",
        "mnemonic_rule": "Pairwise disjoint subsets · All elements accounted for · Reflexive-Symmetric-Transitive equivalence · Tree-based Disjoint-Set Union-Find with path compression.",
        "mnemonic_desc": "An equivalence relation partitions a set into mutually exclusive equivalence classes. Union-Find tracks these partitions with inverse Ackermann alpha(n) complexity (effectively constant time).",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Used in Kruskal's minimum spanning tree algorithm, database shard partition keys, and network connected-component discovery."""
    },
    17: {
        "title": "Propositional SAT & Truth Tables: The Package Manager Dependency Hell",
        "badge_color": "var(--cyan)",
        "bullets": [
            "Why resolving software package dependencies is mathematically NP-complete.",
            "Boolean Conjunctive Normal Form (CNF): Expressing complex rules as ANDs of ORs.",
            "The DPLL Algorithm: How SAT solvers explore millions of possibilities in milliseconds.",
            "Permanent Mnemonic: D.P.L.L.",
            "Live Pyodide Lab: Solve a 3-variable Boolean CNF formula using DPLL backtracking."
        ],
        "hook_title": "1. The Crime Scene: The 4-Hour 'pub get' Dependency Freeze",
        "hook_text": """You type `flutter pub get` after adding a new package to your app.
The terminal hangs: `Resolving dependencies...` for 10 minutes, then outputs:
`Because package A depends on B >=2.0.0 and package C depends on B <2.0.0, version solving failed.`
Why is package resolution so hard? Because finding a compatible set of library versions is mathematically equivalent to the Boolean Satisfiability Problem (SAT)—the foundational NP-complete problem!
Package managers like Dart's Pub, Debian's APT, and Rust's Cargo use industrial SAT solvers under the hood to find valid version combinations.""",
        "analogy_label": "💡 Real-World Metaphor: The Detective's Suspect Clue Board",
        "analogy_text": """Imagine a detective trying to deduce the killer from 5 clues:
• If the butler is guilty, the maid must be innocent.
• Either the chauffeur or the gardener was in the garden.
A SAT solver is an automated detective: it picks one suspect (branching), immediately crosses off everyone whose alibi is proven (unit propagation), and backtracks the second a contradiction appears!""",
        "mnemonic_title": "The D.P.L.L. Solver",
        "mnemonic_rule": "Decide truth value by branching · Propagate unit clauses immediately · Learn and prune dead-end branches · Linear CNF representation · Solves package dependency and formal verification.",
        "mnemonic_desc": "DPLL (Davis-Putnam-Logemann-Loveland) recursively eliminates clauses: if a clause has only 1 unassigned literal, that literal's value is forced (Unit Propagation).",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The core algorithm inside package version resolvers (pub, cargo, apt), automated test verification engines, and hardware circuit verification."""
    },
    18: {
        "title": "Graph Theory & Bipartite Matching: The Ride-Share Dispatch",
        "badge_color": "var(--indigo)",
        "bullets": [
            "Bipartite Graphs: Modeling systems with two disjoint groups (Drivers vs Riders).",
            "Augmenting Paths & The Hopcroft-Karp Algorithm: Maximizing matches efficiently.",
            "König's Theorem: The dual relationship between maximum matching and minimum vertex cover.",
            "Permanent Mnemonic: M.A.T.C.H.",
            "Live Pyodide Lab: Find maximum bipartite matching using augmenting DFS paths."
        ],
        "hook_title": "1. The Crime Scene: The Rush Hour Ride-Share Gridlock",
        "hook_text": """It is 6:00 PM on a Friday. 100 passengers open the ride-share app in downtown Manhattan.
50 drivers are available. A naive greedy algorithm matches the first passenger to the closest driver.
Result: 35 matches made, 15 drivers left unassigned because they are too far from the remaining passengers.
A bipartite matching algorithm finds the global optimum: by matching passenger 1 to driver 2, passenger 2 can match driver 3, unlocking 48 total rides instead of 35!""",
        "analogy_label": "💡 Real-World Metaphor: The Dance Floor Partner Shuffle",
        "analogy_text": """Imagine boys on the left of a hall, girls on the right:
If Alice wants Bob, and Bob is taken by Carol, but Carol would also happily dance with Dave (who is currently dancing with no one),
we shuffle: Carol switches to Dave, freeing up Bob to dance with Alice!
That chain of shuffles is an Augmenting Path: flipping matched and unmatched edges to increase total pairs by 1!""",
        "mnemonic_title": "The M.A.T.C.H. Shuffler",
        "mnemonic_rule": "Max flow through augmenting paths · Alternating paths flip matched and unmatched edges · Two disjoint vertex sets · Cut duality by König's theorem · Hardware register allocation in compilers.",
        "mnemonic_desc": "A matching is maximum if and only if there are no augmenting paths. Finding an augmenting path and flipping edges increases matching cardinality by 1.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Compiler register allocation (matching virtual variables to physical CPU registers), cloud task dispatcher load balancing, and ride-sharing routing engines."""
    },
    19: {
        "title": "Boolean Algebra & ALU Design: Building Math Out of Switches",
        "badge_color": "var(--rose)",
        "bullets": [
            "How physical transistors build logic gates, and logic gates build arithmetic.",
            "The Half-Adder and Full-Adder: Adding binary bits with Carry-in and Carry-out.",
            "Two's Complement: Why subtracting numbers is just adding inverted bits plus one.",
            "Permanent Mnemonic: A.L.U.",
            "Live Pyodide Lab: Simulate an 8-bit ripple-carry adder using pure bitwise gates."
        ],
        "hook_title": "1. The Crime Scene: The CPU That Could Not Subtract",
        "hook_text": """In early computing, engineers had to build two completely separate hardware circuits: one circuit to add numbers, and a second circuit with reverse wiring to subtract numbers.
This doubled chip area, doubled power consumption, and created constant timing bugs.
Then came Two's Complement: by inverting all bits and adding 1, subtraction A - B becomes pure addition: A + (~B + 1)!
A single hardware adder circuit can perform BOTH addition and subtraction with a single XOR control wire!""",
        "analogy_label": "💡 Real-World Metaphor: The Water Valve Calculator",
        "analogy_text": """Imagine building a computer out of water pipes:
• An AND gate is two valves placed in line on the same pipe (water flows only if BOTH valves open).
• An OR gate is two valves on parallel pipes (water flows if EITHER valve opens).
• An XOR gate is a differential piston that opens if one valve is open, but slams shut if both valves open together.
Chain two valves together, and you have an adder that computes sums and carries entirely with water pressure!""",
        "mnemonic_title": "The A.L.U. Silicon Core",
        "mnemonic_rule": "Arithmetic from logical switches · Logic gates built from NAND primitives · Unit adders chain carry-bits · Inverts signals for subtraction · Powers the physical CPU silicon execution core.",
        "mnemonic_desc": "Sum = A XOR B XOR Cin. Carry_out = (A AND B) OR (Cin AND (A XOR B)). Every computer on Earth computes numbers using this exact silicon equation.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The physical transistor architecture inside CPU/GPU execution cores, SIMD integer addition in ARM NEON assembly, and low-level bitwise operations in Dart/C++."""
    },
    20: {
        "title": "Continuous Probability & The Box-Muller Transform: Generating Natural Noise",
        "badge_color": "var(--emerald)",
        "bullets": [
            "Why computers cannot generate natural Gaussian (normal) random numbers directly.",
            "The Box-Muller Transform: Turning two flat uniform dice rolls into a smooth 2D bell curve.",
            "Neural Weight Initialization: Why deep networks need Gaussian weights to avoid dying.",
            "Permanent Mnemonic: B.O.X.M.",
            "Live Pyodide Lab: Transform uniform random numbers into normal distributions via Box-Muller."
        ],
        "hook_title": "1. The Crime Scene: The Exploding Gradients of Uniform Initialization",
        "hook_text": """A machine learning engineer initializes a 50-layer deep neural network with uniform random numbers between -1.0 and +1.0.
After one training step, all activations turn to NaNs. The network is brain-dead.
Why? Uniform numbers have flat distribution variance that accumulates exponentially across layers.
Deep networks require Gaussian (normal) distributions with zero mean and carefully calibrated standard deviation (He / Xavier init). But computer chips only have random generators that return uniform numbers between 0 and 1.
How do you transform a flat rectangle of random numbers into a smooth Gaussian bell curve? The Box-Muller transform!""",
        "analogy_label": "💡 Real-World Metaphor: Darts on a Spinning Dartboard",
        "analogy_text": """Imagine throwing darts at a circular spinning target:
• You pick a random angle from 0 to 360 degrees (Uniform 1).
• You pick a random radial distance from the center (Uniform 2).
Projecting where the darts land onto the horizontal and vertical axes creates two completely independent, perfect Gaussian normal bell curves!""",
        "mnemonic_title": "The B.O.X.M. Bell Curve",
        "mnemonic_rule": "Base uniform random numbers U1, U2 · Orbit angle 2*pi*U2 · eXponent radius sqrt(-2*ln(U1)) · Multiplies out into two independent Gaussians · Powers neural network weight initialization and diffusion denoising.",
        "mnemonic_desc": "Z0 = sqrt(-2 ln U1) * cos(2 pi U2), Z1 = sqrt(-2 ln U1) * sin(2 pi U2). Turns cheap pseudo-random uniform bytes into research-grade Gaussian samples.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Weight initialization in deep neural networks, diffusion model image generation denoising loops, and Monte Carlo physical shaders."""
    },
    22: {
        "title": "Eigenvalues & SVD/PCA: The Tacoma Narrows Bridge Collapse",
        "badge_color": "var(--cyan)",
        "bullets": [
            "Eigenvalues and Eigenvectors: The invariant directions that never rotate under transformation.",
            "Singular Value Decomposition (SVD): Factoring any matrix into Spin, Scale, and Direct.",
            "Low-Rank Adaptation (LoRA): How two skinny matrices replace 16,000,000 LLM weights.",
            "Permanent Mnemonic: E.I.G.E.N.",
            "Live Pyodide Lab: Compute SVD power iteration and reconstruct low-rank matrix approximations."
        ],
        "hook_title": "1. The Crime Scene: The Tacoma Narrows Bridge Catastrophe",
        "hook_text": """On November 7, 1940, a gentle 42 mph wind blew across the Tacoma Narrows suspension bridge in Washington.
Instead of swaying slightly, the bridge began violently twisting like a ribbon, lifting 28 feet in the air before tearing into the Puget Sound.
What destroyed the bridge? The wind matched the natural resonant eigenvalue frequency of the bridge's structural matrix!
In linear algebra, every transformation matrix has special directions (eigenvectors) where forces amplify purely along the line without dispersing. Understanding eigenvalues is knowing where a system naturally resonates, compresses, or breaks.""",
        "analogy_label": "💡 Real-World Metaphor: The Unbending Arrows on a Rubber Pizza",
        "analogy_text": """Imagine drawing hundreds of arrows on an unbaked pizza dough.
You grab the dough and stretch it diagonally:
Almost every arrow twists and changes its angle.
Except for TWO special arrows: one pointing along the exact direction you are pulling, and one perpendicular to it. Those two arrows don't turn at all—they only stretch longer! Those are the Eigenvectors, and their stretch factors are the Eigenvalues!""",
        "mnemonic_title": "The E.I.G.E.N. Stretch",
        "mnemonic_rule": "Equation A*v = lambda*v · Invariant direction arrows · Greatest stretch corresponds to largest eigenvalue · Essential for PCA dimensional compression · Powers LoRA fine-tuning by finding principal ranks.",
        "mnemonic_desc": "SVD decomposes any matrix A = U * Sigma * V^T. Truncating to the top k singular values gives the mathematically optimal rank-k approximation (Eckart-Young-Mirsky Theorem).",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Powers LoRA fine-tuning in LLMs, vector database embedding compression in search engines, and facial recognition PCA decompositions."""
    },
    23: {
        "title": "Linear Data Structures: Vector Doubling & Circular Ring Buffers",
        "badge_color": "var(--indigo)",
        "bullets": [
            "Why dynamic array capacity doubling guarantees O(1) amortized insertion.",
            "The Memory Allocation Spike: Why reallocating memory one item at a time destroys CPU caches.",
            "Circular Ring Buffers: Lock-free FIFO streaming over fixed RAM budgets.",
            "Permanent Mnemonic: B.U.F.F.E.R.",
            "Live Pyodide Lab: Simulate a power-of-two circular ring buffer with bitwise masking."
        ],
        "hook_title": "1. The Crime Scene: The 45-Second Append Freeze",
        "hook_text": """A junior engineer builds a high-frequency trading logger that appends incoming trade prices to an array.
Every time a price arrives, the code calls `realloc(buffer, size + 1)`.
For the first 1,000 items, the code is lightning fast. At 100,000 items, adding a single trade takes 20 milliseconds! At 1,000,000 items, the app freezes for 45 seconds!
Why? Because every append forces the operating system to find a new contiguous block of memory and copy all previous 999,999 items over!
By doubling capacity (1 -> 2 -> 4 -> 8 -> 16...), the total copies across 1,000,000 items is less than 2,000,000, reducing append time from O(N^2) to O(1) amortized!""",
        "analogy_label": "💡 Real-World Metaphor: The Revolving Sushi Bar Conveyor",
        "analogy_text": """Imagine a revolving sushi bar with 8 seats arranged in a circle:
The chef places plates at the Head index; customers eat plates at the Tail index.
When the chef reaches seat 7, the next plate goes to seat 0!
Nobody ever has to rebuild the restaurant or move the conveyor belt. Memory is fixed, allocations are zero, and data flows smoothly in a continuous ring!""",
        "mnemonic_title": "The B.U.F.F.E.R. Ring",
        "mnemonic_rule": "Bitwise mask modulo for power-of-two rings · Uniform O(1) amortized push · Fast lock-free circular queue streaming · Fixed RAM footprint never triggers GC · Essential for high-fps audio and LLM token queues.",
        "mnemonic_desc": "When buffer size is a power of two (e.g. 1024), index wrapping is computed with a single CPU instruction: next_index = (index + 1) & (SIZE - 1), avoiding slow division instructions.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Powers Dart's List capacity growth, SipLLM's memory-budgeted layer streaming ring buffers, and audio engine DMA ring buffers."""
    },
    24: {
        "title": "Trees & Hierarchies: BST & AVL Self-Balancing Rotations",
        "badge_color": "var(--emerald)",
        "bullets": [
            "Why naive Binary Search Trees degenerate into slow O(n) linked lists.",
            "The Balance Factor: Maintaining height difference |h_L - h_R| <= 1.",
            "Tree Rotations: Left, Right, Left-Right, and Right-Left rebalancing maneuvers.",
            "Permanent Mnemonic: R.O.T.A.T.E.",
            "Live Pyodide Lab: Insert nodes into an AVL tree and verify self-balancing tree rotations."
        ],
        "hook_title": "1. The Crime Scene: The Database Index That Crawled Like a Snail",
        "hook_text": """A developer creates a binary search tree to index user IDs.
Users sign up sequentially: ID 1, then ID 2, then ID 3, up to ID 100,000.
The developer expects lightning-fast O(log n) lookups (around 17 operations).
Instead, searching for user 100,000 takes 100,000 operations and crashes the call stack with a StackOverflowException!
Why? Inserting sorted items into a naive BST creates a completely unbalanced tree that is literally just a straight linked list!
AVL trees automatically detect when one branch grows taller than its sibling and execute instant rotations to keep the tree bushy and balanced.""",
        "analogy_label": "💡 Real-World Metaphor: The Tightrope Acrobat's Pole",
        "analogy_text": """Imagine walking a tightrope carrying a long balance pole:
If you lean too far to the left, you tilt the pole to the right to bring your center of mass back to the middle.
An AVL tree does the exact same thing: the moment the left branch is 2 levels deeper than the right branch, the parent node slides down to become a child, pulling the middle node up to become the new root!""",
        "mnemonic_title": "The R.O.T.A.T.E. Acrobat",
        "mnemonic_rule": "Rebalance when height difference |h_L - h_R| > 1 · One single rotation for straight zig-zig · Two double rotations for bent zig-zag · Always guaranteed O(log n) worst-case · Tree indexing in SQLite and filesystem directories.",
        "mnemonic_desc": "Maintains strict O(log n) search, insertion, and deletion times in all cases. Every node stores its subtree height to calculate balance factors in O(1) time.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The direct foundation of B-tree database indexing in SQLite and Postgres, Linux kernel virtual memory trees, and in-memory trading order books."""
    },
    25: {
        "title": "Sorting Algorithms: QuickSort with Randomized Pivoting",
        "badge_color": "var(--amber)",
        "bullets": [
            "Why QuickSort is the undisputed king of real-world sorting in standard libraries.",
            "The Quicksort Denial-of-Service Vulnerability: Exploiting fixed pivots with sorted arrays.",
            "Randomized & Median-of-Three Pivoting: Guaranteeing O(n log n) average performance.",
            "Permanent Mnemonic: Q.U.I.C.K.",
            "Live Pyodide Lab: Run randomized in-place QuickSort with partition step verification."
        ],
        "hook_title": "1. The Crime Scene: The Web Server DoS via Sorted Arrays",
        "hook_text": """In the early 2000s, security researchers discovered they could knock down major web servers by sending HTTP POST requests with sorted key names.
The web servers used naive QuickSort with the first element as the pivot.
Sorting an already-sorted array of 20,000 items caused QuickSort to degrade into O(n^2) quadratic time, taking 400,000,000 operations instead of 280,000, pegging the CPU at 100% and timing out all requests!
The fix? Never pick the first element as the pivot! Always pick a random pivot or use Median-of-Three!""",
        "analogy_label": "💡 Real-World Metaphor: The Schoolyard Height Divider",
        "analogy_text": """Imagine a coach dividing 100 kids by height:
The coach picks one random kid (the Pivot) and shouts: 'Everyone shorter stand on the left, everyone taller on the right!'
In just one scan across the playground, the kids are divided. Then the coach repeats the command for each half. In just 7 rounds of shouting, all 100 kids are perfectly sorted!""",
        "mnemonic_title": "The Q.U.I.C.K. Partition",
        "mnemonic_rule": "Quench worst-case via randomized pivot selection · Unsorted partition in linear O(n) time · In-place swapping requires zero extra memory · Cache-friendly contiguous memory scanning · King of standard library sorting routines.",
        "mnemonic_desc": "Lomuto and Hoare partitioning scan contiguous array memory sequentially, making QuickSort maximize CPU cache hits far better than MergeSort or HeapSort.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The engine behind `std::sort` in C++, `List.sort()` in Dart, and array sorting routines in the V8 JavaScript runtime."""
    },
    27: {
        "title": "Graph Traversal: Dijkstra's Shortest Path & Topological Sort",
        "badge_color": "var(--cyan)",
        "bullets": [
            "How Google Maps finds the shortest route across millions of road segments in milliseconds.",
            "Dijkstra's Algorithm: Greedy relaxation using PriorityQueues.",
            "Topological Sorting: Linear ordering of tasks in Directed Acyclic Graphs (DAGs).",
            "Permanent Mnemonic: D.I.J.K.S.T.R.A.",
            "Live Pyodide Lab: Compute single-source shortest path and topological DAG ordering."
        ],
        "hook_title": "1. The Crime Scene: The Build System Circular Deadlock",
        "hook_text": """You run a build tool to compile a complex C++ or Flutter application with 150 modules.
The build hangs forever. Why? Module A depends on Module B, Module B depends on Module C, and Module C imports Module A!
Without a Topological Sort check on the dependency Directed Acyclic Graph (DAG), build systems deadlock or compile files before their headers exist.
Topological Sort detects cycles instantly and produces the exact linear sequence in which modules must be built!""",
        "analogy_label": "💡 Real-World Metaphor: Water Flooding Through Garden Pipes",
        "analogy_text": """Imagine turn on a garden hose at node A in an intricate pipe network:
Water naturally flows through the shortest, least resistive pipes first, reaching the nearest valves before expanding outward to distant reservoirs.
That is Dijkstra's algorithm: expanding the wavefront of shortest known distances one valve at a time!""",
        "mnemonic_title": "The D.I.J.K.S.T.R.A. Wavefront",
        "mnemonic_rule": "Distance array initialized to infinity · Iteratively pop minimum unvisited vertex from PriorityQueue · Just relax all outgoing edges · Known shortest paths are finalized permanently · Routes packets and builds dependency DAGs.",
        "mnemonic_desc": "Solves single-source shortest paths on non-negative weighted graphs in O((V + E) log V) time. If edge weights are negative, use Bellman-Ford instead.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Google Maps routing, network packet routing in OSPF/IS-IS, and build pipeline dependency ordering in Make, Ninja, and Flutter."""
    },
    28: {
        "title": "Computer Architecture: Memory Hierarchy & Cacheline Physics",
        "badge_color": "var(--rose)",
        "bullets": [
            "Why modern CPUs spend most of their time starving for data from RAM.",
            "The 100x Loop Performance Penalty: Row-major vs Column-major memory layout.",
            "Cachelines: The 64-byte chunks of silicon data transfer.",
            "Permanent Mnemonic: C.A.C.H.E.",
            "Live Pyodide Lab: Simulate direct-mapped and set-associative cache hits and misses."
        ],
        "hook_title": "1. The Crime Scene: The 100x Slower Loop",
        "hook_text": """A developer writes two functions to sum all numbers in a 4,096 x 4,096 integer matrix.
Function A iterates rows first: `for i in range(N): for j in range(N): sum += matrix[i][j]`. Time: 12 milliseconds.
Function B iterates columns first: `for j in range(N): for i in range(N): sum += matrix[i][j]`. Time: 1,400 milliseconds!
The exact same number of additions (16,777,216). The exact same numbers.
Why is Function B more than 100x slower?
Because computers do not fetch 1 integer from RAM. They fetch an entire 64-byte CACHELINE!
Function A reads contiguous memory, hitting L1 cache 99% of the time. Function B jumps across 16KB strides, missing the cache on EVERY SINGLE ACCESS and stalling the CPU waiting for slow DRAM!""",
        "analogy_label": "💡 Real-World Metaphor: The Desk vs The Basement Archive",
        "analogy_text": """Imagine doing research in a library:
• L1 Cache is the 3 open books sitting right in front of you on your desk (1 nanosecond access).
• DRAM is a box stored in the dark basement 4 floors down (100 nanoseconds access — 100x slower!).
If you read the pages in the book on your desk sequentially, you work at lightning speed. If you run down to the basement between every sentence, your research takes days!""",
        "mnemonic_title": "The C.A.C.H.E. Line",
        "mnemonic_rule": "Cache lines transfer in 64-byte chunks · Associativity prevents collision evictions · Coherence protocols stop stale multicore reads · Hit rates above 95% keep CPUs fed · Explains modern data-oriented memory design.",
        "mnemonic_desc": "Temporal locality (using the same data again soon) and Spatial locality (using adjacent memory bytes) are the single biggest determinants of software performance on modern hardware.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Data-oriented design in game engines, avoiding false sharing across Dart isolates, and optimizing GPU texture cache memory."""
    },
    29: {
        "title": "Automata Theory: DFAs, RegEx & Zero-Backtracking Lexers",
        "badge_color": "var(--indigo)",
        "bullets": [
            "Deterministic Finite Automata (DFA): Recognizing regular languages in strict O(n) time.",
            "The ReDoS Catastrophe: Why naive regular expressions with backtracking take 10,000 years on malformed inputs.",
            "Compiler Lexers: Converting raw text source code into clean token streams.",
            "Permanent Mnemonic: D.F.A.",
            "Live Pyodide Lab: Build and simulate a deterministic state machine recognizer."
        ],
        "hook_title": "1. The Crime Scene: The Regular Expression That Took Down Cloudflare",
        "hook_text": """On July 2, 2019, Cloudflare deployed a new firewall rule containing a regular expression to detect XSS attacks.
Within 15 minutes, CPU utilization across all Cloudflare servers worldwide spiked to 100%, taking down major websites across the globe.
What happened? Catastrophic Backtracking (ReDoS).
A regex engine with backtracking attempts every combinatorial permutation when an input fails to match, taking O(2^n) exponential time.
A Deterministic Finite Automaton (DFA) state machine NEVER backtracks: it reads each character once, transitions to the next state in O(1) time, and finishes in strict O(n) linear time!""",
        "analogy_label": "💡 Real-World Metaphor: The Subway Turnstile",
        "analogy_text": """Think of a subway turnstile:
• It has two states: LOCKED and UNLOCKED.
• If you drop a coin in the LOCKED state -> it transitions to UNLOCKED.
• If you push through the UNLOCKED state -> it transitions to LOCKED.
The turnstile doesn't remember who went through yesterday; it only knows its current state and the incoming action! That is the pure beauty of a Finite Automaton.""",
        "mnemonic_title": "The D.F.A. State Machine",
        "mnemonic_rule": "Deterministic transition for every input character · Finite set of discrete states · Always linear O(n) matching with zero backtracking · Direct execution engine in compiler lexers · Powers UI state management machines.",
        "mnemonic_desc": "A DFA is formally a 5-tuple (Q, Sigma, delta, q0, F). It guarantees linear processing speed regardless of adversarial inputs, making it secure against ReDoS attacks.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Compiler tokenizers (lexers), network packet filter validation, and reactive UI state machines in Flutter Bloc and Redux."""
    },
    30: {
        "title": "Computer Networks: TCP Sliding Window & Flow Control",
        "badge_color": "var(--emerald)",
        "bullets": [
            "Why Stop-and-Wait communication makes transoceanic fiber cables slower than dial-up.",
            "Bandwidth-Delay Product (BDP): Calculating how much data must stay in-flight to saturate a pipe.",
            "Flow Control (rwnd) vs Congestion Control (cwnd): Protecting the receiver vs protecting the network.",
            "Permanent Mnemonic: S.L.I.D.E.",
            "Live Pyodide Lab: Simulate a sliding window byte stream with packet drops and ACKs."
        ],
        "hook_title": "1. The Crime Scene: The 10 Gbps Cable That Only Transferred 2 MB/s",
        "hook_text": """A company buys a dedicated 10 Gbps transoceanic fiber line connecting London and Singapore.
Ping latency is 200 milliseconds.
When they copy a database backup, the transfer speed caps out at an abysmal 2 MB/s—using less than 0.2% of the cable's capacity!
Why? The operating system's TCP receive window buffer (rwnd) was capped at 64 KB!
If the sender transmits 64 KB and must wait 200 ms for an acknowledgment before sending more, the maximum throughput is strictly limited to 64 KB / 0.200s = 320 KB/s!
To saturate the line, the window must be expanded to match the Bandwidth-Delay Product (10 Gbps * 0.2s = 250 Megabytes of in-flight data)!""",
        "analogy_label": "💡 Real-World Metaphor: The Conveyor Belt Across the Ocean",
        "analogy_text": """Imagine a giant conveyor belt connecting two warehouses:
If you place one box on the belt, wait 10 minutes for it to arrive, and only put the second box on when you get a phone call, the conveyor belt is 99.9% empty!
The Sliding Window keeps the conveyor belt completely packed with boxes in flight, sliding forward continuously as confirmations return on a return wire!""",
        "mnemonic_title": "The S.L.I.D.E. Window",
        "mnemonic_rule": "Sequence numbers order byte streams · Linear window slides forward as ACKs return · Inflight bytes limited by min(rwnd, cwnd) · Drops trigger exponential backoff · Essential for rural mobile sync reliability.",
        "mnemonic_desc": "Flow control ensures the sender never overwhelms the receiver's socket buffer. Congestion control ensures the sender never overwhelms intermediate router queues.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Mobile network sync reliability in mForm and BSE mobile sync, WebSocket streaming in Flutter, and TCP socket buffer kernel tuning."""
    },
    31: {
        "title": "Advanced OS: Preemptive Scheduling & The Banker's Deadlock Algorithm",
        "badge_color": "var(--amber)",
        "bullets": [
            "Preemptive Scheduling: How timer hardware interrupts prevent rogue infinite loops from freezing the OS.",
            "The 4 Coffman Conditions for Deadlock: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait.",
            "Dijkstra's Banker's Algorithm: Verifying safe resource allocation states before granting locks.",
            "Permanent Mnemonic: B.A.N.K.E.R.",
            "Live Pyodide Lab: Simulate Banker's safe state detection with resource allocation vectors."
        ],
        "hook_title": "1. The Crime Scene: The Android App Freeze in Production",
        "hook_text": """A user taps 'Pay Now'.
Thread A grabs Lock 1 (Database Connection) and waits for Lock 2 (User Auth Token).
Simultaneously, Thread B grabs Lock 2 (User Auth Token) and waits for Lock 1 (Database Connection).
Neither thread will ever release what it holds. Both threads wait forever.
The phone's screen freezes, touch input stops responding, and Android's Watchdog kills the process with an ANR crash.
Deadlock is the ultimate multi-threading nightmare: when two or more processes form a circular wait for exclusive resources!""",
        "analogy_label": "💡 Real-World Metaphor: The Conservative Bank Teller",
        "analogy_text": """Imagine a small town bank with 10 total gold coins in its vault:
Three businesses want loans: Business A needs up to 6 coins, Business B needs up to 5, Business C needs up to 4.
The banker NEVER lends coins if doing so leaves the vault with too few coins to allow AT LEAST ONE business to complete its project and return all its borrowed gold!
If a safe path exists where everyone can eventually finish, the loan is granted; otherwise, the borrower is made to wait!""",
        "mnemonic_title": "The B.A.N.K.E.R. Safe State",
        "mnemonic_rule": "Borrowing only allowed if a safe execution path exists · Avoids circular wait deadlock traps · Needs matrix of max claim minus current allocation · Kernel preempts greedy threads via hardware timer interrupts · Critical for SQLite multithreaded connection safety.",
        "mnemonic_desc": "If allocating resources leaves the system in an unsafe state (where no sequence of processes can finish under worst-case claims), the allocation must be denied.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Preventing deadlocks across multi-threaded SQLite connection pools, Android priority inheritance mutexes, and Linux CFS process scheduling."""
    },
    34: {
        "title": "Distributed Systems: Vector Clocks & Causal Consistency",
        "badge_color": "var(--cyan)",
        "bullets": [
            "Why physical wall-clock timestamps (NTP) are completely unreliable in distributed systems.",
            "Lamport Clocks vs Vector Clocks: Capturing the causal 'happened-before' relation across nodes.",
            "Concurrent Conflict Detection: Knowing when two mobile edits happened in parallel without seeing each other.",
            "Permanent Mnemonic: V.E.C.T.O.R.",
            "Live Pyodide Lab: Simulate vector clocks across 3 distributed nodes and detect concurrent edits."
        ],
        "hook_title": "1. The Crime Scene: The WhatsApp Message from the Future",
        "hook_text": """You send a message to a friend: 'Did you make it home?'
Your friend's phone has a clock drifted 5 minutes into the past.
When they reply: 'Yes, just arrived', their reply appears ABOVE your question in the chat!
Physical clocks on computers drift constantly due to heat and quartz crystal imperfection.
In distributed systems, you CANNOT rely on wall-clock time (e.g. `DateTime.now()`) to order events!
Vector clocks eliminate reliance on physical clocks entirely by counting events causally: each node tracks how many events it has observed across all other nodes!""",
        "analogy_label": "💡 Real-World Metaphor: The Traveling Passport Stampers",
        "analogy_text": """Imagine 3 friends traveling in different countries:
Every friend carries a booklet with 3 boxes: [My events, Friend B's events, Friend C's events].
Whenever you do something, you increment your own box.
Whenever you send a postcard to a friend, you attach your whole booklet!
When your friend receives your postcard, they update every box in their booklet to the HIGHEST number seen. Now, everyone knows the exact causal history of who heard what first!""",
        "mnemonic_title": "The V.E.C.T.O.R. Clock",
        "mnemonic_rule": "Vector of counters one per distributed node · Event increments local counter · Cross-node messages attach the full vector · Tracks causal happened-before ordering without GPS clocks · The foundation of offline-first mobile sync.",
        "mnemonic_desc": "Event A causally precedes event B (A -> B) if and only if every entry in A's vector is <= B's vector, and at least one entry is strictly less. If neither precedes the other, they are concurrent conflicts!",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The mathematical foundation of offline-first sync conflict resolution in mForm, Git commit ancestry graphs, and Amazon DynamoDB version vectors."""
    },
    35: {
        "title": "Cryptography Engineering: RSA Keygen & Digital Signatures",
        "badge_color": "var(--rose)",
        "bullets": [
            "Asymmetric Cryptography: How to share a secret across the public internet without a shared password.",
            "Euler's Totient and Prime Factorization: The mathematical trapdoor that makes RSA work.",
            "Timing Attacks & Constant-Time Montgomery Multiplication: Why software speed optimization can leak private keys.",
            "Permanent Mnemonic: R.S.A.",
            "Live Pyodide Lab: Generate an RSA keypair, encrypt, decrypt, and verify digital signatures."
        ],
        "hook_title": "1. The Crime Scene: The 2-Nanosecond Private Key Theft",
        "hook_text": """A bank runs a secure SSL server with 2048-bit RSA encryption.
A hacker sends 1,000,000 normal HTTPS requests and measures how many nanoseconds the server takes to respond.
Because the server's modular exponentiation algorithm used a naive `if (bit == 1)` branch that skipped an operation when the bit was 0, the hacker deduced every single bit of the bank's secret private key purely from response time fluctuations!
In cryptography engineering, correctness is not enough: operations MUST execute in constant time regardless of key bits!""",
        "analogy_label": "💡 Real-World Metaphor: The Self-Locking Padlock",
        "analogy_text": """Imagine buying an open brass padlock and mailing it to your friend:
Anyone in the postal service can inspect the open padlock.
Your friend places a letter in a box, snaps your padlock shut, and mails it back.
Nobody in the postal service can open the box—only YOU hold the unique key that turns the tumblers!
That is Asymmetric Encryption: anyone can encrypt with the public key, but only the owner can decrypt with the private key.""",
        "mnemonic_title": "The R.S.A. Trapdoor",
        "mnemonic_rule": "Relies on Euler's totient phi(n) = (p-1)*(q-1) · Secret private exponent d = e^-1 mod phi(n) · Asymmetric encryption allows public distribution of e · Constant-time Montgomery reduction prevents cache timing attacks · Secures APK signatures and HTTPS.",
        "mnemonic_desc": "Encrypt: c = m^e mod n. Decrypt: m = c^d mod n. Digital Signature: s = m^d mod n. Verification: s^e mod n == m.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Directly secures HTTPS TLS handshakes, Android APK signature scheme v2/v3, and on-device biometric signature verification."""
    },
    36: {
        "title": "Software Architecture: Observer Pattern & Reactive Streams",
        "badge_color": "var(--indigo)",
        "bullets": [
            "Why tightly coupled spaghetti callbacks cause memory leaks and frozen UIs.",
            "The Observer Pattern: Decoupling event producers from event consumers.",
            "Reactive Event Streams: Transforming, debouncing, and filtering data as asynchronous pipelines.",
            "Permanent Mnemonic: R.E.A.C.T.",
            "Live Pyodide Lab: Build a reactive event bus with subscription filters and cancelable listeners."
        ],
        "hook_title": "1. The Crime Scene: The Memory Leak That Drained 800 MB",
        "hook_text": """A user navigates back and forth between the Home screen and the Profile screen in a Flutter app 20 times.
The app gets slower and slower until Android kills it with an OutOfMemoryError.
You inspect the memory heap: there are 20 invisible ProfileScreen instances still alive in RAM!
Why? The ProfileScreen registered a callback listener to the global UserSession event bus, but never cancelled the subscription when the widget was popped!
The global event bus held strong references to all 20 destroyed widgets, preventing the garbage collector from reclaiming a single byte!""",
        "analogy_label": "💡 Real-World Metaphor: The Magazine Postal Tube",
        "analogy_text": """Think of a newspaper publisher:
The printing press doesn't know who you are; it simply drops newspapers into postal distribution tubes.
Subscribers receive papers as they roll off the press.
If you move to a new house, you unsubscribe so the mail carrier doesn't pile thousands of newspapers on your old doorstep until the porch collapses!""",
        "mnemonic_title": "The R.E.A.C.T. Stream",
        "mnemonic_rule": "Register subscribers loosely without tight coupling · Emit immutable event payloads · Asynchronous stream dispatch buffers UI events · Cancel subscriptions on widget dispose to stop memory leaks · The heartbeat of Flutter Streams and Kotlin Flows.",
        "mnemonic_desc": "Producers emit events; consumers react. Operators like debounce, map, and filter transform data pipelines without modifying producer source code.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The foundational architecture of Flutter StreamBuilder, ValueNotifier, RxDart, and Kotlin StateFlow in Android MVVM."""
    },
    37: {
        "title": "Mobile Systems: Android Looper, Handler & JNI Bridges",
        "badge_color": "var(--emerald)",
        "bullets": [
            "How the Android Main Thread drains its synchronized MessageQueue via Looper.loop().",
            "Why performing I/O or heavy math on the Main Thread triggers the 5-second ANR crash.",
            "The JNI & Dart FFI Bridge: Passing memory pointers cleanly across language runtime borders.",
            "Permanent Mnemonic: L.O.O.P.E.R.",
            "Live Pyodide Lab: Simulate an Android Looper event loop processing delayed message queues."
        ],
        "hook_title": "1. The Crime Scene: The Dreaded Red 'ANR' Screen",
        "hook_text": """A user taps 'Download File'.
A developer writes: `val data = URL('...').readBytes()` directly inside the button click listener.
The network lags for 5 seconds.
The phone stops animating, touch inputs freeze, and Android's OS Watchdog kills the app with:
`Application Not Responding: Input dispatching timed out (Waiting to process key event).`
Why? Android's entire visual UI runs on a SINGLE thread controlled by an infinite loop (`Looper.loop()`).
If you block that loop for even 16 milliseconds, you drop frames. If you block it for 5,000 milliseconds, Android executes your app!""",
        "analogy_label": "💡 Real-World Metaphor: The Single Sushi Chef on the Conveyor",
        "analogy_text": """Imagine a sushi chef standing at a conveyer belt pulling order tickets off a rack:
• Ticket 1: Draw button (1ms).
• Ticket 2: Animate card (2ms).
• Ticket 3: Cook 10-minute roast chicken!
If the chef stops to cook the 10-minute roast, all 50 customers waiting for quick sushi plates starve and walk out of the restaurant!
The chef must delegate the roast to a kitchen assistant (Background Thread) and only plate the meal when it is ready!""",
        "mnemonic_title": "The L.O.O.P.E.R. Heartbeat",
        "mnemonic_rule": "Loop continuously drains the MessageQueue · Offload heavy CPU work to background worker threads · Only touch UI widgets on the main Looper thread · Platform channels bridge to native C++ via JNI / Dart FFI · Powers all Flutter and Android responsive runtimes.",
        "mnemonic_desc": "Android's UI thread is simply while(true) { Message m = queue.next(); m.target.dispatchMessage(m); }. Heavy tasks must be posted to background threads.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The execution model underpinning all native Android apps, Flutter platform channels, and SipLLM's Dart FFI C++ bridge."""
    },
    38: {
        "title": "Numerical Analysis: IEEE-754 Bit Unpacking & Condition Numbers",
        "badge_color": "var(--amber)",
        "bullets": [
            "How floating-point numbers unpack into 1 Sign bit, 8 Exponent bits, and 23 Mantissa bits.",
            "The Catastrophic Cancellation Bug: Why subtracting two nearly-equal floats vaporizes precision.",
            "Condition Numbers: Measuring how sensitive an algorithm is to tiny input perturbations.",
            "Permanent Mnemonic: F.L.O.A.T.",
            "Live Pyodide Lab: Unpack IEEE-754 32-bit float bits into sign, exponent, and fraction."
        ],
        "hook_title": "1. The Crime Scene: The Patriot Missile Roundoff Disaster",
        "hook_text": """On February 25, 1991, an Iraqi Scud missile struck an American military barracks in Dhahran, killing 28 soldiers.
An American Patriot missile defense battery was stationed nearby, but failed to track or intercept the incoming rocket.
Why? A tiny floating-point roundoff error in the clock software!
The system's internal clock measured time in tenths of a second (0.1s).
In binary floating-point, 0.1 is an infinite repeating fraction (like 1/3 in decimal: 0.0001100110011...).
Truncating to 24 bits caused a loss of 0.000000095 seconds per tick.
After 100 continuous hours of operation, the error accumulated to 0.34 seconds.
At 4,000 miles per hour, a Scud travels more than half a kilometer in 0.34 seconds—placing the missile completely outside the radar tracking window!""",
        "analogy_label": "💡 Real-World Metaphor: The Microscope with a Fixed Ruler",
        "analogy_text": """Imagine a microscope with a ruler that only has 7 tick marks:
• When viewing a giant elephant, 1 tick mark is 1 meter (huge range, coarse precision).
• When viewing an amoeba, 1 tick mark is 1 micrometer (tiny range, fine precision).
A float adjusts its exponent to zoom in or out, but it NEVER has more than 23 bits of precision! When you add an elephant and an amoeba together, the amoeba is rounded off to zero!""",
        "mnemonic_title": "The F.L.O.A.T. Bitfield",
        "mnemonic_rule": "Fraction mantissa holds precision · Logarithmic exponent scales the dynamic range · One bit for sign · Accumulating small additions triggers roundoff drift · Underpins GPU neural quantization and physics engines.",
        "mnemonic_desc": "Value = (-1)^s * 2^(e - 127) * (1 + fraction). Floating point addition is NOT associative: (a + b) + c does not always equal a + (b + c)!",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Essential for debugging NaN propagation in PyTorch/TensorFlow, quantization scale calculations in GGUF models, and mobile physics stability."""
    },
    39: {
        "title": "Mathematical Optimization: Adam with Exponential Moving Averages",
        "badge_color": "var(--cyan)",
        "bullets": [
            "Why standard Stochastic Gradient Descent (SGD) gets trapped in narrow ravines.",
            "Momentum (First Moment): Accumulating velocity to power through noisy flat plateaus.",
            "Adaptive Learning Rates (Second Moment): Damping updates on steep volatile weights.",
            "Permanent Mnemonic: A.D.A.M.",
            "Live Pyodide Lab: Implement the complete Adam optimizer update rule with bias correction."
        ],
        "hook_title": "1. The Crime Scene: The Gradient Descent Sled in a Ravine",
        "hook_text": """You train a neural network using standard gradient descent: w = w - lr * grad.
The loss drops for 10 epochs, then oscillates wildly back and forth across a narrow canyon without making any forward progress.
Why? The canyon walls are steep (huge gradients), while the floor of the canyon slopes gently forward (tiny gradients).
Standard gradient descent spends all its energy bouncing off the steep canyon walls!
The Adam (Adaptive Moment Estimation) optimizer solves this by calculating TWO running averages: momentum to carry forward velocity, and variance scaling to damp down wild oscillations!""",
        "analogy_label": "💡 Real-World Metaphor: The Heavy Bobsled on Ice",
        "analogy_text": """Imagine rolling a heavy bobsled down a bumpy snow mountain:
• A light tennis ball (pure gradient descent) gets deflected and stopped by every pebble and rut.
• A heavy bobsled (Momentum) builds up speed; small rocks cannot divert its direction, and it powers straight through flat patches!
Meanwhile, adaptive brakes (RMSprop variance) squeeze the brakes whenever the track turns dangerously steep!""",
        "mnemonic_title": "The A.D.A.M. Navigator",
        "mnemonic_rule": "Adaptive learning rate per parameter · Decay parameter beta1 tracks first moment momentum · Accumulator beta2 tracks second moment uncentered variance · Momentum carries through flat plateaus · Universal optimizer for LLM training.",
        "mnemonic_desc": "m_t = beta1*m + (1-beta1)*g. v_t = beta2*v + (1-beta2)*g^2. Divide m_hat by sqrt(v_hat + eps) to compute parameter step.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The universal optimization algorithm used for training and fine-tuning modern deep networks, Transformer LLMs, and LoRA adapters."""
    },
    40: {
        "title": "Classical Machine Learning: Logistic Regression & Decision Boundaries",
        "badge_color": "var(--indigo)",
        "bullets": [
            "Why linear regression fails completely on binary classification tasks.",
            "The Sigmoid Activation: Squishing real numbers into strict (0, 1) probabilities.",
            "Cross-Entropy Loss: Penalizing confident wrong answers with steep logarithmic penalties.",
            "Permanent Mnemonic: S.I.G.M.O.I.D.",
            "Live Pyodide Lab: Train a 2D logistic regression classifier with gradient descent."
        ],
        "hook_title": "1. The Crime Scene: The Medical Predictor That Output 180% Probability",
        "hook_text": """A developer tries to predict whether a patient has a tumor (0 = Benign, 1 = Malignant) using standard linear regression: y = w*x + b.
For a patient with a large tumor, the model outputs: 'Probability of malignancy: 1.8 (180%)!'
For a patient with no symptoms, it outputs: '-0.3 (-30%)!'
Probabilities cannot be negative, and cannot exceed 100%.
The Sigmoid function sigma(z) = 1 / (1 + e^-z) smoothly squishes any real number from negative infinity to positive infinity into an exact probability between 0.0 and 1.0!""",
        "analogy_label": "💡 Real-World Metaphor: The S-Shaped Light Dimmer Switch",
        "analogy_text": """Think of a light dimmer switch with built-in rubber stops:
No matter how hard you shove the switch to the left, the light never goes below 0% brightness (completely dark).
No matter how hard you shove it to the right, it never exceeds 100% brightness.
The middle transition is smooth, allowing gradual control between off and on!""",
        "mnemonic_title": "The S.I.G.M.O.I.D. Curve",
        "mnemonic_rule": "Squashes linear dot-product into (0, 1) probability range · Inverts odds via cross-entropy loss · Gradient update shares exact formula with linear regression · Monotonic derivative enables smooth gradient descent · Powers mobile on-device classification.",
        "mnemonic_desc": "Loss = -[y*log(p) + (1-y)*log(1-p)]. Gradient with respect to weights is simply (p - y) * x.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Used in on-device gesture recognition in mobile apps, spam filters, fraud detection scoring, and binary decision trees."""
    },
    41: {
        "title": "Deep Learning Foundations: Reverse-Mode Autograd Tape",
        "badge_color": "var(--rose)",
        "bullets": [
            "Why computing derivatives by numerical perturbation would take 3 years per training step.",
            "The Computational Graph: Tracking operations as a Directed Acyclic Graph.",
            "Reverse Accumulation: Propagating adjoints backward in a single topological sweep.",
            "Permanent Mnemonic: T.A.P.E.",
            "Live Pyodide Lab: Build an autograd computation graph with backward pass verification."
        ],
        "hook_title": "1. The Crime Scene: The 1,000,000-Parameter Gradient Impossible Dream",
        "hook_text": """Imagine training a neural network with 1,000,000 weights.
To calculate the gradient using high-school calculus:
You tweak weight 1 by 0.0001, run the whole network forward, and measure the change.
Then you tweak weight 2, run the network forward, and measure the change...
To do one single training step, you would have to run the network 1,000,000 times!
Reverse-Mode Automatic Differentiation computes the exact analytical gradients for all 1,000,000 weights simultaneously in ONE SINGLE BACKWARD PASS! That single algorithmic breakthrough made modern AI possible!""",
        "analogy_label": "💡 Real-World Metaphor: The Tape Recorder Playing in Reverse",
        "analogy_text": """Imagine a cassette tape recorder in a laboratory:
During the Forward pass, the tape records every calculation that happens: 'Multiply A by B, Add C, Apply Sigmoid'.
When you reach the final loss, you stop the tape and press REVERSE.
As the tape unspools backwards, each operation multiplies the incoming error gradient by its local derivative and sends it backward to its inputs!""",
        "mnemonic_title": "The T.A.P.E. Autograd Engine",
        "mnemonic_rule": "Track forward graph of tensor operations · Accumulate local derivatives along the way · Propagate adjoints backward via chain rule · Exactly one backward pass computes all gradients simultaneously · The core engine of PyTorch.",
        "mnemonic_desc": "Reverse mode is optimal when a function has many inputs (millions of weights) and one scalar output (Loss), scaling as O(1) backward passes regardless of parameter count.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The foundational core of PyTorch (torch.autograd), Micrograd, JAX autodiff, and all modern neural network training frameworks."""
    },
    42: {
        "title": "Modern Neural Architectures: Residual Connections & LayerNorm",
        "badge_color": "var(--cyan)",
        "bullets": [
            "The Vanishing Gradient Problem: Why early 30-layer networks performed worse than 5-layer networks.",
            "Residual Skip Connections: Giving gradients an unhindered express highway to the earliest layers.",
            "Layer Normalization: Stabilizing activation variance across token embedding dimensions.",
            "Permanent Mnemonic: R.E.S.I.D.U.A.L.",
            "Live Pyodide Lab: Simulate forward and backward pass through a residual layer with identity skip."
        ],
        "hook_title": "1. The Crime Scene: The Deep Network That Learned Nothing",
        "hook_text": """In 2014, researchers attempted to train a 30-layer deep convolutional network.
The network failed to learn: training error was WORSE than a simple 5-layer network.
Why? As gradients multiplied backwards through 30 layers with weights < 1.0, the signal decayed exponentially (0.5^30 ≈ 0.0000000009). The first layers received zero gradient updates!
In 2015, Kaiming He introduced ResNet with a revolutionary addition: x_{l+1} = x_l + F(x_l).
By simply adding the input x directly to the output, gradients have an uninterrupted identity highway with derivative = 1.0 that travels straight back to layer 1 without decay!""",
        "analogy_label": "💡 Real-World Metaphor: The Express Highway Bridge",
        "analogy_text": """Imagine driving across town through 20 stoplights:
A residual connection is an express elevated highway built directly over the city:
Cars that want to make local turns take the scenic winding road (F(x)).
Cars that want to travel straight across town take the frictionless elevated highway (x).
Information and gradients are never trapped in local traffic!""",
        "mnemonic_title": "The R.E.S.I.D.U.A.L. Highway",
        "mnemonic_rule": "Route identity forward x + F(x) · Eliminates gradient vanishing down deep layers · Smooths the optimization loss landscape · Integrates LayerNorm before attention blocks · The fundamental backbone of all Transformers.",
        "mnemonic_desc": "Because d(x + F(x))/dx = 1 + dF/dx, gradients can flow backward through the '1' term even if dF/dx vanishes completely.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The foundational architecture of ResNets, Transformers (GPT, Claude, Gemini, LLaMA), and diffusion models."""
    },
    45: {
        "title": "Fast Attention Algorithms: Online Softmax & Memory Tiling (FlashAttention)",
        "badge_color": "var(--rose)",
        "bullets": [
            "The High-Bandwidth Memory (HBM) Wall: Why GPUs spend 90% of their time waiting for DRAM reads.",
            "The O(N^2) Attention Memory Bottleneck: Storing full N x N attention matrices in slow memory.",
            "Online Softmax: Computing running maximums and sums across blocks without storing intermediate matrices.",
            "Permanent Mnemonic: F.L.A.S.H.",
            "Live Pyodide Lab: Implement online softmax computing exact values across streaming blocks."
        ],
        "hook_title": "1. The Crime Scene: The GPU Tensor Cores That Starved for Memory",
        "hook_text": """An engineer runs attention on a prompt with 8,192 tokens.
The attention matrix requires 8,192 x 8,192 floats per head = 256 Megabytes of intermediate memory!
The GPU's Tensor Cores can compute the math in 0.2 milliseconds.
Yet the attention kernel took 8.5 milliseconds—40x slower than the hardware could execute!
Why? Because the GPU had to write the massive 256MB matrix out to slow High-Bandwidth Memory (HBM), and then read it all back in just to multiply by V!
The GPU was memory-bound, spending 95% of its time waiting for memory bus transfers!
FlashAttention computes attention in small SRAM tiles using Online Softmax, NEVER writing the intermediate matrix to DRAM and cutting memory from O(N^2) to O(N)!""",
        "analogy_label": "💡 Real-World Metaphor: The Small Scratchpad in the Bank Vault",
        "analogy_text": """Imagine an accountant auditing 10,000 heavy ledger books in a basement vault:
• Naive Attention: Carrying all 10,000 ledger books upstairs to a desk, spreading them across the floor, and calculating.
• FlashAttention: Carrying a small scratchpad into the vault, opening 1 book at a time, updating the running maximum and running sum on the scratchpad, and walking out with the final answer!""",
        "mnemonic_title": "The F.L.A.S.H. Tiler",
        "mnemonic_rule": "Fuse kernel execution into GPU SRAM · Lock memory to O(N) instead of O(N^2) · Avoid writing intermediate attention matrix to DRAM · Streaming blocks compute online softmax running max · Makes 128k context windows possible.",
        "mnemonic_desc": "Online softmax updates running statistics m_new = max(m_prev, x_max) and d_new = d_prev * exp(m_prev - m_new) + sum(exp(x - m_new)), achieving exact numerical equivalence with zero memory bloat.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The core breakthrough behind FlashAttention-2/3 in PyTorch, high-throughput vLLM inference, and edge LLM runtime optimization."""
    },
    47: {
        "title": "Edge Memory Residency Planning: Weight Streaming & KV Cache Paging",
        "badge_color": "var(--emerald)",
        "bullets": [
            "The 4GB Mobile RAM Ceiling: How to run an 8-billion parameter model without triggering Linux OOM-killer.",
            "Static Residency vs On-Demand Streaming: Pinning embedding tables and streaming transformer blocks.",
            "PagedAttention: Managing key-value caches like OS virtual memory pages to eliminate fragmentation.",
            "Permanent Mnemonic: P.A.G.E.D.",
            "Live Pyodide Lab: Simulate a memory residency planner enforcing a strict RAM ceiling."
        ],
        "hook_title": "1. The Crime Scene: The Android SIGKILL at Layer 14",
        "hook_text": """You run a quantized 7B language model on an Android smartphone with 6GB total RAM.
Layers 1 through 13 load cleanly.
At Layer 14, Android's Low Memory Killer daemon (lmkd) detects system RAM dropping below 500MB and sends `SIGKILL` to the app process.
The app disappears instantly without an error trace.
How do you run large language models on edge devices with strict memory budgets?
You enforce strict memory residency planning: you pin the active working buffers, and stream weight blocks from flash storage or DMA rings just-in-time, keeping peak RSS strictly below the hardware ceiling!""",
        "analogy_label": "💡 Real-World Metaphor: The Revolving Stage in a Theater",
        "analogy_text": """Imagine a small theater that can only fit 10 actors on stage at once, but the play has 100 characters:
• You don't try to cram all 100 actors onto the stage at once (the stage will collapse!).
• Actors for Scene 1 perform. As Scene 1 ends, they walk off into the wings while actors for Scene 2 walk on!
The stage always holds exactly 10 actors, but the entire 100-character epic play executes flawlessly!""",
        "mnemonic_title": "The P.A.G.E.D. Memory Plan",
        "mnemonic_rule": "Partition KV cache into discrete block tables · Avoid contiguous memory fragmentation · Garbage collect finished request blocks immediately · Enforce strict RAM residency budgets like SipLLM's --ram-budget 4G · The secret to high-throughput LLM serving.",
        "mnemonic_desc": "The exact algorithm implemented in SipLLM (src/mem_plan.cpp): calculating total working set (weights + KV cache + activations) to guarantee peak RSS never exceeds the configured hardware ceiling.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """The core memory architecture of SipLLM (--ram-budget 4G), vLLM PagedAttention, and llama.cpp mmap weight streaming."""
    },
    49: {
        "title": "Information Theory: Shannon Entropy & BPE Tokenization",
        "badge_color": "var(--amber)",
        "bullets": [
            "Shannon Entropy: The mathematical measure of surprise, information, and uncertainty.",
            "Perplexity (PPL): How language models measure confusion over token distributions.",
            "Byte Pair Encoding (BPE): Compressing frequent letter pairs into unified token vocabularies.",
            "Permanent Mnemonic: E.N.T.R.O.P.Y.",
            "Live Pyodide Lab: Compute Shannon entropy and train a toy Byte Pair Encoding tokenizer."
        ],
        "hook_title": "1. The Crime Scene: The Unpredictable Token Generation",
        "hook_text": """An engineer evaluates two language models:
Model A produces smooth, coherent text with a Perplexity score of 8.2.
Model B produces repetitive, nonsensical babble with a Perplexity score of 240.0.
What is Perplexity? It is simply 2 raised to the Shannon Entropy: PPL = 2^H(X)!
Entropy measures the average number of bits required to guess the next token.
A model with low entropy is confident and accurate; a model with high entropy is guessing wildly in the dark!""",
        "analogy_label": "💡 Real-World Metaphor: The 20 Questions Game",
        "analogy_text": """Imagine playing 20 Questions to guess an animal:
• If I tell you 'It's either a dog or a cat', your uncertainty is 1 bit (1 yes/no question).
• If I tell you 'It's any animal on planet Earth', your uncertainty is high entropy (many yes/no questions needed!).
Entropy is simply the count of yes/no questions required to eliminate surprise!""",
        "mnemonic_title": "The E.N.T.R.O.P.Y. Compression",
        "mnemonic_rule": "Expected surprise measured in bits -sum(p * log2(p)) · Number of bits bounds compression limits · Perplexity 2^H measures model uncertainty · Frequent letter pairs merge via Byte Pair Encoding · Powers token vocabularies in all LLMs.",
        "mnemonic_desc": "BPE iteratively finds the most frequent pair of adjacent bytes and merges them into a single token, creating efficient subword vocabularies for language models.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Byte Pair Encoding tokenizers (tiktoken, SentencePiece), evaluating language model loss in training, and data compression algorithms (gzip, zstd)."""
    },
    50: {
        "title": "Category Theory: Monads, Functors & Affine Ownership Semantics",
        "badge_color": "var(--indigo)",
        "bullets": [
            "The Billion-Dollar Mistake: How Sir Tony Hoare's null reference caused 60 years of software crashes.",
            "Functors and Monads: Wrapping computations safely inside container pipelines.",
            "Affine Ownership: How Rust's borrow checker enforces mathematical 'use-at-most-once' resource safety.",
            "Permanent Mnemonic: M.O.N.A.D.",
            "Live Pyodide Lab: Build a Maybe monad pipeline chaining operations without null checks."
        ],
        "hook_title": "1. The Crime Scene: The Billion-Dollar Null Pointer Exception",
        "hook_text": """In 1965, British computer scientist Sir Tony Hoare invented the `null` reference for the ALGOL W language:
'I call it my billion-dollar mistake. It was the invention of the null reference in 1965... This has led to innumerable errors, vulnerabilities, and system crashes, which have probably caused a billion dollars of pain and damage in the last forty years.'
Why are null pointers so catastrophic? Because a variable that might be null requires defensive `if (x != null)` checks everywhere. The moment you miss one check, your app crashes with a NullPointerException!
Category Theory solves this with Monads (like Optional or Maybe): a value is wrapped inside a safe box, and functions transform the inside of the box without ever exposing nulls to the outside world!""",
        "analogy_label": "💡 Real-World Metaphor: The Standard Cargo Shipping Container",
        "analogy_text": """Think of a standardized ocean shipping container (Functor/Monad):
You don't throw loose glassware and bicycles into the cargo hold of a ship.
You pack them safely inside a sealed steel container.
Cranes move the container (Map), stack containers (Bind), and ship them across the globe without ever opening the doors or breaking the fragile glass inside!""",
        "mnemonic_title": "The M.O.N.A.D. Box",
        "mnemonic_rule": "Monoid in the category of endofunctors · Object wrapped safely inside a container · Nothing/Null handled gracefully via unit and bind · Affine ownership guarantees exactly-once resource usage · Powers Rust borrow checker and Dart Futures.",
        "mnemonic_desc": "Unit wraps a plain value into M(x). Bind (>>=) takes M(x) and a function f: x -> M(y) and produces M(y). If x is None/Null, execution short-circuits gracefully without crashing.",
        "systems_title": "In Your Real Systems Work",
        "systems_text": """Underpins Rust's affine borrow checker, Dart's Future async/await concurrency primitives, and modern functional UI pipelines in Flutter."""
    }
}

print(f"Pedagogy metadata defined for all {len(PEDAGOGY_DATA)} missing chapters.")

def render_chapter_html(chap_num, mod_info, ped_info, prev_file, next_file, prev_title, next_title):
    mid_str = f"{chap_num:02d}"
    title = ped_info["title"]
    badge_color = ped_info.get("badge_color", "var(--cyan)")
    tag = mod_info["tag"]
    code = mod_info["code"]

    bullets_html = "".join([f"      <br>{i+1}. {b}\n" for i, b in enumerate(ped_info["bullets"])])
    
    prev_link = f'<a href="{prev_file}">← Chapter {chap_num-1:02d}: {prev_title}</a>' if prev_file else '<a href="index.html">← Master Textbook Hub</a>'
    next_link = f'<a href="{next_file}">Next: Chapter {chap_num+1:02d}: {next_title} →</a>' if next_file else '<a href="index.html">🎓 Master Textbook Hub (Course Complete!) →</a>'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tutorial {mid_str}: {title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js"></script>
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    :root {{
      --bg: #07090e;
      --card-bg: #0d121c;
      --card-sub: #131b2c;
      --border: rgba(255, 255, 255, 0.08);
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --cyan: #38bdf8;
      --emerald: #10b981;
      --amber: #f59e0b;
      --rose: #f43f5e;
      --indigo: #6366f1;
      --purple: #a855f7;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: 'Inter', sans-serif;
      line-height: 1.8;
      padding: 3rem 1.5rem 6rem;
    }}
    .wrapper {{ max-width: 920px; margin: 0 auto; }}
    .chap-badge {{
      font-family: 'Fira Code', monospace;
      color: {badge_color};
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 0.5rem;
    }}
    h1 {{
      font-size: 2.35rem;
      font-weight: 900;
      letter-spacing: -0.02em;
      margin-bottom: 1.5rem;
      line-height: 1.25;
    }}
    h2 {{
      font-size: 1.55rem;
      font-weight: 800;
      color: #fff;
      margin: 2.8rem 0 1rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 0.5rem;
    }}
    h3 {{
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--cyan);
      margin: 2rem 0 0.6rem;
    }}
    p {{ margin-bottom: 1.25rem; color: #cbd5e1; font-size: 1.02rem; }}
    
    .mnemonic-card {{
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(217, 119, 6, 0.05));
      border: 2px solid var(--amber);
      border-radius: 10px;
      padding: 1.5rem 1.8rem;
      margin: 2rem 0;
      box-shadow: 0 8px 24px rgba(245, 158, 11, 0.1);
    }}
    .mnemonic-header {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-family: 'Fira Code', monospace;
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--amber);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 0.6rem;
    }}
    .mnemonic-title {{
      font-size: 1.35rem;
      font-weight: 900;
      color: #fff;
      margin-bottom: 0.6rem;
    }}
    .mnemonic-rule {{
      font-size: 1.05rem;
      color: #fef3c7;
      font-weight: 600;
      line-height: 1.5;
    }}
    .mnemonic-desc {{
      font-size: 0.92rem;
      color: #cbd5e1;
      margin-top: 0.6rem;
    }}

    .analogy-box {{
      background: rgba(99, 102, 241, 0.08);
      border-left: 4px solid var(--indigo);
      border-radius: 0 8px 8px 0;
      padding: 1.4rem 1.6rem;
      margin: 1.8rem 0;
    }}
    .analogy-label {{
      font-family: 'Fira Code', monospace;
      font-size: 0.78rem;
      font-weight: 800;
      color: var(--indigo);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 0.4rem;
    }}

    .callout {{
      background: rgba(15, 23, 42, 0.8);
      border-left: 4px solid var(--cyan);
      padding: 1.2rem 1.5rem;
      border-radius: 6px;
      margin: 1.5rem 0;
      font-size: 0.98rem;
    }}
    .callout-emerald {{ border-left-color: var(--emerald); background: rgba(16, 185, 129, 0.08); }}

    .code-box {{
      background: #090c14;
      border: 1px solid var(--border);
      border-radius: 8px;
      margin: 1.8rem 0;
      overflow: hidden;
    }}
    .code-header {{
      background: #111726;
      padding: 0.65rem 1.2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: 'Fira Code', monospace;
      font-size: 0.82rem;
      color: var(--text-muted);
    }}
    .run-btn {{
      background: var(--cyan);
      color: #000;
      font-weight: 700;
      border: none;
      padding: 0.4rem 0.95rem;
      border-radius: 4px;
      cursor: pointer;
      font-family: 'Fira Code', monospace;
      font-size: 0.8rem;
      transition: all 0.2s;
    }}
    .run-btn:hover {{ background: #0284c7; color: #fff; }}
    .code-area {{
      width: 100%;
      background: transparent;
      border: none;
      color: #e2e8f0;
      font-family: 'Fira Code', monospace;
      font-size: 0.86rem;
      padding: 1.2rem;
      min-height: 280px;
      outline: none;
      resize: vertical;
    }}
    .term-out {{
      background: #040609;
      border-top: 1px solid var(--border);
      padding: 1.1rem;
      font-family: 'Fira Code', monospace;
      font-size: 0.84rem;
      color: var(--emerald);
      display: none;
      white-space: pre-wrap;
    }}
    .term-out.show {{ display: block; }}
    .nav-links {{
      display: flex;
      justify-content: space-between;
      margin-top: 3.5rem;
      padding-top: 1.8rem;
      border-top: 1px solid var(--border);
      font-family: 'Fira Code', monospace;
      font-size: 0.9rem;
    }}
    .nav-links a {{ color: var(--cyan); text-decoration: none; }}
    .nav-links a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>

  <div class="wrapper">
    <div class="chap-badge">Omni-Academy · Master Tutorial · Chapter {mid_str} ({tag})</div>
    <h1>{title}</h1>

    <div class="callout callout-emerald">
      <strong>🎯 What You Will Master in This Chapter:</strong>
{bullets_html}
    </div>

    <h2>{ped_info["hook_title"]}</h2>
    <p>
      {ped_info["hook_text"].replace(chr(10), '</p><p>')}
    </p>

    <div class="analogy-box">
      <div class="analogy-label">{ped_info["analogy_label"]}</div>
      <p style="margin: 0; color: #e2e8f0;">
        {ped_info["analogy_text"].replace(chr(10), '<br>')}
      </p>
    </div>

    <h2>2. The Core Principle: Understanding the Mechanics</h2>
    <p>
      {mod_info["theory"]}
    </p>

    <div class="mnemonic-card">
      <div class="mnemonic-header">⚡ Permanent Mnemonic Anchor</div>
      <div class="mnemonic-title">{ped_info["mnemonic_title"]}</div>
      <div class="mnemonic-rule">"{ped_info["mnemonic_rule"]}"</div>
      <div class="mnemonic-desc">{ped_info["mnemonic_desc"]}</div>
    </div>

    <h2>3. {ped_info["systems_title"]}</h2>
    <p>
      {ped_info["systems_text"]}
    </p>
    <div class="callout">
      <strong>Systems Connection:</strong> {mod_info["systems_tie_in"]}
    </div>

    <h2>4. The Algorithm in Action: Continuing the Story</h2>
    <div class="callout callout-emerald">
      <strong>Connecting the Code to the Story:</strong>
      <p>As you read the algorithm below, remember the <em>{ped_info["analogy_label"].split(':', 1)[-1].strip() if ":" in ped_info.get("analogy_label", "") else ped_info.get("analogy_label", "")}</em> metaphor:</p>
      <ul>
        <li><strong>Variables:</strong> The mathematical variables represent the physical objects from our story (e.g., the actors in our crime scene).</li>
        <li><strong>Loops:</strong> The <code>for</code> and <code>while</code> loops represent the mechanical steps of resolving the problem, advancing the state one step at a time.</li>
        <li><strong>Return Value:</strong> The final result is the resolution of our hook—restoring order to the system.</li>
      </ul>
      <p>Try modifying the inputs in the Pyodide editor below to see how the story changes!</p>
    </div>

    <h2>5. Live WebAssembly Lab: Execute the Python Algorithm</h2>
    <p>
      Experiment with the algorithm live in your browser. Modify parameters, run edge cases, and verify the assertions.
    </p>

    <div class="code-box">
      <div class="code-header">
        <span>PYTHON 3.12 (IN-BROWSER WEBASSEMBLY RUNNER)</span>
        <button class="run-btn" onclick="runLab()">▶ Run Code in Pyodide</button>
      </div>
      <textarea id="lab-code" class="code-area" spellcheck="false">{code}</textarea>
      <div id="lab-out" class="term-out"></div>
    </div>

    <div class="nav-links">
      {prev_link}
      {next_link}
    </div>
  </div>

  <script>
    let pyodideInstance = null;
    async function initPy() {{
      if (!pyodideInstance) {{
        pyodideInstance = await loadPyodide();
      }}
      return pyodideInstance;
    }}

    async function runLab() {{
      const outBox = document.getElementById('lab-out');
      outBox.className = 'term-out show';
      outBox.textContent = '⏳ Initializing Pyodide & executing algorithm...';
      try {{
        const py = await initPy();
        py.runPython(`
import sys
import io
sys_stdout_backup = sys.stdout
sys.stdout = io.StringIO()
`);
        const code = document.getElementById('lab-code').value;
        await py.runPythonAsync(code);
        const stdout = py.runPython("sys.stdout.getvalue()");
        py.runPython("sys.stdout = sys_stdout_backup");
        outBox.textContent = stdout;
      }} catch (err) {{
        outBox.textContent = '❌ Execution Error:\\n' + err;
      }}
    }}
  </script>
</body>
</html>
"""
    return html


def update_existing_nav(chap_num, prev_file, next_file, prev_title, next_title):
    filename = CHAPTER_FILENAMES[chap_num]
    filepath = os.path.join(TEXTBOOK_DIR, filename)
    if not os.path.exists(filepath):
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    prev_link = f'<a href="{prev_file}">← Chapter {chap_num-1:02d}: {prev_title}</a>' if prev_file else '<a href="index.html">← Master Textbook Hub</a>'
    next_link = f'<a href="{next_file}">Next: Chapter {chap_num+1:02d}: {next_title} →</a>' if next_file else '<a href="index.html">🎓 Master Textbook Hub (Course Complete!) →</a>'

    nav_block = f"""    <div class="nav-links">
      {prev_link}
      {next_link}
    </div>"""

    new_content = re.sub(r'<div class="nav-links">.*?</div>', nav_block, content, flags=re.DOTALL)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)


def generate_master_index(all_modules):
    """Generates the master textbook index.html with all 50 chapters organized by 5 Epochs."""
    epoch_names = [
        "Epoch 1: Foundations (NCERT 6 - 10)",
        "Epoch 2: Calculus & Analysis (11 - 12)",
        "Epoch 3: Undergrad CS & Math (BCA / B.Tech)",
        "Epoch 4: Systems & Compilers (MCA)",
        "Epoch 5: PhD / Research-Grade Deep Systems"
    ]

    cards_by_epoch = {i: [] for i in range(5)}
    for i, mod in enumerate(all_modules):
        chap_num = i + 1
        fn = CHAPTER_FILENAMES[chap_num]
        e_idx = min(i // 10, 4)
        active_cls = " active" if chap_num == 1 else ""
        
        # Clean title
        clean_title = mod["title"]
        if ":" in clean_title:
            clean_title = clean_title.split(":", 1)[1].strip()

        desc = mod["theory"][:140] + "..." if len(mod["theory"]) > 140 else mod["theory"]
        
        card_html = f"""        <a class="chap-card{active_cls}" onclick="loadChapter('{fn}', this)">
          <div class="chap-meta"><span>CHAPTER {chap_num:02d}</span><span>{mod['tag'].split('·')[-1].strip().upper()}</span></div>
          <div class="chap-title">{clean_title}</div>
          <div class="chap-desc">{desc}</div>
        </a>"""
        cards_by_epoch[e_idx].append(card_html)

    sidebar_sections = []
    for e_idx in range(5):
        s_title = epoch_names[e_idx]
        cards = "\n".join(cards_by_epoch[e_idx])
        sec = f"""      <!-- {s_title} -->
      <div>
        <div class="sidebar-section-title">{s_title}</div>
{cards}
      </div>"""
        sidebar_sections.append(sec)

    all_sections_html = "\n\n".join(sidebar_sections)

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Omni-Academy · Complete 50-Chapter Master Interactive Textbook</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #07090e;
      --card-bg: #0d121c;
      --card-hover: #131b2e;
      --border: rgba(255, 255, 255, 0.08);
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --cyan: #38bdf8;
      --emerald: #10b981;
      --amber: #f59e0b;
      --rose: #f43f5e;
      --indigo: #6366f1;
      --purple: #a855f7;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: 'Inter', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}
    header {{
      background: rgba(13, 18, 28, 0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 1rem 2rem;
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}
    .brand-icon {{
      width: 32px;
      height: 32px;
      background: linear-gradient(135deg, var(--cyan), var(--indigo));
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 1.1rem;
      color: #000;
    }}
    .brand-title {{
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: -0.01em;
    }}
    .brand-sub {{
      font-size: 0.75rem;
      color: var(--text-muted);
      font-family: 'Fira Code', monospace;
    }}
    .header-nav {{
      display: flex;
      align-items: center;
      gap: 1.2rem;
      font-size: 0.85rem;
      font-family: 'Fira Code', monospace;
    }}
    .header-nav a {{
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .header-nav a:hover, .header-nav a.active {{
      color: var(--cyan);
    }}
    .main-container {{
      display: flex;
      flex: 1;
      height: calc(100vh - 65px);
      overflow: hidden;
    }}
    .sidebar {{
      width: 420px;
      background: #090c14;
      border-right: 1px solid var(--border);
      overflow-y: auto;
      padding: 1.5rem 1.2rem;
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }}
    .sidebar-section-title {{
      font-size: 0.75rem;
      font-family: 'Fira Code', monospace;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 0.6rem;
      border-bottom: 1px solid rgba(56, 189, 248, 0.2);
      padding-bottom: 0.3rem;
    }}
    .chap-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.9rem 1rem;
      cursor: pointer;
      transition: all 0.2s;
      margin-bottom: 0.65rem;
      text-decoration: none;
      display: block;
      color: inherit;
    }}
    .chap-card:hover {{
      background: var(--card-hover);
      border-color: rgba(56, 189, 248, 0.3);
      transform: translateY(-1px);
    }}
    .chap-card.active {{
      border-color: var(--cyan);
      background: rgba(56, 189, 248, 0.08);
    }}
    .chap-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.72rem;
      font-family: 'Fira Code', monospace;
      color: var(--cyan);
      margin-bottom: 0.35rem;
    }}
    .chap-title {{
      font-size: 0.88rem;
      font-weight: 700;
      line-height: 1.35;
      margin-bottom: 0.35rem;
      color: #fff;
    }}
    .chap-desc {{
      font-size: 0.76rem;
      color: var(--text-muted);
      line-height: 1.45;
    }}
    .content-viewer {{
      flex: 1;
      display: flex;
      flex-direction: column;
      background: var(--bg);
      position: relative;
    }}
    .viewer-bar {{
      background: #0b0f19;
      border-bottom: 1px solid var(--border);
      padding: 0.6rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
      font-family: 'Fira Code', monospace;
    }}
    .viewer-title {{
      color: var(--text);
      font-weight: 600;
    }}
    .viewer-actions a {{
      color: var(--cyan);
      text-decoration: none;
      margin-left: 1rem;
    }}
    .viewer-actions a:hover {{
      text-decoration: underline;
    }}
    iframe {{
      width: 100%;
      height: 100%;
      border: none;
      background: var(--bg);
    }}
  </style>
</head>
<body>

  <header>
    <div class="brand">
      <div class="brand-icon">Ω</div>
      <div>
        <div class="brand-title">Omni-Academy Master Textbook</div>
        <div class="brand-sub">NCERT 6th to PhD Systems · Complete 50-Chapter Interactive Curriculum</div>
      </div>
    </div>
    <div class="header-nav">
      <a href="index.html" class="active">📖 Textbook Reader (All 50 Chapters)</a>
      <a href="../index.html">⚡ 50-Module Lab Portal</a>
      <a href="../../academy_v2/site/index.html">🏛️ Academy v2 (135 Modules)</a>
    </div>
  </header>

  <div class="main-container">
    <div class="sidebar">

{all_sections_html}

    </div>

    <div class="content-viewer">
      <div class="viewer-bar">
        <span class="viewer-title" id="active-title">Chapter 01: The Secret Life of Numbers: Counting, Clocks, Primes & Euclid</span>
        <div class="viewer-actions">
          <a id="open-new-tab" href="chapter_01_number_theory.html" target="_blank">↗ Open in Dedicated Window</a>
        </div>
      </div>
      <iframe id="chapter-frame" src="chapter_01_number_theory.html"></iframe>
    </div>
  </div>

  <script>
    function loadChapter(fileName, cardElem) {{
      document.getElementById('chapter-frame').src = fileName;
      document.getElementById('open-new-tab').href = fileName;
      
      const title = cardElem.querySelector('.chap-title').textContent;
      const meta = cardElem.querySelector('.chap-meta span:first-child').textContent;
      document.getElementById('active-title').textContent = `${{meta}}: ${{title}}`;

      document.querySelectorAll('.chap-card').forEach(c => c.classList.remove('active'));
      cardElem.classList.add('active');
    }}
  </script>
</body>
</html>
"""
    with open(os.path.join(TEXTBOOK_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("Successfully updated omni_academy/textbook/index.html with all 50 chapters!")


def main():
    with open(CURRICULUM_DATA, "r", encoding="utf-8") as f:
        text = f.read()
    m = re.search(r'window\.OMNI_MODULES\s*=\s*(\[.*\]);', text, re.DOTALL)
    modules = json.loads(m.group(1))

    print(f"Loaded {len(modules)} modules from curriculum_data.js")

    # Titles helper
    titles = {}
    for i, mod in enumerate(modules):
        chap_num = i + 1
        t = mod["title"]
        if ":" in t:
            t = t.split(":", 1)[1].strip()
        titles[chap_num] = t

    # 1. Generate 36 missing chapters
    generated_count = 0
    for chap_num, ped_info in PEDAGOGY_DATA.items():
        mod_idx = chap_num - 1
        mod_info = modules[mod_idx]
        
        prev_file = CHAPTER_FILENAMES.get(chap_num - 1)
        next_file = CHAPTER_FILENAMES.get(chap_num + 1)
        prev_title = titles.get(chap_num - 1, "")
        next_title = titles.get(chap_num + 1, "")

        html = render_chapter_html(chap_num, mod_info, ped_info, prev_file, next_file, prev_title, next_title)
        out_path = os.path.join(TEXTBOOK_DIR, CHAPTER_FILENAMES[chap_num])
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        generated_count += 1
        print(f"[{chap_num:02d}/50] Generated {CHAPTER_FILENAMES[chap_num]}")

    print(f"\nGenerated all {generated_count} missing chapters!")

    # 2. Update navigation links in ALL 50 chapters so the 1-50 chain is unbroken
    for chap_num in range(1, 51):
        prev_file = CHAPTER_FILENAMES.get(chap_num - 1)
        next_file = CHAPTER_FILENAMES.get(chap_num + 1)
        prev_title = titles.get(chap_num - 1, "")
        next_title = titles.get(chap_num + 1, "")
        update_existing_nav(chap_num, prev_file, next_file, prev_title, next_title)

    print("Updated sequential navigation links (1 <-> 50) across all 50 chapters!")

    # 3. Generate master textbook index.html
    generate_master_index(modules)
    print("\nMaster 50-Chapter Omni-Academy Textbook successfully built!")


if __name__ == "__main__":
    main()
