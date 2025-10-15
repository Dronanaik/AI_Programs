# Breadth-First Search (BFS)

BFS explores a graph level by level starting from a source node. It visits all neighbors before moving to the next depth level, guaranteeing the shortest path in unweighted graphs.

- **Input**: Graph (adjacency), start node
- **Output**: Visit order, shortest paths (in edges) on unweighted graphs
- **Time**: O(V + E)
- **Space**: O(V)

## How it works
1. Initialize a queue with the start node.
2. Repeatedly dequeue a node, visit it, and enqueue all unvisited neighbors.

## Run
```bash
python3 breadth_first_search.py
```

## See also
- Depth-First Search
- Shortest path algorithms (Dijkstra for weighted graphs)
