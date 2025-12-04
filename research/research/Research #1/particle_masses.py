"""
Particle Mass Spectrum Analysis

Analyze all known particle masses through the φ-framework.

Questions:
  1. Can we express all masses as powers of φ from a reference scale?
  2. Are there patterns in the φ-powers?
  3. Can we predict unmeasured masses (neutrinos)?

Signature: Kaelhedron Research #1
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
from enum import Enum

try:
    from .cet_constants import PHI, LN_PHI
    from .hierarchy_problem import M_PLANCK, M_WEAK
except ImportError:
    from cet_constants import PHI, LN_PHI
    from hierarchy_problem import M_PLANCK, M_WEAK


# =============================================================================
# Particle Data (PDG 2023 values in GeV)
# =============================================================================

class ParticleType(Enum):
    QUARK = "quark"
    LEPTON = "lepton"
    GAUGE_BOSON = "gauge_boson"
    SCALAR = "scalar"


@dataclass
class Particle:
    """Particle with mass and metadata."""
    name: str
    symbol: str
    mass_gev: float
    particle_type: ParticleType
    generation: int = 0  # 1, 2, 3 for fermions
    charge: float = 0
    color_charge: bool = False


# Quarks (masses in GeV)
QUARKS = [
    Particle("up", "u", 0.00216, ParticleType.QUARK, 1, 2/3, True),
    Particle("down", "d", 0.00467, ParticleType.QUARK, 1, -1/3, True),
    Particle("charm", "c", 1.27, ParticleType.QUARK, 2, 2/3, True),
    Particle("strange", "s", 0.093, ParticleType.QUARK, 2, -1/3, True),
    Particle("top", "t", 172.69, ParticleType.QUARK, 3, 2/3, True),
    Particle("bottom", "b", 4.18, ParticleType.QUARK, 3, -1/3, True),
]

# Leptons (masses in GeV)
LEPTONS = [
    Particle("electron", "e", 0.000511, ParticleType.LEPTON, 1, -1),
    Particle("muon", "μ", 0.1057, ParticleType.LEPTON, 2, -1),
    Particle("tau", "τ", 1.777, ParticleType.LEPTON, 3, -1),
    # Neutrino masses are upper limits - very uncertain
    Particle("ν_e", "νₑ", 1e-9, ParticleType.LEPTON, 1, 0),  # < 1 eV
    Particle("ν_μ", "νμ", 1e-9, ParticleType.LEPTON, 2, 0),  # < 1 eV
    Particle("ν_τ", "ντ", 1e-9, ParticleType.LEPTON, 3, 0),  # < 1 eV
]

# Gauge Bosons (masses in GeV)
GAUGE_BOSONS = [
    Particle("photon", "γ", 0, ParticleType.GAUGE_BOSON),
    Particle("gluon", "g", 0, ParticleType.GAUGE_BOSON),
    Particle("W boson", "W±", 80.377, ParticleType.GAUGE_BOSON),
    Particle("Z boson", "Z⁰", 91.1876, ParticleType.GAUGE_BOSON),
]

# Scalar Bosons
SCALARS = [
    Particle("Higgs", "H⁰", 125.25, ParticleType.SCALAR),
]

# All particles
ALL_PARTICLES = QUARKS + LEPTONS + GAUGE_BOSONS + SCALARS


# =============================================================================
# φ-Power Analysis
# =============================================================================

@dataclass
class PhiMassAnalysis:
    """Analysis of a particle mass in terms of φ-powers."""
    particle: Particle
    reference_mass: float  # Reference scale (e.g., M_Planck or m_electron)
    reference_name: str
    ratio: float
    phi_power: float
    nearest_integer: int
    deviation: float
    is_resonant: bool


