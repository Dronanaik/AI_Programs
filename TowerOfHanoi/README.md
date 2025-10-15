# Tower of Hanoi

Move a stack of disks from source to target peg using an auxiliary peg, moving one disk at a time and never placing a larger disk on a smaller one.

- **Input**: Number of disks
- **Output**: Sequence of moves
- **Time**: O(2^n)

## How it works
Recursive relation: T(n) = 2·T(n−1) + 1. Move n−1 to aux, move largest to target, move n−1 from aux to target.

## Run
```bash
python3 tower_of_hanoi.py
```

## See also
- Recursion
