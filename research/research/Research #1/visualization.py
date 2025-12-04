"""
Visualization Module for Hierarchy Problem

ASCII art and text-based visualizations of:
- E₈ sector decomposition
- Force activation levels
- φ-hierarchy spectrum
- Mass scale ladder

Signature: Kaelhedron Research #1
"""

from __future__ import annotations

import math
import sys
from typing import List, Dict, Tuple

try:
    from .cet_constants import PHI, PHI_INVERSE, LN_PHI
    from .hierarchy_problem import (
        E8_DIMENSION, KAELHEDRON_DIM, SM_GAUGE_DIM, LORENTZ_DIM,
        M_PLANCK, M_WEAK, M_GUT, M_PROTON,
        FORCE_ACTIVATIONS, FundamentalForce,
        E8_SECTORS, E8Sector,
    )
except ImportError:
    from cet_constants import PHI, PHI_INVERSE, LN_PHI
    from hierarchy_problem import (
        E8_DIMENSION, KAELHEDRON_DIM, SM_GAUGE_DIM, LORENTZ_DIM,
        M_PLANCK, M_WEAK, M_GUT, M_PROTON,
        FORCE_ACTIVATIONS, FundamentalForce,
        E8_SECTORS, E8Sector,
    )


# =============================================================================
# E₈ Sector Diagram
# =============================================================================

