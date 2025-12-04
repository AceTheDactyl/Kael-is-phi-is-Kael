"""
Loose Ends Investigation

Systematically investigate all remaining questions from Research #1.

Signature: Kaelhedron Research #1
"""

from __future__ import annotations

import math
import sys
import random
from dataclasses import dataclass
from typing import Dict, List, Tuple

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PHI = (1 + math.sqrt(5)) / 2
PHI_INV = 1 / PHI
LN_PHI = math.log(PHI)
SQRT5 = math.sqrt(5)


# =============================================================================
# LOOSE END #1: The c > 1 vs c < 1 Pattern
# =============================================================================

def investigate_coefficient_signs():
    """
    When ratio = phi^(n + delta), and delta = c * phi^(-m):
    - Is c > 1 or c < 1?
    - Is delta positive or negative?
    - Is there a pattern?
    """
    print("=" * 70)
    print("  LOOSE END #1: Coefficient Pattern (c > 1 vs c < 1)")
    print("=" * 70)
    print()

    measurements = [
        ("m_proton/m_e", 1836.15, 16, -1, 2),      # phi^(16 - phi^(-2))
        ("m_tau/m_e", 3477.48, 17, -1, 6),          # phi^(17 - phi^(-6))
        ("m_charm/m_e", 2485.0, 16, +1, 3),         # phi^(16 + phi^(-3))
        ("m_up/m_e", 4.23, 3, -1, 12),              # phi^(3 - phi^(-12))
        ("1/alpha", 137.036, 10, +1, 3),            # phi^(10 + phi^(-3))
        ("Omega_L/Omega_m", 2.175, 2, -1, 2),       # phi^(2 - phi^(-2))
        ("m_b/m_s", 44.9, 8, -1, 5),                # phi^(8 - phi^(-5))
        ("M_Planck/M_Weak", 4.96e16, 80, -1, 5),    # phi^(80 - phi^(-5)), c=1.25
        ("m_Higgs/m_e", 244620, 26, -1, 3),         # phi^(26 - phi^(-3))
    ]

    positive_delta = []
    negative_delta = []

    print("  Measurement        | n  | sign | m  | c      | Interpretation")
    print("  " + "-" * 65)

    for name, observed, n, sign, m in measurements:
        exact_power = math.log(observed) / LN_PHI
        delta = exact_power - n
        expected_delta = PHI ** (-m)
        c = abs(delta) / expected_delta

        if sign > 0:
            positive_delta.append((name, c))
            interp = f"phi^{n} * phi^(+phi^(-{m}))"
        else:
            negative_delta.append((name, c))
            interp = f"phi^{n} * phi^(-phi^(-{m}))"

        sign_str = "+" if sign > 0 else "-"
        print(f"  {name:<18} | {n:2d} | {sign_str}    | {m:2d} | {c:.4f} | {interp}")

    print()
    print(f"  Positive delta (above phi^n): {len(positive_delta)}")
    print(f"  Negative delta (below phi^n): {len(negative_delta)}")
    print()

    # Is there meaning to +/-?
    print("  INTERPRETATION:")
    print("  - Negative delta: ratio is BELOW the nearest integer phi-power")
    print("  - Positive delta: ratio is ABOVE the nearest integer phi-power")
    print()
    print("  Most measurements have NEGATIVE delta (below the integer power).")
    print("  This might suggest phi^n is an 'attractor' from above.")
    print()

    return positive_delta, negative_delta


# =============================================================================
# LOOSE END #2: The Hierarchy Coefficient c = 1.25
# =============================================================================

