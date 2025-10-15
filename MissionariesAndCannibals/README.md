# Missionaries and Cannibals

Transport missionaries and cannibals across a river without ever leaving missionaries outnumbered. Solved with BFS/DFS on state space.

- **State**: (M_left, C_left, boat_side)
- **Constraints**: M_left ≥ C_left and M_right ≥ C_right when missionaries present

## How it works
Generate valid moves, avoid invalid states, search to a goal state.

## Run
```bash
python3 missionaries_and_cannibals.py
```

## See also
- State-space search
