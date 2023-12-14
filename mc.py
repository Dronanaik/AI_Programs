from queue import Queue

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def __eq__(self, other):
        return self.missionaries == other.missionaries and \
               self.cannibals == other.cannibals and \
               self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def is_valid(state):
    if state.missionaries < 0 or state.cannibals < 0 or state.missionaries > 3 or state.cannibals > 3:
        return False
    if state.missionaries < state.cannibals and state.missionaries > 0:
        return False
    if 3 - state.missionaries < 3 - state.cannibals and 3 - state.missionaries > 0:
        return False
    return True

def get_neighbors(current_state):
    neighbors = []

    if current_state.boat == 'left':
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = State(current_state.missionaries - m, current_state.cannibals - c, 'right')
                    if is_valid(new_state):
                        neighbors.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = State(current_state.missionaries + m, current_state.cannibals + c, 'left')
                    if is_valid(new_state):
                        neighbors.append(new_state)

    return neighbors

def solve_missionaries_cannibals():
    initial_state = State(3, 3, 'left')
    goal_state = State(0, 0, 'right')

    frontier = Queue()
    frontier.put((initial_state, []))
    explored = set()

    while not frontier.empty():
        current_state, path = frontier.get()

        if current_state == goal_state:
            return path

        explored.add(current_state)

        for neighbor in get_neighbors(current_state):
            if neighbor not in explored:
                frontier.put((neighbor, path + [current_state]))

    return None

def print_solution(path):
    for i, state in enumerate(path):
        print(f"Step {i + 1}: {state.missionaries} missionaries, {state.cannibals} cannibals, boat on {state.boat} side.")

if __name__ == "__main__":
    solution_path = solve_missionaries_cannibals()

    if solution_path:
        print("Solution found:")
        print_solution(solution_path)
    else:
        print("No solution found.")
