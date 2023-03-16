from block import Block
from algorithm import BFS, genetic_algorithm
from read_level_input import read_file
import global_variables
from test import test
from draw import draw_pygame, draw_raw_solution
# from mcts import monte_carlo_tree_search
from testMCTS import monte_carlo_tree_search_new
import time

def main():
    global_variables.init()
    print("\nChoose mode:")
    global_variables.is_test = int(input("1. Test all levels\n2. Step by step demo\nYour choice: "))
    if global_variables.is_test == 1:
        test()
    elif global_variables.is_test == 2:

        global_variables.pygame_display = int(input("Show solution in pygame demo ?\nYes: 1\nNo: 2\nYour choice: "))
        global_variables.is_bfs = int(input("Choose algorithm ?\nBFS: 1\nGenetic (Beta :v): 2\nYour choice: "))

        level = int(input("choose level (from 1-33)\nYour choice: "))
        path = './levels/lvl' + str(level) + '.txt'
        global_variables.row, global_variables.col, global_variables.start_x, \
            global_variables.start_y, game_map, global_variables.objects = read_file(path)
        block = Block(global_variables.start_x, global_variables.start_y, "STAND", None, game_map)

        start_time = time.time()
        
        if global_variables.is_bfs == 1:
            solution = BFS(block)
        else:
            print("Change variable in genetic_algorithm.py to have the best performance")
            solution = monte_carlo_tree_search_new(block)
        
        if solution:
            #  draw solution
            if global_variables.pygame_display == 1:
                print("Level ", str(level), ":     Found solution in    ", round(time.time() - start_time, 9), ("s"))
                draw_pygame(solution, global_variables.row, global_variables.col)

            else:
                draw_raw_solution(solution)
                print("Level ", str(level), ":     Found solution in    ", round(time.time() - start_time, 9), ("s"))

        else:
            print("can not find solution :((((((")


if __name__ == "__main__":
    main()
