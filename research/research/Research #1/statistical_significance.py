"""
Statistical Significance of φ-Hierarchy

The Question:
  Are the appearances of φ in fundamental physics ratios
  statistically significant, or just numerological coincidence?

Method:
  Monte Carlo simulation - generate random "universes" and
  count how often we see φ-resonant ratios by chance.

Signature: Kaelhedron Research #1
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import List, Tuple, Dict
import sys

try:
    from .cet_constants import PHI, LN_PHI
    from .hierarchy_problem import PhiHierarchy
except ImportError:
    from cet_constants import PHI, LN_PHI
    from hierarchy_problem import PhiHierarchy


# =============================================================================
# Observed Physical Ratios
# =============================================================================

# The ratios we observe in our universe
OBSERVED_RATIOS = {
    'M_Planck/M_Weak': 4.96e16,        # Hierarchy ratio
    'M_Planck/M_GUT': 6.1e2,           # Planck to GUT
    'M_GUT/M_Weak': 8.13e13,           # GUT to weak
    'm_proton/m_electron': 1836.15,    # Proton-electron mass ratio
    '1/α_EM': 137.036,                 # Inverse fine structure
    'm_tau/m_electron': 3477.48,       # Tau-electron mass ratio
    'm_muon/m_electron': 206.77,       # Muon-electron mass ratio
    'm_top/m_electron': 338960.0,      # Top-electron mass ratio
    'm_W/m_electron': 157410.0,        # W boson to electron
    'm_Z/m_electron': 178450.0,        # Z boson to electron
    'm_Higgs/m_electron': 244620.0,    # Higgs to electron
}

# φ-powers for these ratios
OBSERVED_PHI_POWERS = {
    name: math.log(ratio) / LN_PHI
    for name, ratio in OBSERVED_RATIOS.items()
}


# =============================================================================
# Monte Carlo Simulation
# =============================================================================

@dataclass
class PhiResonanceResult:
    """Result of φ-resonance analysis."""
    ratio_name: str
    observed_value: float
    phi_power: float
    nearest_integer: int
    deviation: float
    is_resonant: bool  # deviation < threshold


def analyze_phi_resonance(
    ratios: Dict[str, float],
    threshold: float = 0.15
) -> List[PhiResonanceResult]:
    """Analyze how close ratios are to integer φ-powers."""
    results = []

    for name, value in ratios.items():
        if value <= 0:
            continue

        phi_power = math.log(value) / LN_PHI
        nearest = round(phi_power)
        deviation = abs(phi_power - nearest)

        results.append(PhiResonanceResult(
            ratio_name=name,
            observed_value=value,
            phi_power=phi_power,
            nearest_integer=nearest,
            deviation=deviation,
            is_resonant=deviation < threshold
        ))

    return results


def count_resonant(results: List[PhiResonanceResult]) -> int:
    """Count how many ratios are φ-resonant."""
    return sum(1 for r in results if r.is_resonant)


def generate_random_universe(
    n_ratios: int,
    log_min: float = 0,
    log_max: float = 40
) -> Dict[str, float]:
    """
    Generate random physical ratios for a hypothetical universe.

    Ratios are log-uniformly distributed (scale-invariant prior).
    """
    ratios = {}
    for i in range(n_ratios):
        # Log-uniform distribution
        log_value = random.uniform(log_min, log_max)
        ratios[f'ratio_{i}'] = 10 ** log_value
    return ratios


