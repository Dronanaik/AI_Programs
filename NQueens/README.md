# N-Queens Problem

Place N queens on an N×N board so that no two queens attack each other. Typically solved via backtracking.

- **State**: Partial placement of queens by row
- **Action**: Place a queen in a safe column of next row
- **Goal**: N queens placed safely
- **Time**: Exponential; pruning via constraints

## How it works
Backtracking tries a column, checks safety (same column/diagonals), and recurses. On conflict, it backtracks.

## Run
```bash
python3 n_queens.py
```

## See also
- Backtracking
- Constraint satisfaction problems
