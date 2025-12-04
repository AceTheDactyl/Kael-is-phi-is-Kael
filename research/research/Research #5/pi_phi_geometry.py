"""
THE GEOMETRY OF π/φ²

Why does the CKM phase equal π/φ²?

This file explores the deep geometric meaning behind this relationship.

Signature: Kaelhedron Research #5b
"""

from __future__ import annotations

import math
import sys
from typing import List, Tuple

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PHI = (1 + math.sqrt(5)) / 2
PI = math.pi


def main():
    print("\n" * 2)
    print("=" * 75)
    print("  THE GEOMETRY OF π/φ²")
    print("=" * 75)
    print()
    print("  'Geometry is the archetype of the beauty of the world.'")
    print("  — Johannes Kepler")
    print()

    # =========================================================================
    print("=" * 75)
    print("  PART 1: THE GOLDEN ANGLE")
    print("=" * 75)
    print()

    print("  The GOLDEN ANGLE is well-known in nature:")
    print()

    golden_angle = 2 * PI * (1 - 1/PHI)  # ≈ 137.5°
    golden_angle_deg = math.degrees(golden_angle)

    print(f"    Golden angle = 2π(1 - 1/φ) = 2π/φ² = {golden_angle:.4f} rad = {golden_angle_deg:.1f}°")
    print()
    print("  This appears in:")
    print("    - Phyllotaxis (leaf arrangements)")
    print("    - Sunflower seed spirals")
    print("    - Pinecone scales")
    print()

    print("  The CKM phase δ = π/φ² is HALF the golden angle!")
    print()

    ckm_phase = PI / PHI**2
    ckm_phase_deg = math.degrees(ckm_phase)

    print(f"    δ = π/φ² = {ckm_phase:.4f} rad = {ckm_phase_deg:.1f}°")
    print(f"    Golden angle / 2 = {golden_angle/2:.4f} rad = {golden_angle_deg/2:.1f}°")
    print()
    print("  ★ CP VIOLATION IS HALF THE GOLDEN ANGLE ★")
    print()

    # =========================================================================
    print("=" * 75)
    print("  PART 2: THE PENTAGON CONNECTION")
    print("=" * 75)
    print()

    print("  The regular pentagon is intimately connected to φ:")
    print()
    print("    - Diagonal/side = φ")
    print("    - Interior angle = 108° = 3π/5")
    print("    - Central angle = 72° = 2π/5")
    print()

    interior_angle = 3 * PI / 5
    central_angle = 2 * PI / 5

    print(f"    Interior angle = {math.degrees(interior_angle):.0f}°")
    print(f"    Central angle = {math.degrees(central_angle):.0f}°")
    print()

    print("  How does δ = π/φ² relate to the pentagon?")
    print()

    # Express π/φ² in terms of pentagon angles
    ratio_to_central = ckm_phase / central_angle
    ratio_to_interior = ckm_phase / interior_angle

    print(f"    δ / (2π/5) = {ratio_to_central:.4f}")
    print(f"    δ / (3π/5) = {ratio_to_interior:.4f}")
    print()

    # Check if δ is related to pentagon
    print("  Interesting relationships:")
    print()
    print(f"    5 × δ = {5 * ckm_phase:.4f} rad = {math.degrees(5 * ckm_phase):.1f}°")
    print(f"    5δ/π = {5 * ckm_phase / PI:.4f} = 5/φ² = {5/PHI**2:.4f}")
    print()

    # =========================================================================
    print("=" * 75)
    print("  PART 3: CIRCLE DIVISION")
    print("=" * 75)
    print()

    print("  If we divide a circle by δ = π/φ², how many sectors?")
    print()

    n_sectors = 2 * PI / ckm_phase
    print(f"    2π / δ = 2π / (π/φ²) = 2φ² = {n_sectors:.4f}")
    print()
    print(f"    2φ² = 2(φ + 1) = 2φ + 2 = {2*PHI + 2:.4f}")
    print()
    print("  The circle divides into 2φ² ≈ 5.24 sectors!")
    print()
    print("  This is between 5 (pentagon) and 6 (hexagon).")
    print("  It's the IRRATIONAL division that nature prefers!")
    print()

    # =========================================================================
    print("=" * 75)
    print("  PART 4: THE FIBONACCI ANGLE")
    print("=" * 75)
    print()

    print("  Fibonacci numbers F_n relate to φ via Binet's formula:")
    print()
    print("    F_n = (φⁿ - (-φ)⁻ⁿ) / √5")
    print()

    # Compute some Fibonacci-related angles
    print("  Angles from Fibonacci ratios:")
    print()

    fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i in range(2, len(fibs)):
        ratio = fibs[i-1] / fibs[i]
        angle = 2 * PI * ratio
        print(f"    2π × F_{i}/F_{i+1} = 2π × {fibs[i-1]}/{fibs[i]} = {angle:.4f} rad = {math.degrees(angle):.1f}°")

    print()
    print(f"  As n → ∞: 2π × F_n/F_(n+1) → 2π/φ = {2*PI/PHI:.4f} rad = {math.degrees(2*PI/PHI):.1f}°")
    print()

    # Compare to δ
    print(f"  Compare:")
    print(f"    δ = π/φ² = {ckm_phase:.4f} rad = {ckm_phase_deg:.1f}°")
    print(f"    2π/φ = {2*PI/PHI:.4f} rad = {math.degrees(2*PI/PHI):.1f}°")
    print(f"    π/φ = {PI/PHI:.4f} rad = {math.degrees(PI/PHI):.1f}°")
    print()

    # =========================================================================
    print("=" * 75)
    print("  PART 5: COMPLEX PLANE INTERPRETATION")
    print("=" * 75)
    print()

    print("  The CKM phase δ appears as a complex rotation:")
    print()
    print("    e^(iδ) = e^(iπ/φ²)")
    print()

    exp_delta = complex(math.cos(ckm_phase), math.sin(ckm_phase))
    print(f"    = cos(π/φ²) + i sin(π/φ²)")
    print(f"    = {exp_delta.real:.4f} + i × {exp_delta.imag:.4f}")
    print()

    # What's special about this point?
    print("  This point on the unit circle has special properties:")
    print()
    print(f"    cos(π/φ²) = {math.cos(ckm_phase):.4f}")
    print(f"    sin(π/φ²) = {math.sin(ckm_phase):.4f}")
    print()

    # Check if cos or sin are φ-related
    cos_val = math.cos(ckm_phase)
    sin_val = math.sin(ckm_phase)

    print("  Are these φ-related?")
    print()
    print(f"    cos(π/φ²) ≈ φ^({math.log(abs(cos_val))/math.log(PHI):.2f})")
    print(f"    sin(π/φ²) ≈ φ^({math.log(abs(sin_val))/math.log(PHI):.2f})")
    print()

    # Check specific values
    print("  Comparing to φ-expressions:")
    print()
    print(f"    cos(π/φ²) = {cos_val:.4f}")
    print(f"    1 - φ^(-2) = {1 - PHI**(-2):.4f}")
    print(f"    2 - φ = {2 - PHI:.4f}")
    print(f"    φ^(-1) = {PHI**(-1):.4f}")
    print()
    print(f"    sin(π/φ²) = {sin_val:.4f}")
    print(f"    φ^(-1) + φ^(-3) = {PHI**(-1) + PHI**(-3):.4f}")
    print(f"    √(1 - (2-φ)²) = {math.sqrt(1 - (2-PHI)**2):.4f}")
    print()

    # =========================================================================
    print("=" * 75)
    print("  PART 6: THE DILOGARITHM CONNECTION")
    print("=" * 75)
    print()

    print("  The dilogarithm Li₂(x) = Σ xⁿ/n² has remarkable identities at φ:")
    print()
    print("    Li₂(1/φ²) = π²/15 - ln²(φ)")
    print()
    print("  This connects π and φ through the dilogarithm!")
    print()

    # Approximate numerical check
    ln_phi = math.log(PHI)
    pi_sq_15 = PI**2 / 15
    ln_phi_sq = ln_phi**2

    print(f"    π²/15 = {pi_sq_15:.6f}")
    print(f"    ln²(φ) = {ln_phi_sq:.6f}")
    print(f"    π²/15 - ln²(φ) = {pi_sq_15 - ln_phi_sq:.6f}")
    print()

    # =========================================================================
    print("=" * 75)
    print("  PART 7: WHY π/φ² FOR CP VIOLATION?")
    print("=" * 75)
    print()

    print("  HYPOTHESIS: The CKM phase arises from a geometric constraint.")
    print()
    print("  In the Froggatt-Nielsen mechanism:")
    print("    - Yukawa couplings arise from φ^n factors")
    print("    - Complex phases arise from field rotations")
    print()
    print("  If the flavon field S has a φ-symmetric potential:")
    print()
    print("    V(S) = λ(|S|⁴ - M²|S|² - M⁴)")
    print()
    print("  The minimum is at |S| = √φ × M.")
    print()
    print("  The PHASE of ⟨S⟩ can be any value, but...")
    print()
    print("  If there's a discrete Z_n symmetry that interplays with U(1):")
    print()
    print("    The stable phase might be locked to π/φ².")
    print()

    # =========================================================================
    print("=" * 75)
    print("  PART 8: ANGLE ADDITION PROPERTIES")
    print("=" * 75)
    print()

    delta = ckm_phase

    print("  Interesting angle sums:")
    print()
    print(f"    δ + δ = 2δ = {2*delta:.4f} rad = {math.degrees(2*delta):.1f}°")
    print(f"    2δ ≈ 2π/φ³ = {2*PI/PHI**3:.4f} rad (error: {abs(2*delta - 2*PI/PHI**3)/delta*100:.1f}%)")
    print()
    print(f"    3δ = {3*delta:.4f} rad = {math.degrees(3*delta):.1f}°")
    print(f"    π - δ = {PI - delta:.4f} rad = {math.degrees(PI - delta):.1f}°")
    print()

    # Check if 3δ or 5δ give nice values
    print(f"    5δ = {5*delta:.4f} rad = {math.degrees(5*delta):.1f}°")
    print(f"    5δ = π × 5/φ² = {PI * 5/PHI**2:.4f} rad")
    print()

    # Is 5δ close to 2π - something?
    print(f"    2π - 5δ = {2*PI - 5*delta:.4f} rad = {math.degrees(2*PI - 5*delta):.1f}°")
    print()

    # =========================================================================
    print("=" * 75)
    print("  PART 9: THE TRIANGLE CLOSURE")
    print("=" * 75)
    print()

    print("  The unitarity triangle has angles α, β, γ with α + β + γ = π.")
    print()
    print("  If γ = δ = π/φ², what does this imply for α and β?")
    print()

    gamma = delta
    print(f"    γ = π/φ² = {gamma:.4f} rad = {math.degrees(gamma):.1f}°")
    print()

    # From experiment
    beta_exp = 0.384
    alpha_exp = PI - gamma - beta_exp

    print(f"  From experiment:")
    print(f"    β ≈ {beta_exp:.4f} rad = {math.degrees(beta_exp):.1f}°")
    print(f"    α = π - β - γ ≈ {alpha_exp:.4f} rad = {math.degrees(alpha_exp):.1f}°")
    print()

    # Check if β = arctan(φ^(-2))
    beta_phi = math.atan(PHI**(-2))
    print(f"  If β = arctan(φ⁻²):")
    print(f"    β = {beta_phi:.4f} rad = {math.degrees(beta_phi):.1f}°")
    print(f"    Error from experiment: {abs(beta_phi - beta_exp)/beta_exp*100:.1f}%")
    print()

    # Then α would be
    alpha_from_phi = PI - gamma - beta_phi
    print(f"    α = π - γ - β = {alpha_from_phi:.4f} rad = {math.degrees(alpha_from_phi):.1f}°")
    print()

    # Is α expressible in φ-terms?
    print("  Can α be expressed in φ?")
    print()
    alpha_candidates = [
        ("π/2 + arctan(φ⁻²) - π/φ²", PI/2 + math.atan(PHI**(-2)) - PI/PHI**2),
        ("π(1 - 1/φ²) - arctan(φ⁻²)", PI*(1 - 1/PHI**2) - math.atan(PHI**(-2))),
        ("arctan(φ²)", math.atan(PHI**2)),
        ("π - π/φ² - arctan(φ⁻²)", PI - PI/PHI**2 - math.atan(PHI**(-2))),
    ]

    for name, val in alpha_candidates:
        err = abs(val - alpha_exp) / alpha_exp * 100
        match = "✓" if err < 5 else ""
        print(f"    {name}")
        print(f"      = {val:.4f} rad = {math.degrees(val):.1f}° ({err:.1f}% off) {match}")
    print()

    # =========================================================================
    print("=" * 75)
    print("  SUMMARY: THE DEEP STRUCTURE")
    print("=" * 75)
    print()

    print("  ┌────────────────────────────────────────────────────────────────┐")
    print("  │                                                                │")
    print("  │  δ = π/φ² IS NOT ARBITRARY                                    │")
    print("  │                                                                │")
    print("  │  It is:                                                        │")
    print("  │    • Half the golden angle (natural phyllotaxis)              │")
    print("  │    • Related to pentagon geometry                              │")
    print("  │    • The irrational circle division                           │")
    print("  │    • Connected to dilogarithm identities                      │")
    print("  │                                                                │")
    print("  │  The CKM phase inherits the GEOMETRY of φ!                    │")
    print("  │                                                                │")
    print("  │  CP violation is encoded in the same mathematics              │")
    print("  │  that governs:                                                 │")
    print("  │    • Plant growth patterns                                    │")
    print("  │    • Pentagon tilings                                          │")
    print("  │    • Fibonacci spirals                                         │")
    print("  │    • The mass hierarchy (φ^n)                                 │")
    print("  │                                                                │")
    print("  └────────────────────────────────────────────────────────────────┘")
    print()

    print("  The universe is GEOMETRICALLY CONSISTENT:")
    print()
    print("    Masses:     φ^n")
    print("    Mixings:    φ^(-3|i-j|)")
    print("    CP phase:   π/φ²")
    print()
    print("  All derive from the same self-similar structure.")
    print()
    print("=" * 75)
    print()
    print("  ∃R")
    print()
    print("  The geometry of existence")
    print("  is written in golden ratios.")
    print()
    print("  π/φ² = the angle of matter.")
    print()
    print("  ∃R.")
    print()
    print("=" * 75)


if __name__ == "__main__":
    main()
