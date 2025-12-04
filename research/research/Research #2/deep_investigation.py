"""
Deep Investigation - Research #2

Going deeper into all discovered patterns:
1. Why m₂/m₁ ≈ 2 (binary, not φ)?
2. CKM matrix connection
3. Triple corrections for high n
4. Fibonacci in differences
5. Proton double correction
6. Sign patterns
7. E8/Lie algebra connection

Signature: Kaelhedron Research #2
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict
from itertools import combinations

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PHI = (1 + math.sqrt(5)) / 2
PHI_INV = 1 / PHI
LN_PHI = math.log(PHI)
SQRT5 = math.sqrt(5)

# Fibonacci sequence
FIBS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

# Lucas numbers (related to Fibonacci)
LUCAS = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123]


# =============================================================================
# INVESTIGATION 1: Why m₂/m₁ ≈ 2 (Binary Structure)?
# =============================================================================

def investigate_binary_structure():
    """
    The ratio m₂/m₁ ≈ 2 for most double-correction particles.
    Why 2 and not φ?
    """
    print("=" * 75)
    print("  INVESTIGATION 1: Why m₂/m₁ ≈ 2 (Binary Structure)?")
    print("=" * 75)
    print()

    # The observed m₂/m₁ ratios
    particles = [
        ("strange", 3, 6),   # 6/3 = 2.00
        ("muon", 5, 10),     # 10/5 = 2.00
        ("bottom", 3, 7),    # 7/3 = 2.33
        ("W", 4, 9),         # 9/4 = 2.25
        ("Z", 4, 8),         # 8/4 = 2.00
        ("Higgs", 3, 8),     # 8/3 = 2.67
        ("top", 2, 5),       # 5/2 = 2.50
    ]

    print("  Observed m₂/m₁ ratios:")
    print()
    ratios = []
    for name, m1, m2 in particles:
        ratio = m2 / m1
        ratios.append(ratio)
        print(f"    {name:<8}: m₂/m₁ = {m2}/{m1} = {ratio:.3f}")

    avg_ratio = sum(ratios) / len(ratios)
    print()
    print(f"  Average ratio: {avg_ratio:.4f}")
    print()

    # Test various hypotheses for the ratio
    print("  Testing hypotheses for m₂/m₁:")
    print()

    hypotheses = [
        ("2 (binary)", 2.0),
        ("φ (golden)", PHI),
        ("√φ", math.sqrt(PHI)),
        ("φ²/φ = φ", PHI),
        ("1 + φ^(-1)", 1 + PHI_INV),
        ("2φ - 1", 2*PHI - 1),
        ("φ + φ^(-2)", PHI + PHI**-2),
        ("3 - φ^(-1)", 3 - PHI_INV),
        ("e - 1/2", math.e - 0.5),
    ]

    print("  Hypothesis         | Value  | Avg diff from data")
    print("  " + "-" * 50)

    for name, value in hypotheses:
        avg_diff = sum(abs(r - value) for r in ratios) / len(ratios)
        status = "***" if avg_diff < 0.1 else "**" if avg_diff < 0.2 else "*" if avg_diff < 0.3 else ""
        print(f"  {name:<18} | {value:.4f} | {avg_diff:.4f} {status}")

    print()

    # Key insight: Why might 2 appear?
    print("  WHY 2 (BINARY)?")
    print("  " + "-" * 50)
    print()
    print("  Possibility 1: DOUBLING SYMMETRY")
    print("    φ^(-m) and φ^(-2m) are related by squaring")
    print("    If m₂ = 2×m₁, then φ^(-m₂) = (φ^(-m₁))²")
    print("    This is a natural relationship in perturbation theory")
    print()

    # Check if m₂ = 2×m₁ exactly for any particles
    print("  Testing m₂ = 2×m₁ exactly:")
    for name, m1, m2 in particles:
        if m2 == 2 * m1:
            print(f"    {name}: m₂ = 2×m₁ = {m2} ✓")
        else:
            print(f"    {name}: m₂ = {m2}, 2×m₁ = {2*m1} (diff: {m2 - 2*m1})")

    print()
    print("  Possibility 2: BINARY TREE STRUCTURE")
    print("    Quantum corrections branch in binary trees")
    print("    Each level doubles the recursion depth")
    print("    m₂/m₁ ≈ 2 reflects this binary branching")
    print()

    print("  Possibility 3: TWO-LOOP CORRECTIONS")
    print("    m₁ = one-loop correction depth")
    print("    m₂ = two-loop correction depth")
    print("    Two-loop ≈ 2× one-loop in perturbation theory")
    print()

    # Test: Does φ^(-m) + φ^(-2m) appear naturally?
    print("  Testing φ^(-m) + φ^(-2m) pattern:")
    print()
    for name, m1, m2 in particles:
        if m2 == 2 * m1:
            val = PHI**(-m1) + PHI**(-2*m1)
            val_sq = PHI**(-m1) * (1 + PHI**(-m1))
            print(f"    {name}: φ^(-{m1}) + φ^(-{m2}) = {val:.4f}")
            print(f"           = φ^(-{m1}) × (1 + φ^(-{m1})) = {val_sq:.4f}")
    print()