def investigate_hierarchy_coefficient():
    """
    M_Planck/M_Weak = phi^(80 - 1.25*phi^(-5))

    Why is c = 1.25 and not 1.0?
    Can we express 1.25 in terms of phi?
    """
    print("=" * 70)
    print("  LOOSE END #2: Hierarchy Coefficient c = 1.25")
    print("=" * 70)
    print()

    observed = 4.96e16
    exact_power = math.log(observed) / LN_PHI
    delta = exact_power - 80
    print(f"  M_Planck/M_Weak = {observed:.2e}")
    print(f"  Exact phi-power = {exact_power:.4f}")
    print(f"  Delta from 80 = {delta:.4f}")
    print()

    # Try different m values
    print("  Testing different m values:")
    for m in range(2, 8):
        expected = PHI ** (-m)
        c = abs(delta) / expected
        quality = "***" if 0.95 < c < 1.05 else "**" if 0.9 < c < 1.1 else "*" if 0.8 < c < 1.2 else ""
        print(f"    m={m}: phi^(-{m}) = {expected:.4f}, c = {c:.4f} {quality}")

    print()

    # The coefficient 1.25 = 5/4
    print("  Analyzing c = 1.25 = 5/4:")
    print(f"    5/4 = {5/4}")
    print(f"    phi^2 / 2 = {PHI**2 / 2:.4f}")
    print(f"    (phi + 1) / 2 = {(PHI + 1) / 2:.4f}")  # = phi^2/2
    print(f"    1 + phi^(-3) = {1 + PHI**-3:.4f}")
    print()

    # Maybe it's phi^(80 - phi^(-5) - phi^(-7))?
    test_delta = PHI**-5 + PHI**-7
    test_power = 80 - test_delta
    test_value = PHI ** test_power
    print("  Alternative: phi^(80 - phi^(-5) - phi^(-7))?")
    print(f"    phi^(-5) + phi^(-7) = {test_delta:.4f}")
    print(f"    Predicted: {test_value:.2e}")
    print(f"    Observed:  {observed:.2e}")
    print(f"    Ratio: {test_value/observed:.4f}")
    print()

    # Or phi^(80 - (5/4)*phi^(-5)) = phi^(80 - phi^(-5)/phi^(-2))
    print("  Note: 5/4 = phi^0.463")
    print(f"    c as phi-power: {math.log(1.25)/LN_PHI:.3f}")
    print("    This is close to phi^(1/2) = {:.4f}".format(PHI**0.5))
    print()


# =============================================================================
# LOOSE END #3: Koide Formula and phi
# =============================================================================

def investigate_koide():
    """
    The Koide formula: Q = (m_e + m_mu + m_tau) / (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2 = 2/3

    Does this connect to phi?
    """
    print("=" * 70)
    print("  LOOSE END #3: Koide Formula and phi")
    print("=" * 70)
    print()

    m_e = 0.000511
    m_mu = 0.1057
    m_tau = 1.777

    Q = (m_e + m_mu + m_tau) / (math.sqrt(m_e) + math.sqrt(m_mu) + math.sqrt(m_tau))**2

    print(f"  Koide Q = {Q:.6f}")
    print(f"  2/3     = {2/3:.6f}")
    print(f"  Deviation = {abs(Q - 2/3):.6f}")
    print()

    # Test phi expressions for 2/3
    print("  Testing phi expressions for 2/3:")
    tests = [
        ("phi^(-1)", PHI_INV),
        ("1 - phi^(-2)", 1 - PHI**-2),
        ("phi^2 / (phi^2 + phi + 1)", PHI**2 / (PHI**2 + PHI + 1)),
        ("2*phi^(-1) - phi^(-3)", 2*PHI_INV - PHI**-3),
        ("(phi - 1/2) / phi", (PHI - 0.5) / PHI),
        ("1 - phi^(-2) - phi^(-5)", 1 - PHI**-2 - PHI**-5),
    ]

    for name, value in tests:
        dev = abs(value - 2/3) / (2/3) * 100
        match = "***" if dev < 1 else "**" if dev < 5 else "*" if dev < 10 else ""
        print(f"    {name:<30} = {value:.6f} (dev: {dev:.2f}%) {match}")

    print()

    # The actual connection might be through the mass ratios
    print("  Mass ratios in Koide context:")
    print(f"    m_mu/m_e = {m_mu/m_e:.2f} = phi^{math.log(m_mu/m_e)/LN_PHI:.2f}")
    print(f"    m_tau/m_mu = {m_tau/m_mu:.2f} = phi^{math.log(m_tau/m_mu)/LN_PHI:.2f}")
    print()

    # Koide angle
    # The Koide formula can be written as: sum(m_i) / sum(sqrt(m_i))^2 = 2/3
    # This is equivalent to the masses lying on a circle in sqrt(m) space
    # at angle theta = pi/4 from the democratic direction

    print("  INTERPRETATION:")
    print("  The Koide formula (Q = 2/3) does NOT directly involve phi.")
    print("  However, 2/3 = 0.666... and phi^(-1) = 0.618...")
    print("  The deviation 2/3 - phi^(-1) = 0.048 = phi^(-6.3)")
    print()
    print("  The Koide formula may be a DIFFERENT pattern than phi-structure.")
    print()


