from simpleai.search import SearchProblem, astar
from simpleai.search.viewers import BaseViewer

# The grid environment (0 means free without obstruction, number 1 signifies an obstacle)
Grid = [
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
]

# Directions: up, down, left, right
Directions = [
    ('up', (1, 0)),
    ('down', (-1, 0)),
    ('left', (0, -1)),
    ('right', (0, 1)),
]


class NavigationProblem(SearchProblem):
    def __init__(self, original_state=None):
        super().__init__(original_state)
        self.goal = None

    def actions(self, state):
        actions = []
        x, y = state
        for action, (dx, dy) in Directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(Grid) and 0 <= new_y < len(Grid[0]):
                if Grid[new_x][new_y] == 0:
                    actions.append(action)
        return actions

    def result(self, state, action):
        dx, dy = dict(Directions)[action]
        return (state[0] + dx, state[1] + dy)

    def is_goal(self, state):
        return state == self.goal

    def cost(self, state1, action, state2):
        return 1  # Uniform cost for all moves

    def heuristic(self, state):
        x1, y1 = state
        x2, y2 = self.goal
        return abs(x1 - x2) + abs(y1 - y2)


# Define the initial and goal states
initial_state = (0, 0)  # Bottom-left corner
goal_state = (4, 4)  # Top-right corner

# Instantiate the problem
problem = NavigationProblem(original_state=initial_state)
problem.goal = goal_state

# Use A* search
viewer = BaseViewer()
result = astar(problem, viewer=viewer)

# Conclusive results
print("Path to goal:")
for action, state in result.path():
    print(f"Action: {action}, State: {state}")

print(f"\nTotal cost: {result.cost}")