# =============================================================================
# INVESTIGATION 2: CKM Matrix Connection
# =============================================================================

def investigate_ckm_connection():
    """
    Does the CKM matrix structure relate to correction exponents?
    """
    print("=" * 75)
    print("  INVESTIGATION 2: CKM Matrix Connection")
    print("=" * 75)
    print()

    # CKM matrix elements (magnitudes, approximate)
    # |V_ud|  |V_us|  |V_ub|
    # |V_cd|  |V_cs|  |V_cb|
    # |V_td|  |V_ts|  |V_tb|

    CKM = {
        ("u", "d"): 0.974,
        ("u", "s"): 0.225,
        ("u", "b"): 0.004,
        ("c", "d"): 0.225,
        ("c", "s"): 0.973,
        ("c", "b"): 0.041,
        ("t", "d"): 0.009,
        ("t", "s"): 0.040,
        ("t", "b"): 0.999,
    }

    print("  CKM Matrix (magnitudes):")
    print()
    print("         d        s        b")
    print(f"  u   {CKM[('u','d')]:.3f}    {CKM[('u','s')]:.3f}    {CKM[('u','b')]:.3f}")
    print(f"  c   {CKM[('c','d')]:.3f}    {CKM[('c','s')]:.3f}    {CKM[('c','b')]:.3f}")
    print(f"  t   {CKM[('t','d')]:.3f}    {CKM[('t','s')]:.3f}    {CKM[('t','b')]:.3f}")
    print()

    # Express CKM elements as φ-powers
    print("  CKM elements as φ-powers:")
    print()
    print("  Element    | Value  | φ^x     | x")
    print("  " + "-" * 45)

    for (q1, q2), val in CKM.items():
        if val > 0.001:
            power = math.log(val) / LN_PHI
            print(f"  V_{q1}{q2}      | {val:.4f} | φ^{power:+.2f} | {power:.3f}")

    print()

    # Key observation: Cabibbo angle
    print("  CABIBBO ANGLE:")
    print()
    cabibbo = CKM[("u", "s")]
    cabibbo_power = math.log(cabibbo) / LN_PHI
    print(f"  sin(θ_C) = V_us = {cabibbo:.4f}")
    print(f"           = φ^{cabibbo_power:.3f}")
    print()

    # Is Cabibbo related to φ^(-3)?
    print(f"  φ^(-3) = {PHI**-3:.4f}")
    print(f"  Ratio: V_us / φ^(-3) = {cabibbo / PHI**-3:.3f}")
    print()

    # Wolfenstein parameterization
    print("  WOLFENSTEIN PARAMETERS:")
    print()
    lambda_w = cabibbo  # ≈ 0.225
    A = CKM[("c", "b")] / lambda_w**2  # ≈ 0.81
    print(f"  λ = {lambda_w:.4f} (Cabibbo)")
    print(f"  A = {A:.4f}")
    print()

    # Check if λ is a φ-power
    print(f"  λ = φ^{math.log(lambda_w)/LN_PHI:.3f}")
    print(f"  Compare: φ^(-3) = {PHI**-3:.4f}")
    print(f"  Compare: 1/4 = 0.250")
    print()

    # Connection hypothesis
    print("  HYPOTHESIS: CKM-Correction Connection")
    print("  " + "-" * 50)
    print()
    print("  The Cabibbo angle λ ≈ 0.225 ≈ φ^(-3.1)")
    print("  This is close to the m₁ = 3 correction we see in many particles!")
    print()
    print("  Quark mixing strength may determine correction depth:")
    print("    - Strongly mixed quarks (s, b) need double corrections")
    print("    - Weakly mixed quarks (u, d) need single corrections")
    print()

    # Test: Do mixed quarks need more corrections?
    quark_corrections = {
        "up": ("single", 3),
        "down": ("single", 5),
        "strange": ("double", (3, 6)),
        "charm": ("single", 16),
        "bottom": ("double", (3, 7)),
        "top": ("double", (2, 5)),
    }

    print("  Mixing vs Correction Analysis:")
    print()
    print("  Quark   | Off-diagonal CKM | Correction type")
    print("  " + "-" * 50)

    for quark, (corr_type, _) in quark_corrections.items():
        # Find largest off-diagonal CKM element for this quark
        if quark in ["up", "charm", "top"]:
            # Up-type: look at d, s, b columns
            max_off = max(CKM.get((quark[0], q), 0) for q in ["s", "b"])
        else:
            # Down-type: look at c, t rows
            max_off = max(CKM.get((q, quark[0]), 0) for q in ["c", "t"])

        print(f"  {quark:<8} | {max_off:.4f}           | {corr_type}")

    print()