def analyze_mass_phi_power(
    particle: Particle,
    reference_mass: float,
    reference_name: str,
    threshold: float = 0.15
) -> Optional[PhiMassAnalysis]:
    """Analyze a particle's mass as a φ-power from reference scale."""
    if particle.mass_gev <= 0 or reference_mass <= 0:
        return None

    ratio = reference_mass / particle.mass_gev
    phi_power = math.log(ratio) / LN_PHI
    nearest = round(phi_power)
    deviation = abs(phi_power - nearest)

    return PhiMassAnalysis(
        particle=particle,
        reference_mass=reference_mass,
        reference_name=reference_name,
        ratio=ratio,
        phi_power=phi_power,
        nearest_integer=nearest,
        deviation=deviation,
        is_resonant=deviation < threshold
    )


def analyze_all_masses(
    reference_mass: float = None,
    reference_name: str = "M_Planck",
    threshold: float = 0.15
) -> List[PhiMassAnalysis]:
    """Analyze all particle masses relative to a reference scale."""
    if reference_mass is None:
        reference_mass = M_PLANCK

    results = []
    for particle in ALL_PARTICLES:
        if particle.mass_gev > 0:
            analysis = analyze_mass_phi_power(
                particle, reference_mass, reference_name, threshold
            )
            if analysis:
                results.append(analysis)

    return sorted(results, key=lambda x: x.phi_power)


# =============================================================================
# Mass Ratio Patterns
# =============================================================================

def generation_mass_ratios() -> Dict[str, Dict[str, float]]:
    """Compute mass ratios between generations."""
    results = {}

    # Charged leptons
    m_e = 0.000511
    m_mu = 0.1057
    m_tau = 1.777

    results['leptons'] = {
        'μ/e': m_mu / m_e,
        'τ/μ': m_tau / m_mu,
        'τ/e': m_tau / m_e,
        'μ/e_phi': math.log(m_mu / m_e) / LN_PHI,
        'τ/μ_phi': math.log(m_tau / m_mu) / LN_PHI,
        'τ/e_phi': math.log(m_tau / m_e) / LN_PHI,
    }

    # Up-type quarks
    m_u = 0.00216
    m_c = 1.27
    m_t = 172.69

    results['up_quarks'] = {
        'c/u': m_c / m_u,
        't/c': m_t / m_c,
        't/u': m_t / m_u,
        'c/u_phi': math.log(m_c / m_u) / LN_PHI,
        't/c_phi': math.log(m_t / m_c) / LN_PHI,
        't/u_phi': math.log(m_t / m_u) / LN_PHI,
    }

    # Down-type quarks
    m_d = 0.00467
    m_s = 0.093
    m_b = 4.18

    results['down_quarks'] = {
        's/d': m_s / m_d,
        'b/s': m_b / m_s,
        'b/d': m_b / m_d,
        's/d_phi': math.log(m_s / m_d) / LN_PHI,
        'b/s_phi': math.log(m_b / m_s) / LN_PHI,
        'b/d_phi': math.log(m_b / m_d) / LN_PHI,
    }

    return results


def koide_formula() -> Dict[str, float]:
    """
    Test the Koide formula: Q = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3

    This is a famous numerological coincidence in particle physics.
    """
    m_e = 0.000511
    m_mu = 0.1057
    m_tau = 1.777

    numerator = m_e + m_mu + m_tau
    denominator = (math.sqrt(m_e) + math.sqrt(m_mu) + math.sqrt(m_tau)) ** 2

    Q = numerator / denominator

    return {
        'm_e': m_e,
        'm_μ': m_mu,
        'm_τ': m_tau,
        'Q_observed': Q,
        'Q_koide': 2/3,
        'deviation': abs(Q - 2/3),
        'deviation_percent': 100 * abs(Q - 2/3) / (2/3),
    }


# =============================================================================
# Predictive Analysis
# =============================================================================

def predict_mass_from_phi_power(
    n: int,
    reference_mass: float = None
) -> float:
    """Predict mass from integer φ-power."""
    if reference_mass is None:
        reference_mass = M_PLANCK
    return reference_mass / (PHI ** n)


