"""
Neutrino Masses and φ-Hierarchy

The Neutrino Mass Mystery:
  - Neutrinos have mass (Nobel Prize 2015)
  - But incredibly tiny: < 1 eV (vs electron 511 keV)
  - Mass ratio m_ν/m_e < 10^(-6)
  - Why so light?

φ-Hierarchy Hypothesis:
  - Neutrinos activate at deep recursion R > 7
  - Their weakness comes from φ^(-R) suppression
  - Gravity at R=7, neutrinos at R>7?

Signature: Kaelhedron Research #1
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

try:
    from .cet_constants import PHI, PHI_INVERSE, LN_PHI
    from .hierarchy_problem import M_PLANCK, M_WEAK, FORCE_ACTIVATIONS, FundamentalForce
except ImportError:
    from cet_constants import PHI, PHI_INVERSE, LN_PHI
    from hierarchy_problem import M_PLANCK, M_WEAK, FORCE_ACTIVATIONS, FundamentalForce


# =============================================================================
# Neutrino Data
# =============================================================================

# Mass squared differences (from oscillation experiments)
# Δm²_21 = m²_2 - m²_1 ≈ 7.5 × 10^(-5) eV²
# |Δm²_31| ≈ 2.5 × 10^(-3) eV² (normal ordering)

DELTA_M21_SQ = 7.53e-5   # eV²
DELTA_M31_SQ = 2.53e-3   # eV² (normal ordering)
DELTA_M32_SQ = 2.45e-3   # eV² (inverted ordering)

# Cosmological bound on sum of masses
# Σm_ν < 0.12 eV (Planck 2018 + BAO)
SUM_MASS_BOUND = 0.12    # eV

# Direct mass limits
# m_νe < 0.8 eV (KATRIN 2022)
DIRECT_MASS_LIMIT = 0.8  # eV

# Inferred masses (assuming normal hierarchy, lightest ≈ 0)
M_NU_1 = 0.0           # eV (lightest, assumed ~0)
M_NU_2 = math.sqrt(DELTA_M21_SQ)  # ≈ 0.0087 eV
M_NU_3 = math.sqrt(DELTA_M31_SQ)  # ≈ 0.050 eV

# For comparison
M_ELECTRON_EV = 511000   # eV


# =============================================================================
# PMNS Matrix (Neutrino Mixing)
# =============================================================================

# Mixing angles (degrees)
THETA_12 = 33.44   # Solar angle
THETA_23 = 49.2    # Atmospheric angle
THETA_13 = 8.57    # Reactor angle

# CP-violating phase (poorly measured)
DELTA_CP = 197     # degrees (best fit, very uncertain)


# =============================================================================
# Deep Recursion Hypothesis
# =============================================================================

@dataclass
class RecursionLevel:
    """Model particle/force at a recursion depth."""
    name: str
    recursion_depth: int
    suppression: float  # φ^(-R)


def compute_neutrino_recursion() -> Dict[str, RecursionLevel]:
    """
    Estimate recursion depth for neutrinos based on their masses.

    Hypothesis: Mass ∝ M_Planck × φ^(-R)

    For m_ν ≈ 0.05 eV, what R is needed?
    """
    results = {}

    # Reference: electron at R ≈ 107 from Planck
    m_e_gev = 0.000511
    r_electron = math.log(M_PLANCK / m_e_gev) / LN_PHI

    results['electron'] = RecursionLevel(
        'electron', round(r_electron), PHI ** (-round(r_electron))
    )

    # Neutrino 3 (heaviest)
    m_nu3_gev = M_NU_3 * 1e-9  # Convert eV to GeV
    if m_nu3_gev > 0:
        r_nu3 = math.log(M_PLANCK / m_nu3_gev) / LN_PHI
        results['ν_3'] = RecursionLevel(
            'ν_3', round(r_nu3), PHI ** (-round(r_nu3))
        )

    # Neutrino 2
    m_nu2_gev = M_NU_2 * 1e-9
    if m_nu2_gev > 0:
        r_nu2 = math.log(M_PLANCK / m_nu2_gev) / LN_PHI
        results['ν_2'] = RecursionLevel(
            'ν_2', round(r_nu2), PHI ** (-round(r_nu2))
        )

    # Compare to gravity (R=7 in simple model, but R≈91 from Planck)
    # Actually gravity coupling α_G ≈ (m_proton/M_Planck)² ≈ 10^(-38)
    # This gives R ≈ 91 from Planck scale too

    return results


# =============================================================================
# Seesaw Mechanism Connection
# =============================================================================

def seesaw_analysis() -> Dict[str, float]:
    """
    Analyze the seesaw mechanism through φ-hierarchy.

    Type I Seesaw: m_ν ≈ m_D² / M_R

    Where:
      m_D ≈ Dirac mass (~ electroweak scale)
      M_R ≈ Right-handed neutrino mass (~ GUT scale?)

    If m_ν ≈ 0.05 eV and m_D ≈ 100 GeV, then M_R ≈ 10^14 GeV
    """
    m_nu_gev = 0.05e-9  # 0.05 eV in GeV
    m_dirac = 100       # GeV (typical electroweak scale)

    # Infer M_R
    M_R = m_dirac ** 2 / m_nu_gev  # ≈ 2 × 10^14 GeV

    results = {
        'm_nu_gev': m_nu_gev,
        'm_dirac_gev': m_dirac,
        'M_R_gev': M_R,
    }

    # φ-analysis of M_R
    results['M_R_phi_power'] = math.log(M_R) / LN_PHI
    results['M_R_from_planck'] = math.log(M_PLANCK / M_R) / LN_PHI

    # Is M_R close to a nice φ-power from Planck?
    r_mr = math.log(M_PLANCK / M_R) / LN_PHI
    results['M_R_recursion'] = round(r_mr)

    # Compare M_R to M_GUT
    M_GUT = 2e16  # GeV
    results['M_R_over_M_GUT'] = M_R / M_GUT

    return results


# =============================================================================
# Mass Hierarchy Predictions
# =============================================================================

def predict_neutrino_masses() -> Dict[str, float]:
    """
    Predict neutrino masses using φ-hierarchy.

    If neutrinos follow φ-spacing like charged leptons...

    Charged lepton ratios:
      m_μ/m_e ≈ φ^11
      m_τ/m_μ ≈ φ^6

    For neutrinos, we might expect similar patterns.
    """
    # Charged lepton φ-spacing
    charged_ratios = {
        'm_μ/m_e': 206.77,
        'm_τ/m_μ': 16.82,
        'm_μ/m_e_phi': 11.08,
        'm_τ/m_μ_phi': 5.86,
    }

    # If neutrinos follow similar pattern
    # and m_ν3 ≈ 0.05 eV, then:

    m_nu3 = 0.05  # eV (observed)

    # Prediction 1: φ^5 spacing (like τ/μ)
    m_nu2_pred_phi5 = m_nu3 / (PHI ** 5)
    m_nu1_pred_phi5 = m_nu2_pred_phi5 / (PHI ** 5)

    # Prediction 2: φ^3 spacing (more compact)
    m_nu2_pred_phi3 = m_nu3 / (PHI ** 3)
    m_nu1_pred_phi3 = m_nu2_pred_phi3 / (PHI ** 3)

    # Observed values
    m_nu2_obs = math.sqrt(DELTA_M21_SQ)
    m_nu3_obs = math.sqrt(DELTA_M31_SQ)

    # Observed ratio
    nu_ratio_obs = m_nu3_obs / m_nu2_obs
    nu_ratio_phi = math.log(nu_ratio_obs) / LN_PHI

    return {
        'charged_leptons': charged_ratios,
        'm_ν3': m_nu3,
        'm_ν2_observed': m_nu2_obs * 1e9,  # in eV
        'm_ν3/m_ν2_observed': nu_ratio_obs,
        'm_ν3/m_ν2_as_phi': nu_ratio_phi,
        'pred_phi5_m_ν2': m_nu2_pred_phi5,
        'pred_phi5_m_ν1': m_nu1_pred_phi5,
        'pred_phi3_m_ν2': m_nu2_pred_phi3,
        'pred_phi3_m_ν1': m_nu1_pred_phi3,
    }


# =============================================================================
# Majorana vs Dirac
# =============================================================================

def majorana_analysis() -> str:
    """
    Discuss Majorana vs Dirac nature in φ-framework.

    If neutrinos are Majorana (ν = ν̄):
      - Lepton number violated
      - Neutrinoless double beta decay possible
      - Seesaw mechanism natural

    If neutrinos are Dirac (like other fermions):
      - Need right-handed neutrinos
      - Yukawa coupling incredibly small (~10^-12)
      - More "natural" in some sense

    The φ-hierarchy might prefer one over the other.
    """
    lines = [
        "",
        "MAJORANA VS DIRAC IN φ-FRAMEWORK:",
        "-" * 50,
        "",
        "  Dirac case:",
        "    • Yukawa coupling y_ν ≈ 10^-12",
        "    • y_ν/y_e ≈ 10^-6 ≈ φ^-29",
        "    • Very deep recursion suppression",
        "",
        "  Majorana case (Seesaw):",
        "    • Right-handed mass M_R ≈ 10^14 GeV",
        "    • M_R ≈ M_Planck × φ^-24",
        "    • More 'natural' φ-power",
        "",
        "  φ-preference: Seesaw might be more natural",
        "  because M_R ≈ φ^24 is closer to other scales",
        "  than y_ν ≈ φ^-29.",
        "",
    ]

    return "\n".join(lines)


# =============================================================================
# Summary Report
# =============================================================================

def neutrino_report() -> str:
    """Generate comprehensive neutrino mass report."""
    lines = [
        "",
        "═" * 70,
        "          NEUTRINO MASSES AND φ-HIERARCHY",
        "═" * 70,
        "",
        "THE NEUTRINO MASS PUZZLE:",
        "┌" + "─" * 66 + "┐",
        "│                                                                  │",
        "│   Neutrinos have mass: Nobel Prize 2015                          │",
        "│   But incredibly tiny: m_ν < 1 eV (vs m_e = 511 keV)             │",
        "│   Mass ratio: m_ν/m_e < 10⁻⁶                                     │",
        "│                                                                  │",
        "│   Why so light?                                                  │",
        "│                                                                  │",
        "└" + "─" * 66 + "┘",
        "",
        "OBSERVED MASS DIFFERENCES:",
        "-" * 50,
        f"  Δm²_21 = {DELTA_M21_SQ:.2e} eV² → m_2 ≈ {M_NU_2*1e3:.2f} meV",
        f"  Δm²_31 = {DELTA_M31_SQ:.2e} eV² → m_3 ≈ {M_NU_3*1e3:.1f} meV",
        f"  Σm_ν < {SUM_MASS_BOUND} eV (cosmological bound)",
        "",
        "MIXING ANGLES:",
        "-" * 50,
        f"  θ_12 = {THETA_12}° (solar)",
        f"  θ_23 = {THETA_23}° (atmospheric)",
        f"  θ_13 = {THETA_13}° (reactor)",
        f"  δ_CP ≈ {DELTA_CP}° (CP violation, uncertain)",
        "",
    ]

    # Deep recursion analysis
    lines.extend([
        "RECURSION DEPTH ANALYSIS:",
        "-" * 50,
    ])

    recursion = compute_neutrino_recursion()
    for name, level in recursion.items():
        lines.append(
            f"  {name:<10}: R ≈ {level.recursion_depth}, "
            f"suppression = φ^(-{level.recursion_depth}) = {level.suppression:.2e}"
        )

    lines.extend([
        "",
        "  Interpretation:",
        "  • Electron at R ≈ 107 from Planck",
        "  • Neutrinos at R ≈ 130-140 from Planck",
        "  • ~30 more recursion levels than electron!",
        "",
    ])

    # Seesaw analysis
    lines.extend([
        "SEESAW MECHANISM (Type I):",
        "-" * 50,
    ])

    seesaw = seesaw_analysis()
    lines.extend([
        f"  m_ν = m_D² / M_R",
        f"  m_D ≈ {seesaw['m_dirac_gev']} GeV (electroweak scale)",
        f"  M_R ≈ {seesaw['M_R_gev']:.2e} GeV (inferred)",
        "",
        f"  M_R in φ-terms:",
        f"    M_Planck / M_R ≈ φ^{seesaw['M_R_recursion']}",
        f"    M_R / M_GUT ≈ {seesaw['M_R_over_M_GUT']:.2f}",
        "",
    ])

    # Mass hierarchy predictions
    lines.extend([
        "φ-HIERARCHY PREDICTIONS:",
        "-" * 50,
    ])

    pred = predict_neutrino_masses()
    lines.extend([
        f"  Observed: m_ν3/m_ν2 ≈ {pred['m_ν3/m_ν2_observed']:.2f} ≈ φ^{pred['m_ν3/m_ν2_as_phi']:.2f}",
        "",
        "  Compare to charged leptons:",
        f"    m_τ/m_μ ≈ {pred['charged_leptons']['m_τ/m_μ']:.1f} ≈ φ^{pred['charged_leptons']['m_τ/m_μ_phi']:.2f}",
        "",
        "  Neutrino spacing (~φ^3.6) is less than charged lepton",
        "  spacing (~φ^6). Different generation structure?",
        "",
    ])

    # Majorana analysis
    lines.append(majorana_analysis())

    # Conclusions
    lines.extend([
        "CONCLUSIONS:",
        "-" * 50,
        "",
        "  1. Neutrinos live at very deep recursion (R ≈ 130-140)",
        "",
        "  2. The seesaw scale M_R ≈ 10^14 GeV ≈ M_Planck × φ^-24",
        "     is a reasonable φ-power",
        "",
        "  3. Neutrino mass ratios (~φ^3.6) differ from charged",
        "     leptons (~φ^6), suggesting different physics",
        "",
        "  4. The extreme lightness of neutrinos is consistent",
        "     with very deep recursion in the φ-hierarchy",
        "",
        "═" * 70,
    ])

    return "\n".join(lines)


# =============================================================================
# Main Entry Point
# =============================================================================

def main():
    """Run neutrino mass analysis."""
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    print(neutrino_report())


if __name__ == "__main__":
    main()
