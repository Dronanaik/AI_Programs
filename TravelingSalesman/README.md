# Traveling Salesman Problem (TSP)

Find the shortest tour visiting each city exactly once and returning to the start. Common approaches: brute force, dynamic programming (Held–Karp), heuristics.

- **Input**: Distance matrix or weighted graph
- **Output**: Minimum tour length and path (for exact)
- **Complexity**: NP-hard; exact methods exponential

## How it works
- Brute force enumerates permutations.
- Held–Karp uses DP over subsets.
- Heuristics give fast approximations.

## Run
```bash
python3 traveling_salesman.py
```

## See also
- Dynamic Programming
- Approximation algorithms