# =============================================================================
# INVESTIGATION 3: Triple Corrections for High n
# =============================================================================

def investigate_triple_corrections():
    """
    Do very high-n particles need triple corrections?
    Test with hypothetical 4th generation and extrapolations.
    """
    print("=" * 75)
    print("  INVESTIGATION 3: Triple Corrections for High n")
    print("=" * 75)
    print()

    # Current pattern
    print("  Current correction pattern by n:")
    print()
    print("  n range  | Typical corrections")
    print("  " + "-" * 40)
    print("  1-10     | Single (c ≈ 1)")
    print("  11-15    | Single or Double (transition)")
    print("  16-26    | Double (two φ^(-m) terms)")
    print("  27+      | Triple? (hypothesis)")
    print()

    # Extrapolate: if pattern continues, n > 27 needs triple
    print("  HYPOTHESIS: Triple corrections for n > 27")
    print()

    # What would require n > 27?
    print("  Particles/ratios that would have n > 27:")
    print()

    M_ELECTRON = 0.000511  # GeV

    hypotheticals = [
        ("4th gen quark (5 TeV)", 5000),
        ("4th gen quark (10 TeV)", 10000),
        ("Heavy Higgs (500 GeV)", 500),
        ("M_Planck/m_e", 1.22e19),
        ("M_GUT/m_e", 2e16),
    ]

    for name, mass_gev in hypotheticals:
        ratio = mass_gev / M_ELECTRON
        n = math.log(ratio) / LN_PHI
        print(f"  {name:<25}: n ≈ {n:.1f}")

    print()

    # Test: Can we find a triple-correction formula for hierarchy?
    print("  TESTING TRIPLE CORRECTION FOR M_Planck/M_Weak:")
    print()

    observed = 4.96e16
    power = math.log(observed) / LN_PHI
    n = 80

    print(f"  Observed: {observed:.2e}")
    print(f"  φ-power: {power:.4f}")
    print(f"  n = {n}")
    print()

    # Try triple corrections
    print("  Testing φ^(80 - φ^(-m₁) - φ^(-m₂) - φ^(-m₃)):")
    print()

    best_triple = None
    best_residual = float('inf')

    for m1 in range(2, 8):
        for m2 in range(m1+1, 10):
            for m3 in range(m2+1, 12):
                for s1 in [-1, 1]:
                    for s2 in [-1, 1]:
                        for s3 in [-1, 1]:
                            correction = s1*PHI**(-m1) + s2*PHI**(-m2) + s3*PHI**(-m3)
                            predicted_power = n + correction
                            predicted = PHI ** predicted_power
                            residual = abs(predicted - observed) / observed

                            if residual < best_residual:
                                best_residual = residual
                                best_triple = (m1, m2, m3, s1, s2, s3, residual)

    if best_triple:
        m1, m2, m3, s1, s2, s3, res = best_triple
        s1_str = "+" if s1 > 0 else "-"
        s2_str = "+" if s2 > 0 else "-"
        s3_str = "+" if s3 > 0 else "-"

        print(f"  Best triple: φ^({n} {s1_str} φ^(-{m1}) {s2_str} φ^(-{m2}) {s3_str} φ^(-{m3}))")
        print(f"  Residual: {res*100:.4f}%")
        print()

        # Compare to double
        # Best double from Research #1: φ^(80 - φ^(-5) - φ^(-7))
        double_pred = PHI ** (80 - PHI**-5 - PHI**-7)
        double_res = abs(double_pred - observed) / observed

        print(f"  Double correction residual: {double_res*100:.4f}%")
        print(f"  Triple correction residual: {res*100:.4f}%")
        print()

        if res < double_res:
            print("  ★ TRIPLE CORRECTION IS BETTER! ★")
        else:
            print("  Double correction is sufficient.")

    print()


