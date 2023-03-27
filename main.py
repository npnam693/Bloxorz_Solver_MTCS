from block import Block
from BFS_algorithm import BFS
from read_level import read_file, read_file_forAS
import game_setup
from test import testBFS, testMCTS, testAstart
from draw import draw_pygame, draw_raw_solution
from MCTS_algorithm import MCTS
from Astart_algorithm import Astar
import time
import tracemalloc

def main():
    game_setup.init()
    
    print("\nChoose mode:")
    game_setup.run_mode = int(input("1. Test all levels\n2. Step by step demo\nYour choice: "))
    if game_setup.run_mode == 1:
        alogirthm = int(input("Choose algorithm ?\nBFS: 1\nMCTS: 2\nAstar: 3 \nYour choice: "))
        if (alogirthm == 1): testBFS()
        elif (alogirthm == 2): testMCTS()
        else : testAstart()
    
    elif game_setup.run_mode == 2:
        game_setup.pygame_display = int(input("Show solution in pygame demo ?\nYes: 1\nNo: 2\nYour choice: "))
        
        alogirthm = int(input("Choose algorithm ?\nBFS: 1\nMCTS: 2\nAstar: 3 \nYour choice: "))
        
        if alogirthm == 1: game_setup.is_bfs = 1 
        
        level = int(input("choose level (from 1-33)\nYour choice: "))
        path = './levels/lvl' + str(level) + '.txt'
        


        start_time = time.time()
        
        if game_setup.is_bfs == 1:
            game_setup.row, game_setup.col, game_setup.start_x, \
                game_setup.start_y, game_map, game_setup.objects = read_file(path)
            block = Block(game_setup.start_x, game_setup.start_y, "STAND", None, game_map)

            solution = BFS(block)
        elif alogirthm == 2:
            game_setup.row, game_setup.col, game_setup.start_x, \
            game_setup.start_y, game_map, game_setup.objects = read_file(path)
            block = Block(game_setup.start_x, game_setup.start_y, "STAND", None, game_map)
            solution = MCTS(block)
        else:
            if level in [8,9,10,15,16,20,22,23,24,26, 28]: 
                print("Level ", str(level), ":    Time Limited")
                time.sleep(30)
                return 

            game_setup.row, game_setup.col, game_setup.start_x, \
            game_setup.start_y, game_map, game_setup.objects, \
                game_setup.goal_x, game_setup.goal_y= read_file_forAS(path)
            block = Block(game_setup.start_x, game_setup.start_y, "STAND", None, game_map)

            a = Astar()
            solution = a.solve_by_astar(block)

        if solution:
            #  draw solution
            if game_setup.pygame_display == 1:
                print("Level ", str(level), ":     Found solution in    ", round(time.time() - start_time, 9), ("s"))
                draw_pygame(solution, game_setup.row, game_setup.col)
            else:
                draw_raw_solution(solution)
                print("Level ", str(level), ":     Found solution in    ", round(time.time() - start_time, 9), ("s"))

        else:
            print("can not find solution :((((((")


if __name__ == "__main__":
    main()


