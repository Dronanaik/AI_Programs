class State:
    def __init__(self, monkey_location, monkey_on_box, box_location,monkey_has_banana):
        self.monkey_location = monkey_location
        self.monkey_on_box = monkey_on_box
        self.box_location = box_location
        self.monkey_has_banana = monkey_has_banana
    def __str__(self):
        return f"Monkey: {self.monkey_location}, On Box:{self.monkey_on_box}, Box: {self.box_location}, Has Banana:{self.monkey_has_banana}"
def grasp(state):
    state.monkey_has_banana = True
    return state
def climb(state):
    state.monkey_on_box = True
    return state
def drag(state, p1, p2):
    state.box_location = p2
    return state
def walk(state, p1, p2):
    state.monkey_location = p2
    return state
def can_get(state):
    return state.monkey_has_banana
def solve():
    initial_state = State("middle", "onbox", "middle", False)
    # Grasp the banana
    state1 = grasp(initial_state)
    print(f"Step 1: {state1}")
    # Climb onto the box
    state2 = climb(state1)
    print(f"Step 2: {state2}")
    # Drag the box from 'middle' to 'right'
    state3 = drag(state2, "middle", "right")
    print(f"Step 3: {state3}")
    # Walk from 'middle' to 'right'
    state4 = walk(state3, "middle", "right")
    print(f"Step 4: {state4}")
    if can_get(state4):
        print("Goal reached: Monkey has the banana!")
    else:
        print("Goal not reached.")
solve()