# =============================================================================
# INVESTIGATION 4: Fibonacci Pattern in Differences
# =============================================================================

def investigate_fibonacci_differences():
    """
    The differences m₂ - m₁ are {3, 4, 5} — Fibonacci-adjacent.
    Is this significant?
    """
    print("=" * 75)
    print("  INVESTIGATION 4: Fibonacci Pattern in Differences")
    print("=" * 75)
    print()

    particles = [
        ("strange", 3, 6, 3),
        ("muon", 5, 10, 5),
        ("bottom", 3, 7, 4),
        ("W", 4, 9, 5),
        ("Z", 4, 8, 4),
        ("Higgs", 3, 8, 5),
        ("top", 2, 5, 3),
    ]

    differences = [d for _, _, _, d in particles]

    print("  Observed differences (m₂ - m₁):")
    for name, m1, m2, diff in particles:
        fib_mark = "★" if diff in FIBS else ""
        print(f"    {name:<8}: {m2} - {m1} = {diff} {fib_mark}")

    print()
    print(f"  Differences: {differences}")
    print(f"  Unique: {set(differences)}")
    print()

    # Count Fibonacci
    fib_count = sum(1 for d in differences if d in FIBS)
    print(f"  Fibonacci numbers: {fib_count}/{len(differences)}")
    print()

    # The set {3, 4, 5} is interesting
    print("  THE {3, 4, 5} PATTERN:")
    print("  " + "-" * 50)
    print()
    print("  3, 4, 5 form a Pythagorean triple: 3² + 4² = 5²")
    print("  3, 5 are Fibonacci; 4 is between them")
    print()

    # Check if these relate to Fibonacci indices
    print("  As Fibonacci indices:")
    print(f"    F_4 = 3")
    print(f"    F_5 = 5")
    print(f"    4 = F_4 + 1 = F_5 - 1 (between Fibonacci)")
    print()

    # Lucas numbers?
    print("  Connection to Lucas numbers:")
    for d in set(differences):
        lucas_mark = "★" if d in LUCAS else ""
        print(f"    {d} {lucas_mark}")
    print()

    # Hypothesis: differences = F_{k} for some k
    print("  HYPOTHESIS: m₂ - m₁ relates to recursion structure")
    print()
    print("  If corrections come from nested recursion:")
    print("    Level 1: contributes φ^(-m₁)")
    print("    Level 2: contributes φ^(-(m₁ + Δ)) = φ^(-m₂)")
    print("  Then Δ = m₂ - m₁ is the recursion step size")
    print()
    print("  Fibonacci steps are natural for φ-based recursion!")
    print("  F_n × ln(φ) ≈ n for Fibonacci indices")
    print()

    # Test: Is m₂ - m₁ always close to a Fibonacci?
    print("  Distance to nearest Fibonacci:")
    for name, m1, m2, diff in particles:
        min_dist = min(abs(diff - f) for f in FIBS)
        nearest = min(FIBS, key=lambda f: abs(diff - f))
        print(f"    {name:<8}: {diff} → nearest F = {nearest} (dist = {min_dist})")

    print()


# =============================================================================
# INVESTIGATION 5: Proton Double Correction
# =============================================================================

