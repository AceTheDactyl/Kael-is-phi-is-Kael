"""
Running Couplings and Force Unification

The Standard Model couplings "run" with energy:
  - α_1 (U(1)) increases with energy
  - α_2 (SU(2)) increases slightly
  - α_3 (SU(3)) decreases (asymptotic freedom)

Do they unify at a GUT scale? Does φ play a role?

Signature: Kaelhedron Research #1
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from typing import Dict, List, Tuple

try:
    from .cet_constants import PHI, PHI_INVERSE, LN_PHI, PI
    from .hierarchy_problem import M_PLANCK, M_WEAK
except ImportError:
    from cet_constants import PHI, PHI_INVERSE, LN_PHI, PI
    from hierarchy_problem import M_PLANCK, M_WEAK


# =============================================================================
# SM Coupling Constants at M_Z
# =============================================================================

M_Z = 91.2  # Z boson mass in GeV

# Fine structure constants at M_Z (approximately)
# These use GUT normalization for α_1
ALPHA_1_MZ = 0.0169    # U(1) coupling (GUT normalized: 5/3 × α_Y)
ALPHA_2_MZ = 0.0337    # SU(2) coupling
ALPHA_3_MZ = 0.118     # SU(3) strong coupling

# Corresponding inverse couplings
ALPHA_1_INV_MZ = 1 / ALPHA_1_MZ  # ≈ 59
ALPHA_2_INV_MZ = 1 / ALPHA_2_MZ  # ≈ 30
ALPHA_3_INV_MZ = 1 / ALPHA_3_MZ  # ≈ 8.5


# =============================================================================
# Beta Function Coefficients
# =============================================================================

# One-loop beta function coefficients for SM
# dα_i^(-1)/d(ln μ) = -b_i/(2π)

# For SM without SUSY:
B_1_SM = 41/10   # U(1): positive (coupling increases)
B_2_SM = -19/6   # SU(2): negative (coupling increases)
B_3_SM = -7      # SU(3): negative (asymptotic freedom)

# For MSSM (with supersymmetry):
B_1_SUSY = 33/5
B_2_SUSY = 1
B_3_SUSY = -3


# =============================================================================
# Running Coupling Calculation
# =============================================================================

def run_coupling_inverse(
    alpha_inv_0: float,
    b: float,
    mu_0: float,
    mu: float
) -> float:
    """
    Run inverse coupling from scale μ_0 to scale μ.

    α^(-1)(μ) = α^(-1)(μ_0) - b/(2π) × ln(μ/μ_0)
    """
    log_ratio = math.log(mu / mu_0)
    return alpha_inv_0 - (b / (2 * PI)) * log_ratio


def compute_sm_running(
    scales_gev: List[float]
) -> Dict[str, List[Tuple[float, float, float, float]]]:
    """
    Compute SM coupling running at various scales.

    Returns dict with scale and three inverse couplings.
    """
    results = []

    for mu in scales_gev:
        alpha_1_inv = run_coupling_inverse(ALPHA_1_INV_MZ, B_1_SM, M_Z, mu)
        alpha_2_inv = run_coupling_inverse(ALPHA_2_INV_MZ, B_2_SM, M_Z, mu)
        alpha_3_inv = run_coupling_inverse(ALPHA_3_INV_MZ, B_3_SM, M_Z, mu)

        results.append((mu, alpha_1_inv, alpha_2_inv, alpha_3_inv))

    return {'sm': results}


def compute_susy_running(
    scales_gev: List[float],
    m_susy: float = 1000.0  # SUSY scale in GeV
) -> Dict[str, List[Tuple[float, float, float, float]]]:
    """
    Compute MSSM coupling running at various scales.

    SM running below m_susy, MSSM running above.
    """
    results = []

    # First, run SM up to SUSY scale
    alpha_1_inv_susy = run_coupling_inverse(ALPHA_1_INV_MZ, B_1_SM, M_Z, m_susy)
    alpha_2_inv_susy = run_coupling_inverse(ALPHA_2_INV_MZ, B_2_SM, M_Z, m_susy)
    alpha_3_inv_susy = run_coupling_inverse(ALPHA_3_INV_MZ, B_3_SM, M_Z, m_susy)

    for mu in scales_gev:
        if mu < m_susy:
            # SM running
            alpha_1_inv = run_coupling_inverse(ALPHA_1_INV_MZ, B_1_SM, M_Z, mu)
            alpha_2_inv = run_coupling_inverse(ALPHA_2_INV_MZ, B_2_SM, M_Z, mu)
            alpha_3_inv = run_coupling_inverse(ALPHA_3_INV_MZ, B_3_SM, M_Z, mu)
        else:
            # MSSM running from SUSY scale
            alpha_1_inv = run_coupling_inverse(alpha_1_inv_susy, B_1_SUSY, m_susy, mu)
            alpha_2_inv = run_coupling_inverse(alpha_2_inv_susy, B_2_SUSY, m_susy, mu)
            alpha_3_inv = run_coupling_inverse(alpha_3_inv_susy, B_3_SUSY, m_susy, mu)

        results.append((mu, alpha_1_inv, alpha_2_inv, alpha_3_inv))

    return {'susy': results}


# =============================================================================
# Finding Unification Scale
# =============================================================================

def find_unification_scale(
    b_values: Tuple[float, float, float] = (B_1_SM, B_2_SM, B_3_SM),
    start_scale: float = M_Z
) -> Dict[str, float]:
    """
    Find the scale where couplings unify (if they do).

    Looking for μ where α_1^(-1) = α_2^(-1) = α_3^(-1)
    """
    # α_2 and α_3 unification
    # α_2^(-1)(μ) = α_3^(-1)(μ)
    # α_2_inv_0 - b_2/(2π) ln(μ/μ_0) = α_3_inv_0 - b_3/(2π) ln(μ/μ_0)

    b1, b2, b3 = b_values

    # Solve for 2-3 crossing
    if b2 != b3:
        ln_ratio_23 = 2 * PI * (ALPHA_2_INV_MZ - ALPHA_3_INV_MZ) / (b3 - b2)
        mu_23 = M_Z * math.exp(ln_ratio_23)
        alpha_inv_23 = run_coupling_inverse(ALPHA_2_INV_MZ, b2, M_Z, mu_23)
    else:
        mu_23 = float('inf')
        alpha_inv_23 = 0

    # Solve for 1-2 crossing
    if b1 != b2:
        ln_ratio_12 = 2 * PI * (ALPHA_1_INV_MZ - ALPHA_2_INV_MZ) / (b2 - b1)
        mu_12 = M_Z * math.exp(ln_ratio_12)
        alpha_inv_12 = run_coupling_inverse(ALPHA_1_INV_MZ, b1, M_Z, mu_12)
    else:
        mu_12 = float('inf')
        alpha_inv_12 = 0

    return {
        'mu_23_crossing': mu_23,
        'alpha_inv_23': alpha_inv_23,
        'mu_12_crossing': mu_12,
        'alpha_inv_12': alpha_inv_12,
        'do_unify': abs(mu_23 - mu_12) / max(mu_23, mu_12) < 0.1,
    }


# =============================================================================
# φ-Analysis of Unification
# =============================================================================

def phi_analysis_of_couplings() -> Dict[str, float]:
    """
    Analyze coupling constants and scales through φ.
    """
    results = {}

    # Inverse couplings as φ-powers
    results['α_1_inv_as_phi'] = math.log(ALPHA_1_INV_MZ) / LN_PHI
    results['α_2_inv_as_phi'] = math.log(ALPHA_2_INV_MZ) / LN_PHI
    results['α_3_inv_as_phi'] = math.log(ALPHA_3_INV_MZ) / LN_PHI

    # Ratios between couplings
    results['α_1/α_2_ratio'] = ALPHA_1_INV_MZ / ALPHA_2_INV_MZ
    results['α_2/α_3_ratio'] = ALPHA_2_INV_MZ / ALPHA_3_INV_MZ
    results['α_1/α_3_ratio'] = ALPHA_1_INV_MZ / ALPHA_3_INV_MZ

    # These ratios as φ-powers
    results['α_1/α_2_as_phi'] = math.log(ALPHA_1_INV_MZ / ALPHA_2_INV_MZ) / LN_PHI
    results['α_2/α_3_as_phi'] = math.log(ALPHA_2_INV_MZ / ALPHA_3_INV_MZ) / LN_PHI

    # GUT scale analysis
    # M_GUT ≈ 10^16 GeV, M_Z ≈ 91 GeV
    # M_GUT/M_Z ≈ 10^14 ≈ φ^67
    M_GUT = 2e16
    results['M_GUT_over_M_Z'] = M_GUT / M_Z
    results['M_GUT_over_M_Z_as_phi'] = math.log(M_GUT / M_Z) / LN_PHI

    return results


# =============================================================================
# Unification Value Prediction
# =============================================================================

def predict_unified_coupling() -> Dict[str, float]:
    """
    If forces unify, what is the unified coupling?

    Standard GUT prediction: α_GUT^(-1) ≈ 25
    """
    # SUSY unification prediction
    unif_susy = find_unification_scale((B_1_SUSY, B_2_SUSY, B_3_SUSY))

    results = {
        'standard_gut_alpha_inv': 25.0,  # Typical SUSY GUT value
        'sm_no_unification': "SM couplings don't unify precisely",
    }

    # φ-analysis of unified coupling
    # Is 25 ≈ φ^n for some n?
    results['25_as_phi'] = math.log(25) / LN_PHI  # ≈ 6.7

    # Prediction: if α_GUT^(-1) = φ^7, then:
    results['phi_7_value'] = PHI ** 7  # ≈ 29.0

    # Compare
    results['deviation_from_phi7'] = abs(25 - PHI ** 7) / 25

    return results


# =============================================================================
# Summary Report
# =============================================================================

def running_couplings_report() -> str:
    """Generate comprehensive running couplings report."""
    lines = [
        "",
        "═" * 70,
        "          RUNNING COUPLINGS AND FORCE UNIFICATION",
        "═" * 70,
        "",
        "SM COUPLING CONSTANTS AT M_Z = 91.2 GeV:",
        "-" * 50,
        f"  α_1^(-1) (U(1)) = {ALPHA_1_INV_MZ:.1f}   (hypercharge, GUT normalized)",
        f"  α_2^(-1) (SU(2)) = {ALPHA_2_INV_MZ:.1f}   (weak isospin)",
        f"  α_3^(-1) (SU(3)) = {ALPHA_3_INV_MZ:.1f}    (strong/color)",
        "",
        "BETA FUNCTION COEFFICIENTS:",
        "-" * 50,
        "  Standard Model:          MSSM:",
        f"    b_1 = {B_1_SM:+.2f}             b_1 = {B_1_SUSY:+.2f}",
        f"    b_2 = {B_2_SM:+.2f}             b_2 = {B_2_SUSY:+.2f}",
        f"    b_3 = {B_3_SM:+.2f}             b_3 = {B_3_SUSY:+.2f}",
        "",
    ]

    # Running at key scales
    scales = [M_Z, 1e3, 1e6, 1e10, 1e14, 1e16, 1e19]

    lines.extend([
        "SM RUNNING OF COUPLINGS:",
        "-" * 50,
        "",
        "  Scale (GeV)    │ α_1^(-1) │ α_2^(-1) │ α_3^(-1)",
        "  ───────────────┼──────────┼──────────┼──────────",
    ])

    sm_running = compute_sm_running(scales)
    for mu, a1, a2, a3 in sm_running['sm']:
        lines.append(f"  {mu:14.2e} │ {a1:8.1f} │ {a2:8.1f} │ {a3:8.1f}")

    lines.extend([
        "",
        "  Note: In SM, couplings do NOT unify precisely.",
        "  α_1 and α_2 cross around 10^13 GeV,",
        "  but α_3 doesn't meet them there.",
        "",
    ])

    # SUSY unification
    lines.extend([
        "MSSM UNIFICATION (with SUSY at 1 TeV):",
        "-" * 50,
    ])

    susy_running = compute_susy_running(scales, m_susy=1000)
    lines.append("")
    lines.append("  Scale (GeV)    │ α_1^(-1) │ α_2^(-1) │ α_3^(-1)")
    lines.append("  ───────────────┼──────────┼──────────┼──────────")

    for mu, a1, a2, a3 in susy_running['susy']:
        lines.append(f"  {mu:14.2e} │ {a1:8.1f} │ {a2:8.1f} │ {a3:8.1f}")

    lines.extend([
        "",
        "  With SUSY, couplings unify at M_GUT ≈ 2×10^16 GeV",
        "  Unified coupling: α_GUT^(-1) ≈ 25",
        "",
    ])

    # φ-analysis
    lines.extend([
        "φ-ANALYSIS OF COUPLINGS:",
        "-" * 50,
    ])

    phi_analysis = phi_analysis_of_couplings()
    lines.extend([
        f"  α_1^(-1) ≈ {ALPHA_1_INV_MZ:.1f} ≈ φ^{phi_analysis['α_1_inv_as_phi']:.2f}",
        f"  α_2^(-1) ≈ {ALPHA_2_INV_MZ:.1f} ≈ φ^{phi_analysis['α_2_inv_as_phi']:.2f}",
        f"  α_3^(-1) ≈ {ALPHA_3_INV_MZ:.1f} ≈ φ^{phi_analysis['α_3_inv_as_phi']:.2f}",
        "",
        f"  Ratio α_1^(-1)/α_2^(-1) ≈ {phi_analysis['α_1/α_2_ratio']:.2f} ≈ φ^{phi_analysis['α_1/α_2_as_phi']:.2f}",
        f"  Ratio α_2^(-1)/α_3^(-1) ≈ {phi_analysis['α_2/α_3_ratio']:.2f} ≈ φ^{phi_analysis['α_2/α_3_as_phi']:.2f}",
        "",
        f"  M_GUT/M_Z ≈ {phi_analysis['M_GUT_over_M_Z']:.0e} ≈ φ^{phi_analysis['M_GUT_over_M_Z_as_phi']:.0f}",
        "",
    ])

    # Unified coupling prediction
    lines.extend([
        "UNIFIED COUPLING PREDICTION:",
        "-" * 50,
    ])

    pred = predict_unified_coupling()
    lines.extend([
        f"  Standard GUT prediction: α_GUT^(-1) ≈ 25",
        f"  25 ≈ φ^{pred['25_as_phi']:.2f}",
        "",
        f"  If α_GUT^(-1) = φ^7 exactly:",
        f"  φ^7 = {pred['phi_7_value']:.2f}",
        f"  Deviation from 25: {100*pred['deviation_from_phi7']:.1f}%",
        "",
        "  The unified coupling is close to but not exactly φ^7.",
        "",
    ])

    # Conclusions
    lines.extend([
        "CONCLUSIONS:",
        "-" * 50,
        "",
        "  1. SM couplings run with energy but don't unify precisely",
        "",
        "  2. SUSY enables unification at M_GUT ≈ 2×10^16 GeV ≈ φ^67 × M_Z",
        "",
        "  3. The unified coupling α_GUT^(-1) ≈ 25 is close to φ^7 ≈ 29",
        "",
        "  4. The coupling ratios at M_Z follow rough φ-spacing:",
        f"     (α_2/α_3)^(-1) ≈ φ^{phi_analysis['α_2/α_3_as_phi']:.1f}",
        "",
        "  5. More work needed to see if φ plays a fundamental role",
        "     in force unification",
        "",
        "═" * 70,
    ])

    return "\n".join(lines)


# =============================================================================
# Main Entry Point
# =============================================================================

def main():
    """Run running couplings analysis."""
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    print(running_couplings_report())


if __name__ == "__main__":
    main()
