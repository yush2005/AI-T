def solve_water_jug_simulation(capacity1: int, capacity2: int, goal: int):
    """
    Simulates one specific, rule-based path to solve the Water Jug Problem.

    Args:
        capacity1: The capacity of the first jug.
        capacity2: The capacity of the second jug.
        goal: The target amount of water to have in one of the jugs.
    """
    jug1, jug2 = 0, 0
    # Keep track of visited states to prevent infinite loops
    visited_states = set()

    print(f"--- Water Jug Simulation ---")
    print(f"Capacities: ({capacity1}, {capacity2}), Goal: {goal}\n")

    while (jug1, jug2) not in visited_states:
        # Add current state to visited set
        visited_states.add((jug1, jug2))
        print(f"Current State: ({jug1}, {jug2})")

        # Check if the goal is reached
        if jug1 == goal or jug2 == goal:
            print(f"\nGoal of {goal} liters reached! ✅")
            return

        # Apply a fixed sequence of rules
        if jug1 == 0:
            jug1 = capacity1
            print("Action: Fill Jug 1")
        elif jug2 == capacity2:
            jug2 = 0
            print("Action: Empty Jug 2")
        else:
            # Calculate amount to pour from jug1 to jug2
            transfer_amount = min(jug1, capacity2 - jug2)
            jug1 -= transfer_amount
            jug2 += transfer_amount
            print("Action: Pour Jug 1 -> Jug 2")

    print(f"\nCould not reach goal with this rule set. Stuck in a loop. 🛑")

# --- Example Usage ---
solve_water_jug_simulation(capacity1=4, capacity2=3, goal=2)