def investigate_proton_correction():
    """
    The proton has n = 16 (at threshold) and 155 ppm discrepancy.
    Should it have double correction?
    """
    print("=" * 75)
    print("  INVESTIGATION 5: Proton Double Correction")
    print("=" * 75)
    print()

    # High precision data
    mp_me_observed = 1836.15267343
    mp_me_single = PHI ** (16 - PHI**-2)  # Current prediction

    print(f"  Observed: {mp_me_observed:.8f}")
    print(f"  Single:   {mp_me_single:.8f} = φ^(16 - φ^(-2))")
    print()

    discrepancy = mp_me_observed - mp_me_single
    ppm = discrepancy / mp_me_observed * 1e6
    print(f"  Discrepancy: {discrepancy:.8f} ({ppm:.1f} ppm)")
    print()

    # The discrepancy is NEGATIVE — prediction is too high
    # Need to SUBTRACT more
    print("  The prediction is TOO HIGH by {:.1f} ppm".format(-ppm))
    print("  Need additional NEGATIVE correction")
    print()

    # Find best double correction
    print("  Testing double correction φ^(16 - φ^(-2) + s×φ^(-k)):")
    print()

    target_power = math.log(mp_me_observed) / LN_PHI
    base_power = 16 - PHI**-2

    print(f"  Target power: {target_power:.8f}")
    print(f"  Base power:   {base_power:.8f}")
    print(f"  Need delta:   {target_power - base_power:.8f}")
    print()

    needed_delta = target_power - base_power  # This is negative

    print("  Finding φ^(-k) that matches:")
    for k in range(3, 15):
        c = needed_delta / (-PHI**-k)  # Negative because we need to subtract
        predicted = PHI ** (base_power - c * PHI**-k)
        error = abs(predicted - mp_me_observed) / mp_me_observed * 1e6

        status = "***" if 0.9 < c < 1.1 else "**" if 0.5 < c < 1.5 else ""
        print(f"    k={k:2d}: c = {c:+.4f}, error = {error:.2f} ppm {status}")

    print()

    # Best formula with c ≈ 1
    print("  REFINED PROTON FORMULA:")
    print()

    # The best k where c ≈ 1
    best_k = None
    best_c_dist = float('inf')
    for k in range(3, 15):
        c = needed_delta / (-PHI**-k)
        if abs(c - 1) < best_c_dist:
            best_c_dist = abs(c - 1)
            best_k = k
            best_c = c

    if best_k:
        refined = PHI ** (16 - PHI**-2 - PHI**-best_k)
        error = abs(refined - mp_me_observed) / mp_me_observed * 1e6

        print(f"  m_p/m_e = φ^(16 - φ^(-2) - φ^(-{best_k}))")
        print(f"         = φ^(16 - {PHI**-2:.4f} - {PHI**-best_k:.4f})")
        print(f"         = φ^({16 - PHI**-2 - PHI**-best_k:.6f})")
        print(f"         = {refined:.6f}")
        print()
        print(f"  Observed:   {mp_me_observed:.6f}")
        print(f"  Error:      {error:.2f} ppm")
        print()

        if error < abs(ppm):
            print(f"  ★ IMPROVEMENT: {abs(ppm):.1f} ppm → {error:.2f} ppm ★")

    print()


# =============================================================================
# INVESTIGATION 6: Sign Patterns in Corrections
# =============================================================================

def investigate_sign_patterns():
    """
    Analyze the pattern of signs in double corrections.
    """
    print("=" * 75)
    print("  INVESTIGATION 6: Sign Patterns in Corrections")
    print("=" * 75)
    print()

    particles = [
        ("strange", 11, 3, 6, -1, +1),   # -φ^(-3) + φ^(-6)
        ("muon", 11, 5, 10, +1, -1),     # +φ^(-5) - φ^(-10)
        ("bottom", 19, 3, 7, -1, -1),    # -φ^(-3) - φ^(-7)
        ("W", 25, 4, 9, -1, +1),         # -φ^(-4) + φ^(-9)
        ("Z", 25, 4, 8, +1, -1),         # +φ^(-4) - φ^(-8)
        ("Higgs", 26, 3, 8, -1, +1),     # -φ^(-3) + φ^(-8)
        ("top", 26, 2, 5, +1, +1),       # +φ^(-2) + φ^(-5)
    ]

    print("  Particle | n  | s₁ | s₂ | Net sign | Pattern")
    print("  " + "-" * 55)

    patterns = {"+-": 0, "-+": 0, "++": 0, "--": 0}
    net_positive = 0
    net_negative = 0

    for name, n, m1, m2, s1, s2 in particles:
        s1_str = "+" if s1 > 0 else "-"
        s2_str = "+" if s2 > 0 else "-"
        pattern = s1_str + s2_str

        # Net contribution (weighted by φ^(-m))
        net = s1 * PHI**(-m1) + s2 * PHI**(-m2)
        net_sign = "+" if net > 0 else "-"

        if net > 0:
            net_positive += 1
        else:
            net_negative += 1

        patterns[pattern] += 1

        print(f"  {name:<8} | {n:2d} | {s1_str}  | {s2_str}  | {net_sign}        | {pattern}")

    print()
    print("  Pattern counts:")
    for p, count in patterns.items():
        print(f"    {p}: {count}")

    print()
    print(f"  Net positive corrections: {net_positive}")
    print(f"  Net negative corrections: {net_negative}")
    print()

    # Is there a pattern related to n?
    print("  Pattern by n (even/odd):")
    for name, n, m1, m2, s1, s2 in particles:
        s1_str = "+" if s1 > 0 else "-"
        s2_str = "+" if s2 > 0 else "-"
        parity = "even" if n % 2 == 0 else "odd"
        print(f"    {name:<8}: n={n} ({parity}), signs = {s1_str}{s2_str}")

    print()

    # Hypothesis: alternating based on m₁ parity?
    print("  Pattern by m₁ (even/odd):")
    for name, n, m1, m2, s1, s2 in particles:
        s1_str = "+" if s1 > 0 else "-"
        parity = "even" if m1 % 2 == 0 else "odd"
        print(f"    {name:<8}: m₁={m1} ({parity}), s₁ = {s1_str}")

    print()

    # Check if s₁ correlates with m₁ parity
    m1_even_s1_pos = sum(1 for _, _, m1, _, s1, _ in particles if m1 % 2 == 0 and s1 > 0)
    m1_odd_s1_pos = sum(1 for _, _, m1, _, s1, _ in particles if m1 % 2 == 1 and s1 > 0)
    m1_even_total = sum(1 for _, _, m1, _, _, _ in particles if m1 % 2 == 0)
    m1_odd_total = sum(1 for _, _, m1, _, _, _ in particles if m1 % 2 == 1)

    print(f"  m₁ even → s₁ positive: {m1_even_s1_pos}/{m1_even_total}")
    print(f"  m₁ odd  → s₁ positive: {m1_odd_s1_pos}/{m1_odd_total}")
    print()


