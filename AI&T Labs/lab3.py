# A* Problem

import math
from heapq import heappush, heappop
from typing import List, Tuple, Callable, Optional

# --- Type Aliases (for clarity) ---
Point = Tuple[int, int]
Path = List[Point]
Grid = List[List[int]]

# --- Heuristic Functions ---
def manhattan_distance(a: Point, b: Point) -> int:
    """Calculates the Manhattan distance (city block distance)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean_distance(a: Point, b: Point) -> float:
    """Calculates the straight-line Euclidean distance."""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# --- A* Search Algorithm ---
def astar(
    start: Point,
    goal: Point,
    grid: Grid,
    heuristic: Callable[[Point, Point], float] = manhattan_distance
) -> Optional[Path]:
    """Finds the shortest path from start to goal using the A* algorithm."""
    rows, cols = len(grid), len(grid[0])
    
    # Priority queue: (f_score, node, path_to_node)
    open_list: List[Tuple[float, Point, Path]] = [(0, start, [start])]
    visited: set[Point] = set()

    while open_list:
        # Get the node with the lowest f_score from the priority queue
        f_score, current_node, path = heappop(open_list)

        if current_node == goal:
            return path  # Path found!

        if current_node in visited:
            continue
        
        visited.add(current_node)

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current_node[0] + dx, current_node[1] + dy)
            nx, ny = neighbor

            # Check if neighbor is valid (within bounds and not an obstacle)
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                
                # *** FIX WAS HERE ***
                # g_score is the actual cost from the start to this neighbor
                g_score = len(path) # The cost to the current node is len(path)
                
                # h_score is the estimated heuristic cost from the neighbor to the goal
                h_score = heuristic(neighbor, goal)
                
                # f_score is the total estimated cost
                new_f_score = (g_score + 1) + h_score # Add 1 for the step to the neighbor
                
                # Add the neighbor to the open list with its new path
                heappush(open_list, (new_f_score, neighbor, path + [neighbor]))

    return None # No path found

# --- Example Usage ---
# Example grid (0=free, 1=blocked)
grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start, goal = (0, 0), (4, 4)

# Run the algorithm with both heuristics
manhattan_path = astar(start, goal, grid, manhattan_distance)
euclidean_path = astar(start, goal, grid, euclidean_distance)

print("Manhattan Path:", manhattan_path)
print("Euclidean Path:", euclidean_path)