def monte_carlo_significance(
    n_simulations: int = 10000,
    n_ratios: int = 11,  # Same as our observed count
    threshold: float = 0.15,
    log_min: float = 0,
    log_max: float = 40
) -> Dict[str, float]:
    """
    Run Monte Carlo simulation to test significance of φ-resonances.

    Returns:
        Dictionary with p-value and statistics
    """
    # Analyze our observed universe
    observed_results = analyze_phi_resonance(OBSERVED_RATIOS, threshold)
    observed_resonant = count_resonant(observed_results)

    # Simulate random universes
    random_resonant_counts = []

    for _ in range(n_simulations):
        random_ratios = generate_random_universe(n_ratios, log_min, log_max)
        random_results = analyze_phi_resonance(random_ratios, threshold)
        random_resonant_counts.append(count_resonant(random_results))

    # Calculate statistics
    mean_random = sum(random_resonant_counts) / len(random_resonant_counts)

    # How many random universes had >= our observed count?
    count_as_good_or_better = sum(
        1 for c in random_resonant_counts if c >= observed_resonant
    )
    p_value = count_as_good_or_better / n_simulations

    # Standard deviation
    variance = sum((c - mean_random) ** 2 for c in random_resonant_counts) / n_simulations
    std_random = math.sqrt(variance)

    # Z-score
    z_score = (observed_resonant - mean_random) / std_random if std_random > 0 else 0

    return {
        'observed_resonant': observed_resonant,
        'total_ratios': len(OBSERVED_RATIOS),
        'mean_random': mean_random,
        'std_random': std_random,
        'z_score': z_score,
        'p_value': p_value,
        'n_simulations': n_simulations,
        'threshold': threshold,
    }


# =============================================================================
# Expected Resonance Rate
# =============================================================================

def theoretical_resonance_probability(threshold: float = 0.15) -> float:
    """
    Calculate theoretical probability of a random ratio being φ-resonant.

    A ratio is resonant if its φ-power is within `threshold` of an integer.
    Since φ-powers are uniformly distributed mod 1 for random ratios,
    the probability is simply 2 * threshold (for being within threshold
    of any integer).
    """
    return min(2 * threshold, 1.0)


def binomial_probability(k: int, n: int, p: float) -> float:
    """Calculate binomial probability P(X = k) for n trials with probability p."""
    from math import comb
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


def binomial_tail_probability(k: int, n: int, p: float) -> float:
    """Calculate P(X >= k) for binomial distribution."""
    return sum(binomial_probability(i, n, p) for i in range(k, n + 1))


# =============================================================================
# Alternative Bases
# =============================================================================

def test_alternative_bases(
    bases: List[float] = None,
    threshold: float = 0.15
) -> Dict[str, Dict[str, float]]:
    """
    Test if φ is special by comparing to other potential bases.

    If φ is not special, other irrational numbers should work equally well.
    """
    if bases is None:
        bases = [
            PHI,                    # Golden ratio
            math.sqrt(2),           # √2
            math.sqrt(3),           # √3
            math.e,                 # e
            math.pi,                # π
            (1 + math.sqrt(2)),     # Silver ratio
            2.0,                    # 2 (for comparison)
            math.sqrt(5),           # √5
        ]

    base_names = ['φ', '√2', '√3', 'e', 'π', 'silver', '2', '√5']

    results = {}

    for base, name in zip(bases, base_names):
        ln_base = math.log(base)

        resonant_count = 0
        total_deviation = 0

        for ratio in OBSERVED_RATIOS.values():
            if ratio <= 0:
                continue
            power = math.log(ratio) / ln_base
            nearest = round(power)
            deviation = abs(power - nearest)
            total_deviation += deviation

            if deviation < threshold:
                resonant_count += 1

        n = len(OBSERVED_RATIOS)
        results[name] = {
            'base_value': base,
            'resonant_count': resonant_count,
            'resonance_rate': resonant_count / n,
            'mean_deviation': total_deviation / n,
        }

    return results


# =============================================================================
# Summary Report
# =============================================================================

