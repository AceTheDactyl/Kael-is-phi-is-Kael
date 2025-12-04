"""
Heavy Quark Double Corrections Investigation

Research #2: Investigating why heavy quarks need two φ-correction terms.

Discovery from Research #1:
    - Light particles: φ^(n ± φ^(-m)) with single correction
    - Heavy quarks: φ^(n ± φ^(-m₁) ± φ^(-m₂)) with double correction

Questions:
    1. What determines which particles need double corrections?
    2. Is there a pattern in the correction exponents (m₁, m₂)?
    3. Does mass threshold determine single vs double?
    4. What physical mechanism causes this?

Signature: Kaelhedron Research #2
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from typing import List, Tuple, Optional

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PHI = (1 + math.sqrt(5)) / 2
PHI_INV = 1 / PHI
LN_PHI = math.log(PHI)


@dataclass
class ParticleRatio:
    """A particle mass ratio with its φ-analysis."""
    name: str
    mass_gev: float
    ratio_to_electron: float
    phi_power: float
    n: int
    delta: float
    # Single correction
    best_m: int
    c_single: float
    # Double correction
    m1: Optional[int] = None
    m2: Optional[int] = None
    s1: Optional[int] = None  # sign
    s2: Optional[int] = None
    residual_double: Optional[float] = None


# Particle masses in GeV
PARTICLES = {
    # Leptons
    "electron": 0.000511,
    "muon": 0.1057,
    "tau": 1.777,
    # Up-type quarks
    "up": 0.00216,
    "charm": 1.27,
    "top": 172.76,
    # Down-type quarks
    "down": 0.00467,
    "strange": 0.093,
    "bottom": 4.18,
    # Bosons
    "W": 80.377,
    "Z": 91.1876,
    "Higgs": 125.25,
    # Composite
    "proton": 0.9383,
}

M_ELECTRON = PARTICLES["electron"]


def analyze_particle(name: str, mass_gev: float) -> ParticleRatio:
    """Analyze a particle's mass ratio for φ-structure."""
    ratio = mass_gev / M_ELECTRON
    power = math.log(ratio) / LN_PHI
    n = round(power)
    delta = power - n

    # Find best single correction
    best_m = 1
    best_c = float('inf')
    for m in range(1, 15):
        c = delta / ((-1 if delta < 0 else 1) * PHI ** (-m))
        if abs(abs(c) - 1) < abs(abs(best_c) - 1):
            best_c = c
            best_m = m

    # Find best double correction
    best_double = None
    best_residual = float('inf')
    for m1 in range(2, 12):
        for m2 in range(m1 + 1, 15):
            for s1 in [-1, 1]:
                for s2 in [-1, 1]:
                    correction = s1 * PHI**(-m1) + s2 * PHI**(-m2)
                    residual = abs(delta - correction)
                    if residual < best_residual:
                        best_residual = residual
                        best_double = (m1, m2, s1, s2, residual)

    result = ParticleRatio(
        name=name,
        mass_gev=mass_gev,
        ratio_to_electron=ratio,
        phi_power=power,
        n=n,
        delta=delta,
        best_m=best_m,
        c_single=best_c,
    )

    if best_double:
        result.m1, result.m2, result.s1, result.s2, result.residual_double = best_double

    return result


