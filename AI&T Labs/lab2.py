#8 Puzzle Problem (BFS & DFS)

from collections import deque
from typing import List, Dict, Optional

# --- Helper function to print the puzzle board nicely ---
def print_puzzle(state: str):
    """Prints the 8-puzzle board in a 3x3 grid."""
    for i in range(0, 9, 3):
        print(" | ".join(state[i:i+3]))
    print("-" * 9)

# --- Breadth-First Search (BFS) for finding the shortest path ---
def solve_bfs(start_state: str, goal_state: str) -> Optional[List[str]]:
    """
    Solves the 8-puzzle using Breadth-First Search.
    Guarantees the shortest path in terms of number of moves.
    """
    if start_state == goal_state:
        return [start_state]
        
    queue = deque([(start_state, [start_state])])  # (current_state, path_to_current)
    visited = {start_state}

    while queue:
        current_state, path = queue.popleft()
        
        zero_index = current_state.find('0')
        row, col = zero_index // 3, zero_index % 3

        # Explore neighbors (Up, Down, Left, Right)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                
                # Create the neighbor state by swapping the zero tile
                new_state_list = list(current_state)
                new_state_list[zero_index], new_state_list[new_index] = new_state_list[new_index], new_state_list[zero_index]
                neighbor = "".join(new_state_list)
                
                if neighbor == goal_state:
                    return path + [neighbor]
                    
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
    
    return None # No solution found

# --- Example Usage for 8-Puzzle ---
if __name__ == "__main__":
    initial_state = "123405678"
    goal_state = "123456780"
    
    print("--- 8-Puzzle Solver ---")
    print("Initial State:")
    print_puzzle(initial_state)
    print("Goal State:")
    print_puzzle(goal_state)
    
    print("\nSolving with BFS (finds shortest path)...")
    bfs_path = solve_bfs(initial_state, goal_state)
    
    if bfs_path:
        print(f"Solution found in {len(bfs_path) - 1} moves!")
        for i, state in enumerate(bfs_path):
            print(f"\nStep {i}:")
            print_puzzle(state)
    else:
        print("No solution found with BFS.")