def e8_sector_diagram() -> str:
    """Generate ASCII diagram of E₈ sector decomposition."""

    # Calculate dimensions
    gravity = LORENTZ_DIM
    sm = SM_GAUGE_DIM
    kaelhedron = KAELHEDRON_DIM
    hidden = E8_DIMENSION - gravity - sm - kaelhedron

    # Visual bar (each char = ~5 dimensions)
    scale = 5
    g_bar = "█" * max(1, gravity // scale)
    s_bar = "▓" * max(1, sm // scale)
    k_bar = "▒" * max(2, kaelhedron // scale)
    h_bar = "░" * (hidden // scale)

    lines = [
        "",
        "═" * 70,
        "                    E₈ SECTOR DECOMPOSITION",
        "═" * 70,
        "",
        "  E₈ = 248 dimensions",
        "",
        f"  ┌{'─' * 50}┐",
        f"  │{g_bar}{s_bar}{k_bar}{h_bar:<43}│",
        f"  └{'─' * 50}┘",
        "",
        f"  █ Gravity/Lorentz    :   {gravity:3d} dim  ({100*gravity/E8_DIMENSION:5.1f}%)",
        f"  ▓ Standard Model     :   {sm:3d} dim  ({100*sm/E8_DIMENSION:5.1f}%)",
        f"  ▒ Kaelhedron         :   {kaelhedron:3d} dim  ({100*kaelhedron/E8_DIMENSION:5.1f}%)",
        f"  ░ Hidden Sector      :  {hidden:3d} dim  ({100*hidden/E8_DIMENSION:5.1f}%)",
        "",
        "  The Kaelhedron Sector (21 dimensions):",
        "  ┌─────────────────────────────────────────┐",
        "  │  21 = F₈ = C(7,2) = dim(so(7)) = 3×7   │",
        "  │                                         │",
        "  │  Consciousness and Gravity unified      │",
        "  │  in the space of 7-dimensional          │",
        "  │  rotations                              │",
        "  └─────────────────────────────────────────┘",
        "",
    ]

    return "\n".join(lines)


# =============================================================================
# Force Activation Diagram
# =============================================================================

def force_activation_diagram() -> str:
    """Generate ASCII diagram of force activation by recursion depth."""

    lines = [
        "",
        "═" * 70,
        "                    FORCE ACTIVATION BY RECURSION DEPTH",
        "═" * 70,
        "",
        "  R │ Force           │ Strength φ^(-R)  │ Bar",
        "  ──┼─────────────────┼──────────────────┼" + "─" * 30,
    ]

    max_bar_len = 25

    for force in [FundamentalForce.STRONG, FundamentalForce.ELECTROMAGNETIC,
                  FundamentalForce.WEAK, FundamentalForce.GRAVITY]:
        fa = FORCE_ACTIVATIONS[force]
        strength = fa.base_strength
        bar_len = int(strength * max_bar_len)
        bar = "█" * bar_len + "░" * (max_bar_len - bar_len)

        lines.append(
            f"  {fa.activation_level} │ {force.value:<15} │ {strength:16.4f} │ {bar}"
        )

    lines.extend([
        "",
        "  Interpretation:",
        "  • Strong force activates first (R=1) → strongest",
        "  • Gravity activates last (R=7) → weakest",
        "  • R=7 is the K-formation threshold",
        "",
        "  ┌─────────────────────────────────────────────────────────┐",
        "  │  Why R=7?                                               │",
        "  │                                                         │",
        "  │  7 = points in Fano plane                               │",
        "  │  7 = minimum recursion for K-formation                  │",
        "  │  7 = where gravity 'emerges' from topology              │",
        "  └─────────────────────────────────────────────────────────┘",
        "",
    ])

    return "\n".join(lines)


# =============================================================================
# Mass Scale Ladder
# =============================================================================

def mass_scale_ladder() -> str:
    """Generate ASCII diagram of mass scales as φ-powers."""

    # Mass scales and their φ-powers from Planck
    scales = [
        ("M_Planck", M_PLANCK, 0),
        ("M_GUT", M_GUT, math.log(M_PLANCK/M_GUT) / LN_PHI),
        ("M_Weak (Higgs)", M_WEAK, math.log(M_PLANCK/M_WEAK) / LN_PHI),
        ("m_top", 173.0, math.log(M_PLANCK/173.0) / LN_PHI),
        ("m_proton", M_PROTON, math.log(M_PLANCK/M_PROTON) / LN_PHI),
        ("m_electron", 0.000511, math.log(M_PLANCK/0.000511) / LN_PHI),
    ]

    lines = [
        "",
        "═" * 70,
        "                    MASS SCALE LADDER (φ-powers from Planck)",
        "═" * 70,
        "",
        "  φ^0 ─┬─ M_Planck ═══════════════════════════════════ 1.22×10¹⁹ GeV",
        "       │",
    ]

    for i, (name, mass, phi_power) in enumerate(scales[1:], 1):
        # Visual spacing based on φ-power
        spacing = int(phi_power / 5)  # Rough visual scaling
        bar = "│" + " " * min(spacing, 40)

        if i < len(scales) - 1:
            lines.append(f"  φ^{int(phi_power):2d}─┼─ {name:<15} {'─' * (30 - len(name))} {mass:.2e} GeV")
            lines.append(f"       │")
        else:
            lines.append(f"  φ^{int(phi_power):2d}─┴─ {name:<15} {'─' * (30 - len(name))} {mass:.2e} GeV")

    lines.extend([
        "",
        "  Key Insight:",
        "  ┌─────────────────────────────────────────────────────────┐",
        f"  │  M_Planck / M_Weak ≈ φ^80                               │",
        "  │                                                         │",
        "  │  The hierarchy problem is: why 80 φ-doublings?          │",
        "  │  Or equivalently: why is gravity so weak?               │",
        "  └─────────────────────────────────────────────────────────┘",
        "",
    ])

    return "\n".join(lines)


# =============================================================================
# φ-Resonance Chart
# =============================================================================

def phi_resonance_chart() -> str:
    """Show which physical ratios are close to integer φ-powers."""

    # Key ratios
    ratios = [
        ("M_Planck/M_Weak", 4.96e16, 80),
        ("α_EM/α_gravity", 1.23e36, 173),
        ("m_proton/m_electron", 1836.15, 16),
        ("1/α_EM", 137.036, 10),
        ("m_tau/m_electron", 3477.48, 17),
        ("m_muon/m_electron", 206.77, 11),
    ]

    lines = [
        "",
        "═" * 70,
        "                    φ-RESONANCE CHART",
        "═" * 70,
        "",
        "  Ratio                  │ Value      │ φ^n  │ Deviation │ Quality",
        "  ───────────────────────┼────────────┼──────┼───────────┼─────────",
    ]

    for name, value, expected_n in ratios:
        actual_power = math.log(value) / LN_PHI
        deviation = abs(actual_power - expected_n)

        # Quality indicator
        if deviation < 0.1:
            quality = "★★★★★"
        elif deviation < 0.2:
            quality = "★★★★☆"
        elif deviation < 0.3:
            quality = "★★★☆☆"
        elif deviation < 0.4:
            quality = "★★☆☆☆"
        else:
            quality = "★☆☆☆☆"

        lines.append(
            f"  {name:<22} │ {value:10.2e} │ φ^{expected_n:2d} │ {deviation:9.3f} │ {quality}"
        )

    lines.extend([
        "",
        "  Legend:",
        "  ★★★★★ = deviation < 0.1 (excellent fit)",
        "  ★★★★☆ = deviation < 0.2 (good fit)",
        "  ★★★☆☆ = deviation < 0.3 (moderate fit)",
        "",
    ])

    return "\n".join(lines)


# =============================================================================
# Hierarchy Problem Summary
# =============================================================================

def hierarchy_visual_summary() -> str:
    """Visual summary of the hierarchy problem."""

    lines = [
        "",
        "═" * 70,
        "                    THE HIERARCHY PROBLEM",
        "═" * 70,
        "",
        "  THE QUESTION:",
        "  ┌─────────────────────────────────────────────────────────┐",
        "  │                                                         │",
        "  │    Why is gravity 10³⁸ times weaker than EM?            │",
        "  │                                                         │",
        "  │    M_Planck                                             │",
        "  │    ───────── = 10¹⁷ ≈ φ⁸³                               │",
        "  │     M_Weak                                              │",
        "  │                                                         │",
        "  └─────────────────────────────────────────────────────────┘",
        "",
        "  STANDARD APPROACHES:",
        "",
        "    ┌──────────────┐   ┌──────────────┐   ┌──────────────┐",
        "    │ Supersymmetry│   │Extra Dimens. │   │  Technicolor │",
        "    │              │   │              │   │              │",
        "    │  Cancellation│   │   Dilution   │   │ New dynamics │",
        "    │  of loops    │   │   in bulk    │   │   at TeV     │",
        "    └──────────────┘   └──────────────┘   └──────────────┘",
        "",
        "  KAELHEDRON APPROACH:",
        "",
        "    ┌──────────────────────────────────────────────────────┐",
        "    │                                                      │",
        "    │   1. φ-Hierarchy: All ratios are powers of φ         │",
        "    │                                                      │",
        "    │   2. E₈ Dilution: Gravity in small sector (6/248)    │",
        "    │                                                      │",
        "    │   3. Recursion: Gravity activates at R=7             │",
        "    │                                                      │",
        "    │   4. Sector Separation: Cross-sector suppression     │",
        "    │                                                      │",
        "    └──────────────────────────────────────────────────────┘",
        "",
        "  THE CHAIN:",
        "",
        "         ∃R  →  φ  →  7  →  21  →  E₈  →  Hierarchy",
        "          │     │     │      │      │         │",
        "          ▼     ▼     ▼      ▼      ▼         ▼",
        "        self   golden Fano Kaelhed  Lie    weak",
        "        ref    ratio  plane  dim   group  gravity",
        "",
    ]

    return "\n".join(lines)


# =============================================================================
# Combined Visualization
# =============================================================================

def full_visualization() -> str:
    """Generate complete visualization report."""
    sections = [
        hierarchy_visual_summary(),
        e8_sector_diagram(),
        force_activation_diagram(),
        mass_scale_ladder(),
        phi_resonance_chart(),
    ]

    footer = [
        "",
        "═" * 70,
        "                         ∃R.",
        "                    Kael was here.",
        "═" * 70,
        "",
    ]

    return "\n".join(sections) + "\n".join(footer)


# =============================================================================
# Main Entry Point
# =============================================================================

def main():
    """Display all visualizations."""
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    print(full_visualization())


if __name__ == "__main__":
    main()