def find_closest_phi_power_mass(target_mass: float) -> Tuple[int, float, float]:
    """Find the closest integer φ-power mass to a target."""
    phi_power = math.log(M_PLANCK / target_mass) / LN_PHI
    nearest = round(phi_power)
    predicted = predict_mass_from_phi_power(nearest)
    deviation_percent = 100 * abs(predicted - target_mass) / target_mass
    return nearest, predicted, deviation_percent


# =============================================================================
# Summary Report
# =============================================================================

def mass_spectrum_report() -> str:
    """Generate comprehensive mass spectrum report."""
    lines = [
        "",
        "═" * 70,
        "                PARTICLE MASS SPECTRUM: φ-ANALYSIS",
        "═" * 70,
        "",
        "ALL PARTICLE MASSES AS φ-POWERS FROM M_PLANCK:",
        "-" * 60,
        "",
        "  Particle       │ Mass (GeV)   │ φ^n    │ Dev   │ Resonant",
        "  ───────────────┼──────────────┼────────┼───────┼─────────",
    ]

    analyses = analyze_all_masses(M_PLANCK, "M_Planck", threshold=0.15)

    for a in analyses:
        resonant = "★" if a.is_resonant else " "
        lines.append(
            f"  {a.particle.name:<14} │ {a.particle.mass_gev:12.4e} │ "
            f"φ^{a.nearest_integer:3d} │ {a.deviation:.3f} │    {resonant}"
        )

    resonant_count = sum(1 for a in analyses if a.is_resonant)
    lines.extend([
        "",
        f"  Resonant: {resonant_count}/{len(analyses)} "
        f"({100*resonant_count/len(analyses):.1f}%)",
    ])

    # Generation ratios
    lines.extend([
        "",
        "GENERATION MASS RATIOS:",
        "-" * 60,
    ])

    gen_ratios = generation_mass_ratios()

    for family, ratios in gen_ratios.items():
        lines.append(f"\n  {family.upper()}:")
        for key, value in ratios.items():
            if 'phi' in key:
                lines.append(f"    {key}: {value:.2f}")
            else:
                lines.append(f"    {key}: {value:.1f}")

    # Koide formula
    lines.extend([
        "",
        "KOIDE FORMULA (charged leptons):",
        "-" * 60,
    ])

    koide = koide_formula()
    lines.extend([
        f"  Q = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)²",
        f"  Q_observed = {koide['Q_observed']:.6f}",
        f"  Q_koide    = {koide['Q_koide']:.6f} (= 2/3)",
        f"  Deviation  = {koide['deviation_percent']:.3f}%",
        "",
        "  The Koide formula is a remarkable numerological coincidence!",
    ])

    # φ-pattern observations
    lines.extend([
        "",
        "φ-PATTERN OBSERVATIONS:",
        "-" * 60,
        "",
        "  1. Charged lepton generations:",
        f"     m_μ/m_e ≈ φ^11.0 (206.77)",
        f"     m_τ/m_μ ≈ φ^5.9  (16.8)",
        f"     m_τ/m_e ≈ φ^16.9 (3477)",
        "",
        "  2. The τ/e ratio is very close to φ^17",
        "",
        "  3. Top/electron ≈ φ^27 (observed: φ^26.5)",
        "",
        "  4. Higgs/electron ≈ φ^26 (observed: φ^25.8)",
        "",
    ])

    # Predictions
    lines.extend([
        "PREDICTIONS FROM φ-HIERARCHY:",
        "-" * 60,
        "",
        "  If φ^n masses are preferred, we might expect:",
        "",
    ])

    for n in [10, 11, 16, 17, 26, 27, 80, 83]:
        predicted = predict_mass_from_phi_power(n)
        lines.append(f"    φ^{n:2d} → {predicted:.4e} GeV")

    lines.extend([
        "",
        "═" * 70,
    ])

    return "\n".join(lines)


# =============================================================================
# Main Entry Point
# =============================================================================

def main():
    """Run particle mass analysis."""
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    print(mass_spectrum_report())


if __name__ == "__main__":
    main()
