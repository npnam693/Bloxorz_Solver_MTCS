import game_setup
from functions import is_win, action, get_solution

def BFS(block):
    game_setup.previous = [block]  
    queue = [block]
    solution = []
    while queue:
        currentState = queue.pop(0)

        if is_win(currentState):
            print("Success! Found solution after", currentState.id, "steps:")
            solution = get_solution(currentState)
            break

        if currentState.status != "SPLIT":
            action(queue, currentState.move_up())
            action(queue, currentState.move_down())
            action(queue, currentState.move_left())
            action(queue, currentState.move_right())
        else:
            action(queue, currentState.S1_move_up())
            action(queue, currentState.S1_move_down())
            action(queue, currentState.S1_move_left())
            action(queue, currentState.S1_move_right())

            action(queue, currentState.S2_move_up())
            action(queue, currentState.S2_move_down())
            action(queue, currentState.S2_move_left())
            action(queue, currentState.S2_move_right())
    return solution

