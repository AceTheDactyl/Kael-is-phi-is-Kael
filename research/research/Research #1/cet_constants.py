"""
CET Constants for Hierarchy Problem Module

Core mathematical and physical constants used throughout the
φ-hierarchy framework for analyzing the hierarchy problem.

These constants bridge the Kaelhedron framework with Ace's
scalar_architecture physics module.
"""

import math

# =============================================================================
# Mathematical Constants
# =============================================================================

# Golden ratio and related
PHI = (1 + math.sqrt(5)) / 2          # φ = 1.618033988749895
PHI_INVERSE = 1 / PHI                  # φ⁻¹ = 0.618033988749895
PSI = 1 - PHI                          # ψ = -0.618033988749895

# Natural logarithm of φ (for converting between base-e and base-φ)
LN_PHI = math.log(PHI)                 # ln(φ) = 0.4812118250596034

# Standard mathematical constants
PI = math.pi                           # π = 3.141592653589793
E = math.e                             # e = 2.718281828459045
TAU = 2 * PI                          # τ = 2π = 6.283185307179586

# =============================================================================
# Derived Constants
# =============================================================================

# Powers of φ frequently used
PHI_2 = PHI ** 2                       # φ² = 2.618033988749895
PHI_3 = PHI ** 3                       # φ³ = 4.23606797749979
PHI_7 = PHI ** 7                       # φ⁷ = 29.034441853748634 (K-formation)
PHI_21 = PHI ** 21                     # φ²¹ = 24476.000399940013

# Inverse powers
PHI_INV_7 = PHI ** (-7)               # φ⁻⁷ = 0.03444185374863... (gravity activation)

# =============================================================================
# Kaelhedron-Specific Constants
# =============================================================================

# The three fundamental numbers
SEVEN = 7                              # Fano plane, K-formation threshold
TWENTY_ONE = 21                        # F₈ = C(7,2) = dim(so(7))
EIGHT = 8                              # Fibonacci index, E₈ rank

# K-formation threshold
K_THRESHOLD = PHI_INVERSE              # κ > φ⁻¹ for K-formation

# =============================================================================
# Verification
# =============================================================================

def verify_constants():
    """Verify mathematical relationships between constants."""
    assert abs(PHI * PHI_INVERSE - 1.0) < 1e-15, "φ × φ⁻¹ should be 1"
    assert abs(PHI - 1 - PHI_INVERSE) < 1e-15, "φ = 1 + φ⁻¹"
    assert abs(PHI ** 2 - PHI - 1) < 1e-15, "φ² = φ + 1"
    assert abs(PHI + PSI - 1) < 1e-15, "φ + ψ = 1"
    assert abs(PHI * PSI - (-1)) < 1e-15, "φ × ψ = -1"
    return True


if __name__ == "__main__":
    verify_constants()
    print("All constants verified!")
    print(f"PHI = {PHI}")
    print(f"PHI_INVERSE = {PHI_INVERSE}")
    print(f"LN_PHI = {LN_PHI}")
    print(f"PI = {PI}")
    print(f"E = {E}")
