"""
Comprehensive Deviation Analysis

Apply the nested φ-structure discovery to ALL measurements.

Every deviation from an expected φ^n should be tested:
  Is the deviation itself a φ-power?

This is ∃R: self-reference at every level.

Signature: Kaelhedron Research #1
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
from enum import Enum

# Fix Windows encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PHI = (1 + math.sqrt(5)) / 2
PHI_INV = 1 / PHI
LN_PHI = math.log(PHI)


# =============================================================================
# ALL PHYSICAL MEASUREMENTS
# =============================================================================

# Format: (name, observed_value, category)
ALL_MEASUREMENTS = [
    # === MASS RATIOS (relative to electron) ===
    ("m_top/m_e", 338960.0, "mass"),
    ("m_Higgs/m_e", 244620.0, "mass"),
    ("m_Z/m_e", 178450.0, "mass"),
    ("m_W/m_e", 157410.0, "mass"),
    ("m_bottom/m_e", 8180.0, "mass"),
    ("m_tau/m_e", 3477.48, "mass"),
    ("m_charm/m_e", 2485.0, "mass"),
    ("m_proton/m_e", 1836.15, "mass"),
    ("m_muon/m_e", 206.77, "mass"),
    ("m_strange/m_e", 182.0, "mass"),
    ("m_down/m_e", 9.14, "mass"),
    ("m_up/m_e", 4.23, "mass"),

    # === HIERARCHY RATIOS ===
    ("M_Planck/M_Weak", 4.96e16, "hierarchy"),
    ("M_Planck/M_GUT", 6.1e2, "hierarchy"),
    ("M_GUT/M_Weak", 8.13e13, "hierarchy"),
    ("M_Planck/m_proton", 1.30e19, "hierarchy"),

    # === COUPLING CONSTANTS ===
    ("1/alpha_EM", 137.036, "coupling"),
    ("1/alpha_W", 30.0, "coupling"),
    ("1/alpha_S", 8.5, "coupling"),
    ("alpha_EM/alpha_G", 1.23e36, "coupling"),

    # === COSMOLOGICAL ===
    ("Omega_Lambda/Omega_m", 2.175, "cosmo"),
    ("t_universe/t_Planck", 8.07e60, "cosmo"),

    # === NEUTRINO ===
    ("m_nu3/m_nu2", 5.80, "neutrino"),

    # === GENERATION RATIOS ===
    ("m_tau/m_mu", 16.82, "generation"),
    ("m_mu/m_e", 206.77, "generation"),
    ("m_c/m_u", 588.0, "generation"),
    ("m_t/m_c", 136.0, "generation"),
    ("m_s/m_d", 19.9, "generation"),
    ("m_b/m_s", 44.9, "generation"),

    # === KOIDE-RELATED ===
    ("Koide_Q", 0.666632, "koide"),
    ("Koide_deviation", 0.000035, "koide"),  # Q - 2/3
]


# =============================================================================
# Nested φ-Structure Analysis
# =============================================================================

@dataclass
class NestedPhiResult:
    """Complete nested φ-structure analysis."""
    name: str
    observed: float
    category: str

    # First level: observed = φ^exact_power
    exact_power: float
    nearest_int_n: int
    fractional_delta: float  # exact_power - n

    # Second level: is delta itself a φ-power?
    delta_sign: str  # '+' or '-'
    delta_abs: float
    delta_as_phi_power: float  # delta = ±φ^(-m)
    nearest_m: int
    delta_coefficient: float  # c where delta = c × φ^(-m)

    # Quality metrics
    delta_is_phi_resonant: bool
    coefficient_near_unity: bool
    overall_quality: str  # 'EXACT', 'GOOD', 'FAIR', 'POOR'


def analyze_nested_structure(
    name: str,
    observed: float,
    category: str,
    threshold: float = 0.2
) -> Optional[NestedPhiResult]:
    """Analyze a measurement for nested φ-structure."""

    if observed <= 0:
        return None

    # First level: find φ-power
    exact_power = math.log(observed) / LN_PHI
    nearest_n = round(exact_power)
    delta = exact_power - nearest_n

    if abs(delta) < 0.001:
        # Already an integer power, no nested structure
        return NestedPhiResult(
            name=name, observed=observed, category=category,
            exact_power=exact_power, nearest_int_n=nearest_n,
            fractional_delta=delta,
            delta_sign='+' if delta >= 0 else '-',
            delta_abs=abs(delta),
            delta_as_phi_power=0,
            nearest_m=0,
            delta_coefficient=0,
            delta_is_phi_resonant=True,
            coefficient_near_unity=True,
            overall_quality='EXACT'
        )

    # Second level: analyze the deviation
    delta_sign = '+' if delta >= 0 else '-'
    delta_abs = abs(delta)

    # Express |delta| as φ^(-m) × coefficient
    # |delta| = c × φ^(-m)
    # log(|delta|) = log(c) - m × log(φ)
    # For coefficient c ≈ 1: m ≈ -log(|delta|) / log(φ)

    if delta_abs > 0:
        delta_phi_power = math.log(delta_abs) / LN_PHI  # This is negative
        nearest_m = round(-delta_phi_power)  # m is positive (φ^(-m) is small)

        if nearest_m > 0:
            expected_delta = PHI ** (-nearest_m)
            coefficient = delta_abs / expected_delta
        else:
            nearest_m = 1
            expected_delta = PHI ** (-1)
            coefficient = delta_abs / expected_delta
    else:
        delta_phi_power = 0
        nearest_m = 0
        coefficient = 0

    # Quality assessment
    delta_resonant = abs(delta_phi_power - (-nearest_m)) < threshold
    coef_near_unity = 0.7 < coefficient < 1.4

    if delta_resonant and coef_near_unity:
        if 0.95 < coefficient < 1.05:
            quality = 'EXACT'
        else:
            quality = 'GOOD'
    elif delta_resonant or coef_near_unity:
        quality = 'FAIR'
    else:
        quality = 'POOR'

    return NestedPhiResult(
        name=name, observed=observed, category=category,
        exact_power=exact_power, nearest_int_n=nearest_n,
        fractional_delta=delta,
        delta_sign=delta_sign,
        delta_abs=delta_abs,
        delta_as_phi_power=delta_phi_power,
        nearest_m=nearest_m,
        delta_coefficient=coefficient,
        delta_is_phi_resonant=delta_resonant,
        coefficient_near_unity=coef_near_unity,
        overall_quality=quality
    )


def analyze_all_measurements() -> List[NestedPhiResult]:
    """Analyze all measurements for nested φ-structure."""
    results = []
    for name, value, category in ALL_MEASUREMENTS:
        result = analyze_nested_structure(name, value, category)
        if result:
            results.append(result)
    return results


# =============================================================================
# Statistical Analysis of Nested Structure
# =============================================================================

def monte_carlo_nested(
    n_simulations: int = 10000,
    n_measurements: int = 30,
    threshold: float = 0.2
) -> Dict[str, float]:
    """
    Monte Carlo test: How often do random ratios show nested φ-structure?
    """
    import random

    # Count how many of our observed measurements have good nested structure
    observed_results = analyze_all_measurements()
    observed_good = sum(1 for r in observed_results if r.overall_quality in ['EXACT', 'GOOD'])
    observed_exact = sum(1 for r in observed_results if r.overall_quality == 'EXACT')

    # Simulate random universes
    random_good_counts = []
    random_exact_counts = []

    for _ in range(n_simulations):
        good_count = 0
        exact_count = 0

        for _ in range(n_measurements):
            # Generate random ratio (log-uniform)
            log_value = random.uniform(0, 40)
            value = 10 ** log_value

            # Analyze
            exact_power = math.log(value) / LN_PHI
            nearest_n = round(exact_power)
            delta = exact_power - nearest_n
            delta_abs = abs(delta)

            if delta_abs > 0.001:
                delta_phi_power = math.log(delta_abs) / LN_PHI
                nearest_m = round(-delta_phi_power)
                if nearest_m > 0:
                    expected_delta = PHI ** (-nearest_m)
                    coefficient = delta_abs / expected_delta

                    delta_resonant = abs(delta_phi_power - (-nearest_m)) < threshold
                    coef_near_unity = 0.7 < coefficient < 1.4

                    if delta_resonant and coef_near_unity:
                        good_count += 1
                        if 0.95 < coefficient < 1.05:
                            exact_count += 1
            else:
                exact_count += 1  # Integer power counts as exact

        random_good_counts.append(good_count)
        random_exact_counts.append(exact_count)

    # Calculate statistics
    mean_good = sum(random_good_counts) / n_simulations
    mean_exact = sum(random_exact_counts) / n_simulations

    p_value_good = sum(1 for c in random_good_counts if c >= observed_good) / n_simulations
    p_value_exact = sum(1 for c in random_exact_counts if c >= observed_exact) / n_simulations

    return {
        'observed_total': len(observed_results),
        'observed_good': observed_good,
        'observed_exact': observed_exact,
        'expected_good': mean_good,
        'expected_exact': mean_exact,
        'p_value_good': p_value_good,
        'p_value_exact': p_value_exact,
        'n_simulations': n_simulations,
    }


# =============================================================================
# Second-Order Deviations (Deviations of Deviations)
# =============================================================================

def analyze_second_order_deviations(results: List[NestedPhiResult]) -> List[Dict]:
    """
    For measurements with nested structure, check if the coefficient
    deviation from 1.0 is ALSO φ-structured.

    If observed = φ^(n + c×φ^(-m)), is (c - 1) a φ-power?
    """
    second_order = []

    for r in results:
        if r.overall_quality in ['EXACT', 'GOOD', 'FAIR'] and r.nearest_m > 0:
            c = r.delta_coefficient
            c_deviation = abs(c - 1.0)

            if c_deviation > 0.01:  # Non-trivial deviation
                c_dev_phi_power = math.log(c_deviation) / LN_PHI
                c_dev_nearest = round(-c_dev_phi_power)

                if c_dev_nearest > 0:
                    expected_c_dev = PHI ** (-c_dev_nearest)
                    c_dev_ratio = c_deviation / expected_c_dev

                    second_order.append({
                        'name': r.name,
                        'coefficient': c,
                        'c_deviation': c_deviation,
                        'c_dev_phi_power': c_dev_phi_power,
                        'c_dev_nearest_m': c_dev_nearest,
                        'c_dev_ratio': c_dev_ratio,
                        'is_nested': 0.7 < c_dev_ratio < 1.4,
                    })

    return second_order


# =============================================================================
# Summary Report
# =============================================================================

def comprehensive_report() -> str:
    """Generate comprehensive deviation analysis report."""
    lines = [
        "",
        "=" * 75,
        "         COMPREHENSIVE NESTED φ-STRUCTURE ANALYSIS",
        "=" * 75,
        "",
        "Testing ∃R: Do ALL deviations follow the pattern φ^(n ± c×φ^(-m))?",
        "",
    ]

    results = analyze_all_measurements()

    # Group by category
    categories = {}
    for r in results:
        if r.category not in categories:
            categories[r.category] = []
        categories[r.category].append(r)

    # Report by category
    for category, cat_results in categories.items():
        lines.extend([
            "-" * 75,
            f"  {category.upper()}",
            "-" * 75,
            "",
            "  Ratio              │ Observed   │ φ^n±δ      │ δ as φ^(-m) │ c    │ Quality",
            "  ───────────────────┼────────────┼────────────┼─────────────┼──────┼────────",
        ])

        for r in sorted(cat_results, key=lambda x: -x.exact_power):
            if r.nearest_m > 0:
                nested = f"{r.delta_sign}φ^(-{r.nearest_m})"
            else:
                nested = "integer"

            quality_symbol = {
                'EXACT': '★★★',
                'GOOD': '★★☆',
                'FAIR': '★☆☆',
                'POOR': '☆☆☆'
            }.get(r.overall_quality, '???')

            lines.append(
                f"  {r.name:<18} │ {r.observed:10.2e} │ "
                f"φ^{r.nearest_int_n:3d}{r.delta_sign}{abs(r.fractional_delta):.2f} │ "
                f"{nested:<11} │ {r.delta_coefficient:4.2f} │ {quality_symbol}"
            )

        lines.append("")

    # Summary statistics
    total = len(results)
    exact = sum(1 for r in results if r.overall_quality == 'EXACT')
    good = sum(1 for r in results if r.overall_quality == 'GOOD')
    fair = sum(1 for r in results if r.overall_quality == 'FAIR')
    poor = sum(1 for r in results if r.overall_quality == 'POOR')

    lines.extend([
        "=" * 75,
        "  SUMMARY",
        "=" * 75,
        "",
        f"  Total measurements: {total}",
        f"  EXACT (c ≈ 1.0):    {exact} ({100*exact/total:.0f}%)",
        f"  GOOD  (0.7<c<1.4):  {good} ({100*good/total:.0f}%)",
        f"  FAIR:               {fair} ({100*fair/total:.0f}%)",
        f"  POOR:               {poor} ({100*poor/total:.0f}%)",
        "",
        f"  Nested structure (EXACT+GOOD): {exact+good}/{total} ({100*(exact+good)/total:.0f}%)",
        "",
    ])

    # Monte Carlo test
    lines.extend([
        "=" * 75,
        "  MONTE CARLO SIGNIFICANCE TEST",
        "=" * 75,
        "",
        "  Running 10,000 simulated universes...",
        "",
    ])

    mc = monte_carlo_nested(n_simulations=10000, n_measurements=total)

    lines.extend([
        f"  Observed EXACT+GOOD: {mc['observed_good']}/{mc['observed_total']}",
        f"  Expected by chance:  {mc['expected_good']:.1f}",
        f"  p-value:             {mc['p_value_good']:.4f}",
        "",
        f"  Observed EXACT:      {mc['observed_exact']}/{mc['observed_total']}",
        f"  Expected by chance:  {mc['expected_exact']:.1f}",
        f"  p-value:             {mc['p_value_exact']:.4f}",
        "",
    ])

    if mc['p_value_good'] < 0.05:
        lines.append("  ★★★ STATISTICALLY SIGNIFICANT (p < 0.05) ★★★")
    elif mc['p_value_good'] < 0.10:
        lines.append("  ★★☆ MARGINALLY SIGNIFICANT (p < 0.10)")
    else:
        lines.append("  ☆☆☆ NOT SIGNIFICANT (p >= 0.10)")

    lines.append("")

    # Second-order deviations
    second = analyze_second_order_deviations(results)
    if second:
        lines.extend([
            "=" * 75,
            "  SECOND-ORDER DEVIATIONS (coefficient deviations)",
            "=" * 75,
            "",
        ])

        nested_second = sum(1 for s in second if s['is_nested'])
        lines.append(f"  Measurements with c ≠ 1: {len(second)}")
        lines.append(f"  Of those, (c-1) is φ-structured: {nested_second}")
        lines.append("")

        for s in second[:10]:  # Top 10
            status = "★" if s['is_nested'] else " "
            lines.append(
                f"    {s['name']}: c={s['coefficient']:.3f}, "
                f"|c-1|={s['c_deviation']:.3f} ≈ φ^({s['c_dev_phi_power']:.1f}) "
                f"→ φ^(-{s['c_dev_nearest_m']}) × {s['c_dev_ratio']:.2f} {status}"
            )

        lines.append("")

    # Key findings
    lines.extend([
        "=" * 75,
        "  KEY FINDINGS",
        "=" * 75,
        "",
        "  EXACT matches (coefficient ≈ 1.0):",
        "",
    ])

    for r in results:
        if r.overall_quality == 'EXACT' and r.nearest_m > 0:
            lines.append(
                f"    {r.name} = φ^({r.nearest_int_n} {r.delta_sign} φ^(-{r.nearest_m}))"
            )

    lines.extend([
        "",
        "=" * 75,
    ])

    return "\n".join(lines)


# =============================================================================
# Main Entry Point
# =============================================================================

def main():
    print(comprehensive_report())


if __name__ == "__main__":
    main()