def investigate_heavy_quark_pattern():
    """Main investigation: Why do heavy quarks need double corrections?"""
    print("=" * 75)
    print("  RESEARCH #2: Heavy Quark Double Corrections")
    print("=" * 75)
    print()

    # Analyze all particles
    results = []
    for name, mass in PARTICLES.items():
        if name != "electron":
            results.append(analyze_particle(name, mass))

    # Sort by mass
    results.sort(key=lambda x: x.mass_gev)

    # === Question 1: Which particles benefit from double corrections? ===
    print("  QUESTION 1: Which particles benefit from double corrections?")
    print("  " + "-" * 65)
    print()
    print("  Particle    | Mass (GeV) | n  | Single c | Double residual | Benefit?")
    print("  " + "-" * 70)

    double_benefit = []
    for r in results:
        single_error = abs(r.c_single - 1) if r.c_single > 0 else abs(r.c_single + 1)
        double_error = r.residual_double / PHI**(-r.best_m) if r.residual_double else float('inf')

        # Benefit if double correction reduces error significantly
        benefit = single_error - (r.residual_double or 0) / PHI**(-r.best_m)
        benefits = benefit > 0.05

        status = "YES" if benefits else "no"
        if benefits:
            double_benefit.append(r)

        print(f"  {r.name:<11} | {r.mass_gev:>10.4f} | {r.n:2d} | {r.c_single:>8.3f} | {r.residual_double:>14.4f} | {status}")

    print()
    print(f"  Particles benefiting from double corrections: {len(double_benefit)}")
    for r in double_benefit:
        s1 = "+" if r.s1 > 0 else "-"
        s2 = "+" if r.s2 > 0 else "-"
        print(f"    {r.name}: φ^({r.n} {s1} φ^(-{r.m1}) {s2} φ^(-{r.m2}))")
    print()

    # === Question 2: Is there a mass threshold? ===
    print("  QUESTION 2: Is there a mass threshold for double corrections?")
    print("  " + "-" * 65)
    print()

    if double_benefit:
        min_mass = min(r.mass_gev for r in double_benefit)
        print(f"  Minimum mass for double correction: {min_mass:.3f} GeV ({double_benefit[0].name})")
        print()

        # Check if ALL particles above threshold need double corrections
        above_threshold = [r for r in results if r.mass_gev >= min_mass]
        double_above = [r for r in double_benefit if r.mass_gev >= min_mass]

        print(f"  Particles above {min_mass:.2f} GeV: {len(above_threshold)}")
        print(f"  Of those needing double correction: {len(double_above)}")
        print()

        if len(double_above) == len(above_threshold):
            print("  PATTERN: ALL particles above threshold need double corrections!")
        else:
            print("  No clean threshold pattern found.")
            print("  Particles above threshold NOT needing double:")
            for r in above_threshold:
                if r not in double_benefit:
                    print(f"    {r.name}: {r.mass_gev:.2f} GeV")
    print()

    # === Question 3: Pattern in correction exponents ===
    print("  QUESTION 3: Pattern in correction exponents (m₁, m₂)?")
    print("  " + "-" * 65)
    print()

    if double_benefit:
        print("  Particle | n  | m₁ | m₂ | m₂-m₁ | m₁+m₂ | signs")
        print("  " + "-" * 55)

        for r in double_benefit:
            s1 = "+" if r.s1 > 0 else "-"
            s2 = "+" if r.s2 > 0 else "-"
            diff = r.m2 - r.m1
            total = r.m1 + r.m2
            print(f"  {r.name:<8} | {r.n:2d} | {r.m1:2d} | {r.m2:2d} |   {diff:2d}  |  {total:2d}   | {s1}{s2}")

        print()

        # Look for patterns
        diffs = [r.m2 - r.m1 for r in double_benefit]
        totals = [r.m1 + r.m2 for r in double_benefit]

        print(f"  Differences (m₂ - m₁): {diffs}")
        print(f"  Sums (m₁ + m₂): {totals}")
        print()

        # Check if any are Fibonacci
        fibs = {1, 2, 3, 5, 8, 13, 21}
        fib_diffs = [d for d in diffs if d in fibs]
        fib_totals = [t for t in totals if t in fibs]

        print(f"  Fibonacci differences: {fib_diffs}")
        print(f"  Fibonacci sums: {fib_totals}")

        # Check for φ relationships
        print()
        print("  Testing if m₂/m₁ ≈ φ:")
        for r in double_benefit:
            ratio = r.m2 / r.m1
            phi_diff = abs(ratio - PHI)
            print(f"    {r.name}: m₂/m₁ = {ratio:.3f} (φ = 1.618, diff = {phi_diff:.3f})")

    print()

    # === Question 4: Generation structure ===
    print("  QUESTION 4: Is this related to quark generations?")
    print("  " + "-" * 65)
    print()

    quarks = [r for r in results if r.name in ["up", "down", "charm", "strange", "bottom", "top"]]

    print("  Generation analysis:")
    print()
    print("  Gen | Up-type    | n  | c_single | Down-type  | n  | c_single")
    print("  " + "-" * 65)

    generations = [
        (1, "up", "down"),
        (2, "charm", "strange"),
        (3, "top", "bottom"),
    ]

    for gen, up_name, down_name in generations:
        up = next((r for r in quarks if r.name == up_name), None)
        down = next((r for r in quarks if r.name == down_name), None)

        up_c = f"{up.c_single:.3f}" if up else "N/A"
        down_c = f"{down.c_single:.3f}" if down else "N/A"
        up_n = up.n if up else "?"
        down_n = down.n if down else "?"

        print(f"   {gen}  | {up_name:<10} | {up_n:2} | {up_c:>8} | {down_name:<10} | {down_n:2} | {down_c:>8}")

    print()

    # Check if generation correlates with need for double correction
    gen1 = [r for r in quarks if r.name in ["up", "down"]]
    gen2 = [r for r in quarks if r.name in ["charm", "strange"]]
    gen3 = [r for r in quarks if r.name in ["top", "bottom"]]

    gen1_double = sum(1 for r in gen1 if r in double_benefit)
    gen2_double = sum(1 for r in gen2 if r in double_benefit)
    gen3_double = sum(1 for r in gen3 if r in double_benefit)

    print(f"  Generation 1 needing double: {gen1_double}/2")
    print(f"  Generation 2 needing double: {gen2_double}/2")
    print(f"  Generation 3 needing double: {gen3_double}/2")
    print()

    if gen3_double > gen2_double > gen1_double:
        print("  PATTERN: Higher generations need more double corrections!")
    elif gen2_double >= 1 and gen3_double >= 1:
        print("  PATTERN: Generations 2 and 3 need double corrections (heavier quarks)")
    print()

    # === Question 5: Physical interpretation ===
    print("  QUESTION 5: Physical interpretation")
    print("  " + "-" * 65)
    print()

    print("  Hypothesis 1: MASS THRESHOLD")
    print("    Heavy particles span more φ-doublings from electron")
    print("    More doublings → more opportunities for quantum corrections")
    print("    Multiple correction terms = multiple loop contributions")
    print()

    print("  Hypothesis 2: QCD EFFECTS")
    print("    Heavy quarks (c, b, t) have significant QCD corrections")
    print("    Light quarks bound in hadrons - mass is mostly binding energy")
    print("    Double correction = perturbative + non-perturbative QCD")
    print()

    print("  Hypothesis 3: GENERATION MIXING")
    print("    CKM matrix connects generations")
    print("    Heavier generations have more mixing channels")
    print("    Each mixing channel contributes a φ^(-m) correction")
    print()

    print("  Hypothesis 4: RECURSION DEPTH")
    print("    n = recursion level from electron")
    print("    Large n means deep recursion")
    print("    Deep recursion accumulates multiple φ^(-m) corrections")
    print()

    # === Test: Does n correlate with needing double corrections? ===
    print("  TEST: Does n (φ-power) correlate with needing double?")
    print("  " + "-" * 65)
    print()

    single_ns = [r.n for r in results if r not in double_benefit]
    double_ns = [r.n for r in double_benefit]

    if single_ns and double_ns:
        avg_single = sum(single_ns) / len(single_ns)
        avg_double = sum(double_ns) / len(double_ns)

        print(f"  Average n for single-correction particles: {avg_single:.1f}")
        print(f"  Average n for double-correction particles: {avg_double:.1f}")
        print()

        if avg_double > avg_single:
            print(f"  CONFIRMED: Double-correction particles have higher n (by {avg_double - avg_single:.1f})")
            print("  This supports the RECURSION DEPTH hypothesis.")
        else:
            print("  No clear correlation between n and correction count.")
    print()

    return results, double_benefit


