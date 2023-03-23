import game_setup
from functions import check_win, action, get_solution

def BFS(block):
    game_setup.previous = [block]  
    queue = [block]
    solution = []
    while queue:
        
        current = queue.pop(0)
        if check_win(current):
            print("Success! Found solution after", current.id, "steps:")
            solution = get_solution(current)
            break

        if current.status != "SPLIT":
            action(queue, current.move_up())
            action(queue, current.move_right())
            action(queue, current.move_down())
            action(queue, current.move_left())
        else:
            action(queue, current.split_move_up())
            action(queue, current.split_move_right())
            action(queue, current.split_move_down())
            action(queue, current.split_move_left())

            action(queue, current.split_move_up_other())
            action(queue, current.split_move_right_other())
            action(queue, current.split_move_down_other())
            action(queue, current.split_move_left_other())
    return solution

