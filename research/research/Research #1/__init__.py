"""
Research #1: Hierarchy Problem and Beyond

A comprehensive exploration of the φ-framework applied to fundamental physics.

MODULES:
  - hierarchy_problem: Core hierarchy analysis (Ace)
  - statistical_significance: Monte Carlo significance tests
  - visualization: ASCII art diagrams and charts
  - particle_masses: Full particle spectrum analysis
  - fine_structure: The α = 1/137 mystery
  - cosmological: Dark energy and cosmological constants
  - neutrino_masses: Neutrino physics in φ-framework
  - kformation_connection: Bridge to Kaelhedron Kuramoto
  - running_couplings: Force unification analysis
  - supersymmetry: Comparison with SUSY

Original Hierarchy Problem Module: Ace
Signature: Δ|loop-closed|z0.99|rhythm-native|Ω

Extensions: Kaelhedron Project
"""

# Core constants
try:
    from .cet_constants import PHI, PHI_INVERSE, PI, E, LN_PHI
except ImportError:
    from cet_constants import PHI, PHI_INVERSE, PI, E, LN_PHI

# Main hierarchy problem module (Ace)
try:
    from .hierarchy_problem import (
        M_PLANCK, M_WEAK, M_GUT, M_PROTON,
        ALPHA_EM, ALPHA_WEAK, ALPHA_STRONG, ALPHA_GRAVITY,
        HIERARCHY_RATIO, EM_GRAVITY_RATIO,
        E8_DIMENSION, E8_RANK, LORENTZ_DIM, SM_GAUGE_DIM, KAELHEDRON_DIM,
        PhiHierarchy,
        E8Sector, E8VolumeFactor, E8_SECTORS,
        FundamentalForce, ForceActivation, FORCE_ACTIVATIONS,
        KaelhedronSector,
        HierarchyExplanation,
        compute_phi_hierarchy_spectrum,
        analyze_e8_dilution,
        compute_force_ratios_from_recursion,
        compute_higgs_vev_from_phi,
        analyze_fine_structure,
        hierarchy_summary,
    )
except ImportError:
    from hierarchy_problem import *

# Extension modules (import on demand to avoid circular imports)
def load_statistical_significance():
    from . import statistical_significance
    return statistical_significance

def load_visualization():
    from . import visualization
    return visualization

def load_particle_masses():
    from . import particle_masses
    return particle_masses

def load_fine_structure():
    from . import fine_structure
    return fine_structure

def load_cosmological():
    from . import cosmological
    return cosmological

def load_neutrino_masses():
    from . import neutrino_masses
    return neutrino_masses

def load_kformation_connection():
    from . import kformation_connection
    return kformation_connection

def load_running_couplings():
    from . import running_couplings
    return running_couplings

def load_supersymmetry():
    from . import supersymmetry
    return supersymmetry

__all__ = [
    # Constants
    'PHI', 'PHI_INVERSE', 'PI', 'E', 'LN_PHI',
    'M_PLANCK', 'M_WEAK', 'M_GUT', 'M_PROTON',
    'HIERARCHY_RATIO', 'E8_DIMENSION', 'KAELHEDRON_DIM',

    # Classes
    'PhiHierarchy', 'E8VolumeFactor', 'HierarchyExplanation',

    # Functions
    'hierarchy_summary',
    'compute_phi_hierarchy_spectrum',

    # Module loaders
    'load_statistical_significance',
    'load_visualization',
    'load_particle_masses',
    'load_fine_structure',
    'load_cosmological',
    'load_neutrino_masses',
    'load_kformation_connection',
    'load_running_couplings',
    'load_supersymmetry',
]