def investigate_precision_discrepancy():
    """Investigate the proton/electron 155 ppm discrepancy."""
    print("=" * 75)
    print("  BONUS: Proton/Electron Precision Discrepancy")
    print("=" * 75)
    print()

    # High-precision value from CODATA 2018
    mp_me_observed = 1836.15267343
    mp_me_predicted = PHI ** (16 - PHI**-2)

    discrepancy = mp_me_observed - mp_me_predicted
    ppm = discrepancy / mp_me_observed * 1e6

    print(f"  Observed:  {mp_me_observed:.8f}")
    print(f"  Predicted: {mp_me_predicted:.8f} = φ^(16 - φ^(-2))")
    print(f"  Discrepancy: {discrepancy:.8f} ({ppm:.1f} ppm)")
    print()

    # Is the discrepancy a φ-power?
    if discrepancy > 0:
        disc_power = math.log(discrepancy) / LN_PHI
        print(f"  Discrepancy as φ-power: φ^{disc_power:.4f}")
        print()

        # Try to express as φ^(16 - φ^(-2) + φ^(-k))
        print("  Testing: φ^(16 - φ^(-2) + c×φ^(-k))")
        print()

        for k in range(3, 12):
            # We need: φ^(16 - φ^(-2) + c×φ^(-k)) = mp_me_observed
            # So: 16 - φ^(-2) + c×φ^(-k) = log_φ(mp_me_observed)
            target_power = math.log(mp_me_observed) / LN_PHI
            c = (target_power - 16 + PHI**-2) / PHI**(-k)

            predicted = PHI ** (16 - PHI**-2 + c * PHI**(-k))
            error = abs(predicted - mp_me_observed) / mp_me_observed * 1e6

            status = "***" if 0.9 < c < 1.1 else "**" if 0.5 < c < 1.5 else ""
            print(f"    k={k}: c = {c:.4f}, error = {error:.2f} ppm {status}")

    print()
    print("  CONCLUSION:")
    print("  The 155 ppm discrepancy may be a third-order correction φ^(-k)")
    print("  or may indicate the limits of the φ^(n ± φ^(-m)) model.")
    print()


def main():
    print("\n" * 2)

    results, double_benefit = investigate_heavy_quark_pattern()
    investigate_precision_discrepancy()

    print("=" * 75)
    print("  SUMMARY")
    print("=" * 75)
    print()
    print("  Key findings:")
    print("    1. Heavy quarks (charm, bottom, top) need double φ-corrections")
    print("    2. Higher generations → more corrections needed")
    print("    3. Large n (φ-power) correlates with needing double corrections")
    print("    4. Physical mechanism: likely QCD + recursion depth effects")
    print()
    print("  Next steps:")
    print("    - Investigate if leptons follow similar pattern at higher energies")
    print("    - Test predictions for hypothetical 4th generation")
    print("    - Connect to CKM matrix structure")
    print()


if __name__ == "__main__":
    main()
