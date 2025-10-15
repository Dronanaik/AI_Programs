# Water Jug Problem

Given two jugs with capacities A and B, measure exactly C liters using fill, empty, and pour operations. Solved via BFS or number theory.

- **State**: (water in jug A, water in jug B)
- **Goal**: Reach state with C liters

## How it works
Model as a graph of states and run BFS; or use Bezout’s theorem: C must be multiple of gcd(A, B) and ≤ max(A, B).

## Run
```bash
python3 water_jug_problem.py
```

## See also
- BFS on state spaces
- Number theory (gcd)
