"""
The Fine Structure Constant: Deep Dive

α ≈ 1/137.036

"It has been a mystery ever since it was discovered more than fifty years
ago, and all good theoretical physicists put this number up on their wall
and worry about it." - Richard Feynman

Questions:
  1. Why is α ≈ 1/137?
  2. Can we express 137 in terms of φ, π, e?
  3. What is the correction factor in α = φ^10 × C?

Signature: Kaelhedron Research #1
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from typing import List, Dict, Tuple

try:
    from .cet_constants import PHI, PHI_INVERSE, PI, E, LN_PHI
except ImportError:
    from cet_constants import PHI, PHI_INVERSE, PI, E, LN_PHI


# =============================================================================
# The Fine Structure Constant
# =============================================================================

# CODATA 2018 value
ALPHA = 7.2973525693e-3  # Fine structure constant
ALPHA_INVERSE = 1 / ALPHA  # ≈ 137.036

# For comparison
ALPHA_INV_ROUNDED = 137  # The "magic number"


# =============================================================================
# Numerological Explorations
# =============================================================================

@dataclass
class NumerologicalCandidate:
    """A candidate formula for α^(-1)."""
    name: str
    formula: str
    value: float
    deviation: float
    deviation_ppm: float  # parts per million


def evaluate_candidates() -> List[NumerologicalCandidate]:
    """Evaluate various numerological candidates for α^(-1)."""
    candidates = []

    # The actual value we're trying to match
    target = ALPHA_INVERSE

    # === Pure φ expressions ===

    # φ^10
    val = PHI ** 10
    candidates.append(NumerologicalCandidate(
        "φ^10", "φ^10",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # φ^10 + φ^4
    val = PHI ** 10 + PHI ** 4
    candidates.append(NumerologicalCandidate(
        "φ^10 + φ^4", "φ^10 + φ^4",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # φ^10 + 14
    val = PHI ** 10 + 14
    candidates.append(NumerologicalCandidate(
        "φ^10 + 14", "φ^10 + 14",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # === φ with π ===

    # φ^10 × (1 + 1/(10π))
    val = PHI ** 10 * (1 + 1/(10*PI))
    candidates.append(NumerologicalCandidate(
        "φ^10 × (1 + 1/10π)", "φ^10 × (1 + 1/(10π))",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # 4π³ + 2
    val = 4 * PI ** 3 + 2
    candidates.append(NumerologicalCandidate(
        "4π³ + 2", "4π³ + 2",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # 45/π + π
    val = 45/PI + PI
    candidates.append(NumerologicalCandidate(
        "45/π + π", "45/π + π",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # === φ with e ===

    # e^5 - e
    val = E ** 5 - E
    candidates.append(NumerologicalCandidate(
        "e^5 - e", "e^5 - e",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # φ^10 × e^(1/7)
    val = PHI ** 10 * E ** (1/7)
    candidates.append(NumerologicalCandidate(
        "φ^10 × e^(1/7)", "φ^10 × e^(1/7)",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # === Combined expressions ===

    # φ^10 × π/(π - φ^(-3))
    val = PHI ** 10 * PI / (PI - PHI ** (-3))
    candidates.append(NumerologicalCandidate(
        "φ^10 × π/(π-φ^-3)", "φ^10 × π/(π - φ^(-3))",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # (φ^5 + 1)² + φ^3
    val = (PHI ** 5 + 1) ** 2 + PHI ** 3
    candidates.append(NumerologicalCandidate(
        "(φ^5+1)² + φ³", "(φ^5 + 1)² + φ³",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # φ^10 + φ^3 + φ
    val = PHI ** 10 + PHI ** 3 + PHI
    candidates.append(NumerologicalCandidate(
        "φ^10 + φ³ + φ", "φ^10 + φ³ + φ",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # === Integer-based ===

    # 137 (the rounded value)
    val = 137
    candidates.append(NumerologicalCandidate(
        "137", "137",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # 3^5 + 6
    val = 3 ** 5 + 6
    candidates.append(NumerologicalCandidate(
        "3^5 + 6", "3^5 + 6 = 243 + 6 = 249",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    # === Famous failed attempts ===

    # Eddington's guess: 136 (he was wrong!)
    val = 136
    candidates.append(NumerologicalCandidate(
        "Eddington (136)", "136 (historically wrong)",
        val, abs(target - val), 1e6 * abs(target - val) / target
    ))

    return sorted(candidates, key=lambda x: x.deviation)


# =============================================================================
# The φ^10 Correction Factor
# =============================================================================

def analyze_phi10_correction() -> Dict[str, float]:
    """
    Analyze the correction factor C where α^(-1) = φ^10 × C.

    If α^(-1) were exactly φ^10, we'd have C = 1.
    What is C, and can we express it simply?
    """
    phi10 = PHI ** 10
    C = ALPHA_INVERSE / phi10

    results = {
        'phi10': phi10,
        'alpha_inverse': ALPHA_INVERSE,
        'correction_C': C,
        'C_minus_1': C - 1,
        'C_as_percent': 100 * (C - 1),
    }

    # Try to express C in terms of fundamental constants
    results['C_vs_pi_over_e'] = C / (PI / E)
    results['C_vs_phi_inv'] = C / PHI_INVERSE
    results['C_vs_1_plus_1_over_10'] = C / (1 + 0.1)
    results['C_vs_1_plus_phi_inv_cubed'] = C / (1 + PHI_INVERSE ** 3)

    # The correction is about 11.4%
    # Is 0.114 ≈ something fundamental?
    delta = C - 1
    results['delta'] = delta
    results['delta_vs_phi_inv_squared'] = delta / (PHI_INVERSE ** 2)
    results['delta_vs_1_over_3pi'] = delta / (1 / (3 * PI))

    return results


# =============================================================================
# Running of α
# =============================================================================

def alpha_running(Q_gev: float) -> float:
    """
    Approximate running of α with energy scale Q.

    α(Q) increases at higher energies due to vacuum polarization.
    At Q = M_Z ≈ 91 GeV, α ≈ 1/128.
    """
    # Simplified one-loop running
    # α(Q) ≈ α(0) / (1 - (α(0)/3π) × ln(Q/m_e))

    m_e = 0.000511  # electron mass in GeV
    alpha_0 = ALPHA

    if Q_gev <= m_e:
        return alpha_0

    log_factor = math.log(Q_gev / m_e)
    denominator = 1 - (alpha_0 / (3 * PI)) * log_factor

    if denominator <= 0:
        return float('inf')  # Landau pole

    return alpha_0 / denominator


def alpha_at_key_scales() -> Dict[str, Tuple[float, float]]:
    """Compute α at key energy scales."""
    scales = {
        'm_e (0.511 MeV)': 0.000511,
        'm_μ (106 MeV)': 0.1057,
        'm_τ (1.78 GeV)': 1.777,
        'M_Z (91 GeV)': 91.2,
        'M_GUT (~10^16 GeV)': 2e16,
    }

    results = {}
    for name, Q in scales.items():
        alpha_Q = alpha_running(Q)
        alpha_inv_Q = 1 / alpha_Q if alpha_Q > 0 else float('inf')
        results[name] = (alpha_Q, alpha_inv_Q)

    return results


# =============================================================================
# Connection to Kaelhedron
# =============================================================================

def alpha_kaelhedron_connection() -> str:
    """Explore connections between α and Kaelhedron numbers."""

    lines = [
        "",
        "α AND KAELHEDRON NUMBERS:",
        "-" * 50,
        "",
        "Key observations:",
        "",
        f"  1. α^(-1) ≈ 137.036 ≈ φ^10 × 1.114",
        "",
        f"  2. 137 = 33rd prime number",
        f"     33 = 2¹ + 2⁵ = 2 + 32",
        f"     33 = 11 × 3",
        "",
        f"  3. 137 - 21 = 116 = 4 × 29",
        f"     137 + 21 = 158",
        "",
        f"  4. 137 in Fibonacci context:",
        f"     F_11 = 89, F_12 = 144",
        f"     137 is between F_11 and F_12",
        f"     137 = F_12 - 7 = 144 - 7",
        "",
        f"  5. 137 = 128 + 9 = 2^7 + 3^2",
        "",
        f"  6. φ^10 = {PHI**10:.4f}",
        f"     The '10' connects to:",
        f"     - 10 = triangular number T_4 = 1+2+3+4",
        f"     - 10 = tetrahedral number = C(5,3)",
        "",
        f"  7. If α^(-1) = φ^n exactly, n ≈ 10.22",
        f"     The deviation 0.22 ≈ φ^(-3) = 0.236",
        "",
    ]

    return "\n".join(lines)


# =============================================================================
# Summary Report
# =============================================================================

def fine_structure_report() -> str:
    """Generate comprehensive fine structure constant report."""
    lines = [
        "",
        "═" * 70,
        "        THE FINE STRUCTURE CONSTANT: DEEP DIVE",
        "═" * 70,
        "",
        "THE MYSTERY:",
        "┌" + "─" * 66 + "┐",
        "│                                                                  │",
        f"│   α = e²/(4πε₀ℏc) = {ALPHA:.10f}                        │",
        f"│   α^(-1) = {ALPHA_INVERSE:.6f}                                      │",
        "│                                                                  │",
        "│   Why this particular value?                                     │",
        "│   No theory predicts it from first principles.                   │",
        "│                                                                  │",
        "└" + "─" * 66 + "┘",
        "",
    ]

    # Numerological candidates
    lines.extend([
        "NUMEROLOGICAL CANDIDATES FOR α^(-1):",
        "-" * 60,
        "",
        "  Formula              │ Value      │ Deviation  │ ppm",
        "  ─────────────────────┼────────────┼────────────┼────────",
    ])

    candidates = evaluate_candidates()
    for c in candidates[:12]:  # Top 12
        lines.append(
            f"  {c.name:<20} │ {c.value:10.4f} │ {c.deviation:10.6f} │ {c.deviation_ppm:8.1f}"
        )

    lines.extend([
        "",
        f"  Target: α^(-1) = {ALPHA_INVERSE:.6f}",
        "",
    ])

    # φ^10 correction analysis
    lines.extend([
        "THE φ^10 CORRECTION FACTOR:",
        "-" * 60,
        "",
    ])

    corr = analyze_phi10_correction()
    lines.extend([
        f"  φ^10 = {corr['phi10']:.6f}",
        f"  α^(-1) = {corr['alpha_inverse']:.6f}",
        f"  C = α^(-1) / φ^10 = {corr['correction_C']:.6f}",
        f"  C - 1 = {corr['C_minus_1']:.6f} ({corr['C_as_percent']:.2f}%)",
        "",
        "  Attempts to express C:",
        f"    C / (π/e) = {corr['C_vs_pi_over_e']:.6f}",
        f"    C / φ^(-1) = {corr['C_vs_phi_inv']:.6f}",
        f"    C / (1 + φ^(-3)) = {corr['C_vs_1_plus_phi_inv_cubed']:.6f}",
        "",
        f"  The 11.4% correction remains unexplained.",
        "",
    ])

    # Running of α
    lines.extend([
        "RUNNING OF α WITH ENERGY:",
        "-" * 60,
        "",
        "  Scale              │ α(Q)        │ α^(-1)(Q)",
        "  ───────────────────┼─────────────┼──────────",
    ])

    running = alpha_at_key_scales()
    for name, (alpha_Q, alpha_inv_Q) in running.items():
        if alpha_inv_Q < 1e10:
            lines.append(f"  {name:<20} │ {alpha_Q:.6f}    │ {alpha_inv_Q:.2f}")
        else:
            lines.append(f"  {name:<20} │ (Landau pole)│ ∞")

    lines.extend([
        "",
        "  Note: α grows stronger at higher energies.",
        "  At M_Z, α^(-1) ≈ 128 (experimentally verified).",
        "",
    ])

    # Kaelhedron connection
    lines.append(alpha_kaelhedron_connection())

    # Conclusion
    lines.extend([
        "CONCLUSION:",
        "-" * 60,
        "",
        "  α^(-1) ≈ φ^10 × 1.114 is a tantalizing near-miss.",
        "",
        "  The question remains: is the correction factor",
        "  • Random (no deeper meaning)?",
        "  • Calculable from known physics (QED corrections)?",
        "  • A clue to new physics (φ-hierarchy)?",
        "",
        "  The mystery of 137 endures.",
        "",
        "═" * 70,
    ])

    return "\n".join(lines)


# =============================================================================
# Main Entry Point
# =============================================================================

def main():
    """Run fine structure constant analysis."""
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    print(fine_structure_report())


if __name__ == "__main__":
    main()