# =============================================================================
# INVESTIGATION 7: E8/Lie Algebra Connection
# =============================================================================

def investigate_e8_connection():
    """
    Connect the correction pattern to E8 and Lie algebra structure.
    """
    print("=" * 75)
    print("  INVESTIGATION 7: E8/Lie Algebra Connection")
    print("=" * 75)
    print()

    # Lie algebra dimensions
    print("  Lie Algebra Dimensions:")
    print()

    algebras = [
        ("so(3)", 3, "rotations in 3D"),
        ("so(5)", 10, "B₂"),
        ("so(7)", 21, "B₃ - Kaelhedron!"),
        ("so(8)", 28, "D₄ - triality"),
        ("G₂", 14, "exceptional"),
        ("F₄", 52, "exceptional"),
        ("E₆", 78, "exceptional"),
        ("E₇", 133, "exceptional"),
        ("E₈", 248, "exceptional"),
    ]

    for name, dim, note in algebras:
        phi_power = math.log(dim) / LN_PHI if dim > 0 else 0
        print(f"    {name:<6}: dim = {dim:3d} = φ^{phi_power:.2f}  ({note})")

    print()

    # The key: 21 appears in corrections
    print("  CONNECTION TO CORRECTIONS:")
    print("  " + "-" * 50)
    print()

    # The m values we see: 2, 3, 4, 5, 6, 7, 8, 9, 10
    m_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("  Correction depths m and their φ^(-m) values:")
    print()
    for m in m_values:
        val = PHI ** (-m)
        # What is this close to in Lie algebra terms?
        print(f"    m={m}: φ^(-{m}) = {val:.4f}")

    print()

    # so(7) has dimension 21 = 7×6/2
    # The 7 points of the Fano plane
    print("  THE FANO PLANE CONNECTION:")
    print()
    print("  Fano plane: 7 points, 7 lines, 3 points per line")
    print("  so(7) dimension: 21 = C(7,2) = number of edges")
    print()
    print("  Correction depths m ∈ {2,3,4,5,6,7,8,9,10}")
    print("  Range: 2 to 10, span of 8")
    print("  7 + 1 = 8 (E₈ rank)")
    print()

    # The sum m₁ + m₂ values
    particles = [
        ("strange", 3, 6),
        ("muon", 5, 10),
        ("bottom", 3, 7),
        ("W", 4, 9),
        ("Z", 4, 8),
        ("Higgs", 3, 8),
        ("top", 2, 5),
    ]

    sums = [m1 + m2 for _, m1, m2 in particles]
    print(f"  Sums m₁ + m₂: {sums}")
    print()

    # Check against Lie algebra dimensions
    print("  Matching sums to structures:")
    for name, m1, m2 in particles:
        total = m1 + m2
        # Check if total matches any special number
        matches = []
        if total == 7:
            matches.append("Fano points")
        if total == 8:
            matches.append("E₈ rank")
        if total in FIBS:
            matches.append(f"F_{FIBS.index(total)+1}")
        if total == 21:
            matches.append("so(7) dim")

        match_str = ", ".join(matches) if matches else "-"
        print(f"    {name:<8}: m₁+m₂ = {total:2d}  {match_str}")

    print()

    # E8 decomposition
    print("  E₈ DECOMPOSITION:")
    print()
    print("  E₈ (248) = so(16) (120) + spinor (128)")
    print("  Or: E₈ = 8 + 56 + 56 + 128 (under maximal subgroup)")
    print()
    print("  Standard Model content in E₈: ~45 generators")
    print("  Hidden sector: 248 - 45 = 203")
    print()

    # φ^(-m) contributions sum
    print("  Total correction contribution:")
    total_correction = sum(PHI**(-m1) + PHI**(-m2) for _, m1, m2 in particles)
    print(f"  Σ (φ^(-m₁) + φ^(-m₂)) = {total_correction:.4f}")
    print(f"  As φ-power: φ^{math.log(total_correction)/LN_PHI:.2f}")
    print()


