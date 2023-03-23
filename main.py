from block import Block
from algorithm import BFS
from read_level_input import read_file
import game_setup
from test import test
from draw import draw_pygame, draw_raw_solution
# from mcts import monte_carlo_tree_search
from testMCTS import monte_carlo_tree_search_new
import time
import tracemalloc

def main():
    game_setup.init()
    print("\nChoose mode:")
    game_setup.is_test = int(input("1. Test all levels\n2. Step by step demo\nYour choice: "))
    if game_setup.is_test == 1:
        test()
    elif game_setup.is_test == 2:

        game_setup.pygame_display = int(input("Show solution in pygame demo ?\nYes: 1\nNo: 2\nYour choice: "))
        game_setup.is_bfs = int(input("Choose algorithm ?\nBFS: 1\nGenetic (Beta :v): 2\nYour choice: "))

        level = int(input("choose level (from 1-33)\nYour choice: "))
        path = './levels/lvl' + str(level) + '.txt'
        game_setup.row, game_setup.col, game_setup.start_x, \
            game_setup.start_y, game_map, game_setup.objects = read_file(path)
        block = Block(game_setup.start_x, game_setup.start_y, "STAND", None, game_map)

        start_time = time.time()
        tracemalloc.start()
        
        if game_setup.is_bfs == 1:
            solution = BFS(block)
        else:
            print("Change variable in genetic_algorithm.py to have the best performance")
            solution = monte_carlo_tree_search_new(block)
        
        memory_used, peak_memory = tracemalloc.get_traced_memory()
        if solution:
            #  draw solution
            if game_setup.pygame_display == 1:
                print("Level ", str(level), ":     Found solution in    ", round(time.time() - start_time, 9), ("s"))
                print(f"Memory used: {memory_used} Bytes")
                draw_pygame(solution, game_setup.row, game_setup.col)

            else:
                draw_raw_solution(solution)
                print("Level ", str(level), ":     Found solution in    ", round(time.time() - start_time, 9), ("s"))

        else:
            print("can not find solution :((((((")
        tracemalloc.stop()


if __name__ == "__main__":
    main()