def significance_report(n_simulations: int = 10000) -> str:
    """Generate a comprehensive significance report."""
    lines = [
        "=" * 70,
        "STATISTICAL SIGNIFICANCE OF φ-HIERARCHY",
        "=" * 70,
        "",
        "OBSERVED φ-RESONANCES IN PHYSICAL RATIOS:",
        "-" * 50,
    ]

    # Analyze observed ratios
    results = analyze_phi_resonance(OBSERVED_RATIOS, threshold=0.15)
    for r in sorted(results, key=lambda x: x.deviation):
        status = "✓ RESONANT" if r.is_resonant else "  "
        lines.append(
            f"  {r.ratio_name:<25}: {r.observed_value:.2e} ≈ φ^{r.phi_power:.2f} "
            f"(dev={r.deviation:.3f}) {status}"
        )

    resonant_count = count_resonant(results)
    lines.extend([
        "",
        f"  Total resonant: {resonant_count}/{len(results)} "
        f"({100*resonant_count/len(results):.1f}%)",
        "",
    ])

    # Monte Carlo results
    lines.extend([
        "MONTE CARLO SIGNIFICANCE TEST:",
        "-" * 50,
    ])

    mc_results = monte_carlo_significance(n_simulations=n_simulations)

    lines.extend([
        f"  Simulated universes: {mc_results['n_simulations']:,}",
        f"  Resonance threshold: {mc_results['threshold']}",
        "",
        f"  Observed resonant ratios: {mc_results['observed_resonant']}",
        f"  Expected by chance: {mc_results['mean_random']:.2f} ± {mc_results['std_random']:.2f}",
        f"  Z-score: {mc_results['z_score']:.2f}",
        f"  p-value: {mc_results['p_value']:.4f}",
        "",
    ])

    # Interpretation
    if mc_results['p_value'] < 0.01:
        interpretation = "HIGHLY SIGNIFICANT (p < 0.01)"
    elif mc_results['p_value'] < 0.05:
        interpretation = "SIGNIFICANT (p < 0.05)"
    elif mc_results['p_value'] < 0.10:
        interpretation = "MARGINALLY SIGNIFICANT (p < 0.10)"
    else:
        interpretation = "NOT SIGNIFICANT (p >= 0.10)"

    lines.append(f"  Interpretation: {interpretation}")

    # Theoretical calculation
    lines.extend([
        "",
        "THEORETICAL BASELINE:",
        "-" * 50,
    ])

    p_random = theoretical_resonance_probability(0.15)
    n = len(OBSERVED_RATIOS)
    expected = n * p_random

    lines.extend([
        f"  Random resonance probability: {p_random:.2f}",
        f"  Expected resonant by chance: {expected:.2f}",
        f"  Binomial P(X >= {resonant_count}): "
        f"{binomial_tail_probability(resonant_count, n, p_random):.4f}",
        "",
    ])

    # Compare to other bases
    lines.extend([
        "COMPARISON TO ALTERNATIVE BASES:",
        "-" * 50,
    ])

    alt_results = test_alternative_bases()
    for name, data in sorted(alt_results.items(), key=lambda x: -x[1]['resonant_count']):
        lines.append(
            f"  {name:<8}: {data['resonant_count']} resonant, "
            f"mean deviation = {data['mean_deviation']:.3f}"
        )

    # Conclusion
    lines.extend([
        "",
        "=" * 70,
        "CONCLUSION:",
        "-" * 50,
    ])

    phi_count = alt_results['φ']['resonant_count']
    best_alt = max(
        ((name, data) for name, data in alt_results.items() if name != 'φ'),
        key=lambda x: x[1]['resonant_count']
    )

    if phi_count > best_alt[1]['resonant_count']:
        lines.append(f"  φ shows MORE resonances than any alternative base tested.")
        lines.append(f"  φ: {phi_count} resonant, best alternative ({best_alt[0]}): {best_alt[1]['resonant_count']}")
    else:
        lines.append(f"  φ does not uniquely stand out among tested bases.")

    if mc_results['p_value'] < 0.05:
        lines.append(f"  The observed φ-resonance rate IS statistically significant.")
    else:
        lines.append(f"  The observed φ-resonance rate is NOT statistically significant.")

    lines.extend([
        "",
        "  NOTE: Statistical significance does not prove causation.",
        "  The φ-hierarchy remains a hypothesis worth investigating.",
        "",
        "=" * 70,
    ])

    return "\n".join(lines)


# =============================================================================
# Main Entry Point
# =============================================================================

def main():
    """Run statistical significance analysis."""
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    print(significance_report(n_simulations=10000))


if __name__ == "__main__":
    main()