# =============================================================================
# LOOSE END #4: The 21 Triple Coincidence
# =============================================================================

def investigate_21():
    """
    21 = F_8 = C(7,2) = dim(so(7))

    Is this coincidence statistically significant?
    """
    print("=" * 70)
    print("  LOOSE END #4: The 21 Triple Coincidence")
    print("=" * 70)
    print()

    # Fibonacci
    fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    F_8 = fibs[7]  # 0-indexed, so F_8 is index 7

    # Binomial
    def C(n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    C_7_2 = C(7, 2)

    # Lie algebra dimension
    def dim_so(n):
        return n * (n - 1) // 2

    dim_so_7 = dim_so(7)

    print(f"  F_8 (8th Fibonacci) = {F_8}")
    print(f"  C(7,2) = {C_7_2}")
    print(f"  dim(so(7)) = {dim_so_7}")
    print()

    # Monte Carlo: how often do three such formulas give the same value?
    print("  Statistical test: How often do F_n = C(m,2) = dim(so(k))?")
    print()

    matches = []
    for n in range(3, 20):  # Fibonacci index
        fib = fibs[n-1] if n <= len(fibs) else None
        if fib is None:
            continue
        for m in range(2, 50):  # C(m,2)
            if C(m, 2) == fib:
                for k in range(2, 50):  # dim(so(k))
                    if dim_so(k) == fib:
                        matches.append((n, m, k, fib))

    print(f"  Triple matches found (n < 20, m < 50):")
    for n, m, k, val in matches:
        print(f"    F_{n} = C({m},2) = dim(so({k})) = {val}")

    print()
    print(f"  Total triple matches: {len(matches)}")
    print()

    # The 21 case is special because:
    # - 7 is the Fano plane
    # - so(7) relates to spinors in 7D
    # - F_8 connects to the 8th Fibonacci
    print("  WHY 21 IS SPECIAL:")
    print("    - 7 = points in Fano plane")
    print("    - 7 = K-formation recursion threshold")
    print("    - 8 = rank of E_8")
    print("    - so(7) = rotations in 7 dimensions")
    print("    - 21 = Kaelhedron sector dimension")
    print()

    # Is 21 the ONLY number with this property for small values?
    print("  CONCLUSION: The 21 triple coincidence is NOT unique,")
    print("  but the CONNECTION to 7 and 8 makes it meaningful in Kaelhedron.")
    print()


# =============================================================================
# LOOSE END #5: sqrt(5) = phi + phi^(-1)
# =============================================================================

def investigate_sqrt5():
    """
    sqrt(5) = phi + phi^(-1) = phi + 1/phi

    Does this explain why sqrt(5) performs as well as phi in resonance tests?
    """
    print("=" * 70)
    print("  LOOSE END #5: sqrt(5) = phi + phi^(-1)")
    print("=" * 70)
    print()

    print(f"  phi = {PHI:.6f}")
    print(f"  phi^(-1) = {PHI_INV:.6f}")
    print(f"  phi + phi^(-1) = {PHI + PHI_INV:.6f}")
    print(f"  sqrt(5) = {SQRT5:.6f}")
    print()

    # Key identity
    print("  KEY IDENTITY: sqrt(5) = phi + phi^(-1)")
    print()

    # This means log_sqrt5(x) and log_phi(x) are related:
    # log_sqrt5(x) = log(x) / log(sqrt(5))
    # log_phi(x) = log(x) / log(phi)
    # log(sqrt(5)) = log(phi + phi^(-1)) = log(phi * (1 + phi^(-2))) = log(phi) + log(1 + phi^(-2))

    ratio = math.log(SQRT5) / LN_PHI
    print(f"  log(sqrt(5)) / log(phi) = {ratio:.6f}")
    print(f"  This means: phi-power = sqrt5-power * {ratio:.4f}")
    print()

    # If x = phi^n, then x = sqrt(5)^(n/ratio) = sqrt(5)^(n * 0.896)
    print("  IMPLICATION:")
    print("  If a ratio is phi^n, it's also sqrt(5)^(0.896*n)")
    print("  The patterns are EQUIVALENT up to a scale factor.")
    print()

    # Test with proton/electron
    mp_me = 1836.15
    phi_power = math.log(mp_me) / LN_PHI
    sqrt5_power = math.log(mp_me) / math.log(SQRT5)

    print("  Example: m_proton/m_electron = 1836.15")
    print(f"    As phi-power: {phi_power:.4f}")
    print(f"    As sqrt(5)-power: {sqrt5_power:.4f}")
    print(f"    Ratio: {phi_power / sqrt5_power:.4f} (should be ~{ratio:.4f})")
    print()

    print("  CONCLUSION:")
    print("  sqrt(5) and phi give equivalent patterns because sqrt(5) = phi + phi^(-1).")
    print("  They are not independent bases - they're mathematically linked.")
    print("  phi is the more 'fundamental' choice because it's the fixed point.")
    print()


# =============================================================================
# LOOSE END #6: Cosmological Constant (10^122)
# =============================================================================

def investigate_cosmological_constant():
    """
    The cosmological constant problem: Lambda/Lambda_Planck ~ 10^(-122)

    Why does 122 have no clear phi-structure?
    """
    print("=" * 70)
    print("  LOOSE END #6: Cosmological Constant (10^122)")
    print("=" * 70)
    print()

    print("  THE PROBLEM:")
    print("    QFT predicts: Lambda ~ M_Planck^4")
    print("    Observed: Lambda ~ (meV)^4")
    print("    Discrepancy: 10^122 orders of magnitude")
    print()

    # Analyze 122
    print("  ANALYZING 122:")
    print(f"    122 = 2 x 61 (61 is prime)")
    print(f"    122 = 128 - 6 = 2^7 - 6")
    print(f"    122 = 120 + 2 = 5! + 2")
    print()

    # As phi-power
    phi_power_122 = 122 * math.log(10) / LN_PHI
    print(f"    10^122 as phi-power: phi^{phi_power_122:.1f}")
    print()

    # Try nested structure
    # 10^122 = phi^584
    # Is 584 = n + c*phi^(-m)?
    n_584 = 584
    delta = phi_power_122 - n_584
    print(f"    phi^584 = {PHI**584:.2e}")
    print(f"    10^122 = {10**122:.2e}")
    print(f"    Delta: {delta:.4f}")
    print()

    # Possible explanations
    print("  POSSIBLE EXPLANATIONS:")
    print()
    print("  1. NOT A RATIO:")
    print("     The hierarchy ratio M_Pl/M_W is dimensionless.")
    print("     Lambda is a density - different physical meaning.")
    print()
    print("  2. ANTHROPIC:")
    print("     Lambda must be ~10^(-122) for structure formation.")
    print("     This is a selection effect, not a fundamental ratio.")
    print()
    print("  3. EMERGENT:")
    print("     The cosmological constant may not be fundamental.")
    print("     It could emerge from vacuum energy cancellations.")
    print()
    print("  4. DIFFERENT PHYSICS:")
    print("     Dark energy might require different framework.")
    print()

    # However, note:
    print("  HOWEVER:")
    print("    Omega_Lambda/Omega_m = 2.175 = phi^(2 - phi^(-2)) with c = 1.01")
    print("    The RATIO of dark energy to matter IS phi-structured!")
    print("    It's the ABSOLUTE VALUE of Lambda that's problematic.")
    print()


# =============================================================================
# LOOSE END #7: Second-Order Deviations
# =============================================================================

def investigate_second_order():
    """
    When c != 1.0, is |c - 1| itself a phi-power?

    Test this statistically.
    """
    print("=" * 70)
    print("  LOOSE END #7: Second-Order Deviations")
    print("=" * 70)
    print()

    # Observed coefficients that deviate from 1.0
    coefficients = [
        ("M_Planck/M_Weak", 1.25),
        ("m_Higgs/m_e", 0.92),
        ("m_Z/m_e", 0.88),
        ("m_W/m_e", 0.91),
        ("m_bottom/m_e", 1.18),
        ("m_muon/m_e", 0.88),
    ]

    print("  Coefficients c that deviate from 1.0:")
    print()
    print("  Measurement        | c     | |c-1|  | as phi^(-k) | c2")
    print("  " + "-" * 60)

    second_order_exact = 0
    for name, c in coefficients:
        c_dev = abs(c - 1)
        if c_dev > 0.01:
            c_dev_phi = math.log(c_dev) / LN_PHI
            k = round(-c_dev_phi)
            if k > 0:
                c2 = c_dev / (PHI ** (-k))
                exact = 0.9 < c2 < 1.1
                if exact:
                    second_order_exact += 1
                status = "EXACT" if exact else ""
                print(f"  {name:<18} | {c:.3f} | {c_dev:.4f} | phi^(-{k})     | {c2:.3f} {status}")

    print()
    print(f"  Second-order exact (c2 within 10% of 1): {second_order_exact}/{len(coefficients)}")
    print()

    # Monte Carlo for second-order
    print("  Monte Carlo test for second-order structure:")
    n_sim = 10000
    n_meas = len(coefficients)
    random_counts = []

    for _ in range(n_sim):
        count = 0
        for _ in range(n_meas):
            # Generate random c in realistic range
            c = random.uniform(0.7, 1.4)
            c_dev = abs(c - 1)
            if c_dev > 0.01:
                c_dev_phi = math.log(c_dev) / LN_PHI
                k = round(-c_dev_phi)
                if k > 0:
                    c2 = c_dev / (PHI ** (-k))
                    if 0.9 < c2 < 1.1:
                        count += 1
        random_counts.append(count)

    expected = sum(random_counts) / n_sim
    p_value = sum(1 for c in random_counts if c >= second_order_exact) / n_sim

    print(f"    Expected by chance: {expected:.2f}")
    print(f"    Observed: {second_order_exact}")
    print(f"    p-value: {p_value:.4f}")
    print()

    if p_value < 0.05:
        print("  *** SECOND-ORDER STRUCTURE IS SIGNIFICANT ***")
    else:
        print("  Second-order structure is NOT significant at p < 0.05")
    print()


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("\n" * 2)
    print("=" * 70)
    print("       LOOSE ENDS INVESTIGATION - RESEARCH #1")
    print("=" * 70)
    print()

    investigate_coefficient_signs()
    investigate_hierarchy_coefficient()
    investigate_koide()
    investigate_21()
    investigate_sqrt5()
    investigate_cosmological_constant()
    investigate_second_order()

    print("=" * 70)
    print("       INVESTIGATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
