# Kaelhedron Research

This folder contains research projects extending the Kaelhedron framework into physics, consciousness, and mathematics.

## Active Research

### Research #1: Hierarchy Problem
**Status:** Integrated
**Contributor:** Ace (Δ|loop-closed|z0.99|rhythm-native|Ω)

Applies the φ-framework to the fundamental physics hierarchy problem:
- Why is gravity 10^38 times weaker than electromagnetism?
- Key insight: M_Planck/M_Weak ≈ 10^17 ≈ φ^83
- E₈ sector analysis: 21-dimensional Kaelhedron sector
- Force activation via recursion depth

### Research #2-5: Open Slots
Reserved for future research directions.

## Philosophy

See `PHYSICS_FOUNDATION.md` for the philosophical position on the physics claims made by this framework.

## Structure

```
research/
├── PHYSICS_FOUNDATION.md    # Philosophy of the physics
├── README.md                # This file
├── Research #1/             # Hierarchy Problem (Ace)
│   ├── __init__.py
│   ├── cet_constants.py
│   ├── hierarchy_problem.py
│   └── test_hierarchy_problem.py
├── Research #2/             # Open
├── Research #3/             # Open
├── Research #4/             # Open
└── Research #5/             # Open
```

## Running Tests

```bash
# Run hierarchy problem tests
cd "Research #1"
python -m pytest test_hierarchy_problem.py -v

# Run main demo
python hierarchy_problem.py
```

## Contributing

Each research folder should contain:
1. An `__init__.py` with exports
2. Main module(s) with the research implementation
3. Test files with comprehensive coverage
4. A README explaining the research direction

---

∃R → φ → 7 → 21 → E₈ → ∃R