# =============================================================================
# INVESTIGATION 8: The Complete Picture
# =============================================================================

def synthesize_findings():
    """
    Bring all findings together into a coherent picture.
    """
    print("=" * 75)
    print("  SYNTHESIS: The Complete Picture")
    print("=" * 75)
    print()

    print("  THE EMERGING STRUCTURE:")
    print("  " + "-" * 50)
    print()
    print("  1. BASE: All mass ratios are φ^n for integer n")
    print("     This comes from self-reference (∃R)")
    print()
    print("  2. FIRST CORRECTION: φ^(n ± φ^(-m₁))")
    print("     Quantum corrections perturb the base")
    print("     m₁ relates to loop order / recursion depth")
    print()
    print("  3. SECOND CORRECTION: φ^(n ± φ^(-m₁) ± φ^(-m₂))")
    print("     Higher-n particles accumulate more corrections")
    print("     m₂ ≈ 2×m₁ (binary doubling)")
    print()
    print("  4. THRESHOLD: n ≈ 15")
    print("     Below: single correction sufficient")
    print("     Above: double correction needed")
    print("     (Proton at n=16 is borderline)")
    print()
    print("  5. PATTERN IN DIFFERENCES: m₂ - m₁ ∈ {3, 4, 5}")
    print("     These are Fibonacci-adjacent")
    print("     Pythagorean triple: 3² + 4² = 5²")
    print()
    print("  6. GENERATION STRUCTURE:")
    print("     Gen 1: no double corrections")
    print("     Gen 2: 1/2 double")
    print("     Gen 3: 2/2 double")
    print("     Heavier generations accumulate corrections")
    print()

    print("  THE PHYSICAL PICTURE:")
    print("  " + "-" * 50)
    print()
    print("  • Particle masses emerge from φ-structured vacuum")
    print("  • Quantum loops add corrections at each recursion level")
    print("  • Deep recursion (high n) → multiple correction sources")
    print("  • Binary structure (m₂ ≈ 2m₁) suggests doubling mechanism")
    print("  • Fibonacci differences link to φ's continued fraction")
    print()

    print("  REMAINING MYSTERIES:")
    print("  " + "-" * 50)
    print()
    print("  • Why exactly 2 (not φ) for the m₂/m₁ ratio?")
    print("  • What determines the signs (+/-)?")
    print("  • Why {3,4,5} specifically for differences?")
    print("  • Connection to CKM matrix still unclear")
    print("  • E8 connection needs more development")
    print()


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("\n" * 2)
    print("=" * 75)
    print("       DEEP INVESTIGATION - RESEARCH #2")
    print("=" * 75)
    print()

    investigate_binary_structure()
    print()

    investigate_ckm_connection()
    print()

    investigate_triple_corrections()
    print()

    investigate_fibonacci_differences()
    print()

    investigate_proton_correction()
    print()

    investigate_sign_patterns()
    print()

    investigate_e8_connection()
    print()

    synthesize_findings()

    print("=" * 75)
    print("       DEEP INVESTIGATION COMPLETE")
    print("=" * 75)


if __name__ == "__main__":
    main()
