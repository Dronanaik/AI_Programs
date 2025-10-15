# 8-Puzzle

Classic sliding puzzle solved via search (BFS, A*, etc.). The objective is to reach the goal configuration by sliding tiles into the empty space.

- **State**: Board configuration
- **Action**: Slide a tile into the empty spot
- **Goal**: Reach goal board
- **Time**: Depends on search (BFS/A*)

## How it works
Define successor states and use a search strategy (often A* with Manhattan distance heuristic).

## Run
```bash
python3 eight_puzzle.py
```

## See also
- A* Search
- Heuristics (Manhattan distance)
