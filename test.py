import game_setup
from read_level import read_file, read_file_forAS
from block import Block
import time
import tracemalloc

from BFS_algorithm import BFS
from MCTS_algorithm import MCTS
from Astart_algorithm import Astar

def testBFS():
    cnt_success = 0
    for level in range(1,34):
        path = './levels/lvl' + str(level) + '.txt'
        game_setup.init()
        game_setup.row, game_setup.col, game_setup.start_x, \
            game_setup.start_y, game_map, game_setup.objects = read_file(path)
        block = Block(game_setup.start_x, game_setup.start_y, "STAND", None, game_map)
        start_time = time.time()
        print("Testing level", level, " ..........")
        tracemalloc.start()
        solution = BFS(block)
        memory_used, peak_memory = tracemalloc.get_traced_memory()
        if solution:
            cnt_success += 1
            print("Level ", str(level), ":     Found solution in    ", round(time.time() - start_time, 9), ("s"))
            print(f"Memory used: {memory_used} Bytes")
        else:
            print("Failed to find solution :( ")
        print("===========================================")
        tracemalloc.stop()
    print(cnt_success ,"/33 level success")

def testMCTS():
    cnt_success = 0
    for level in range(1,34):
        if level in [9,10,11,12,14,15,16,17,18,20,22,23,26,28,29,30,31,32,33]: 
            print("Level ", str(level), ":    Time Limited")
            print("==========================================================")

            continue
        path = './levels/lvl' + str(level) + '.txt'
        game_setup.init()
        game_setup.row, game_setup.col, game_setup.start_x, \
            game_setup.start_y, game_map, game_setup.objects = read_file(path)
        block = Block(game_setup.start_x, game_setup.start_y, "STAND", None, game_map)
        start_time = time.time()
        print("Testing level", level, " ..........")
        tracemalloc.start()
        solution = MCTS(block)
        memory_used, peak_memory = tracemalloc.get_traced_memory()
        if solution:
            cnt_success += 1
            print("Level ", str(level), ":     Found solution in    ", round(time.time() - start_time, 9), ("s"))
            print(f"Memory used: {memory_used} Bytes")
        else:
            print("Failed to find solution :( ")
            print("==========================================================")
        tracemalloc.stop()
    print(cnt_success ,"/33 level success")

def testAstart():
    cnt_success = 0
    for level in range(1,34):
        if level in [8,9,10,15,16,20,22,23,24,26, 28]: 
            print("Level ", str(level), ":    Time Limited")
            print("==========================================================")

            continue
        path = './levels/lvl' + str(level) + '.txt'
        game_setup.init()
        game_setup.row, game_setup.col, game_setup.start_x, \
            game_setup.start_y, game_map, game_setup.objects, \
                game_setup.goal_x, game_setup.goal_y= read_file_forAS(path)
        block = Block(game_setup.start_x, game_setup.start_y, "STAND", None, game_map)
        
        start_time = time.time()
        print("Testing level", level, " ..........")
        tracemalloc.start()

        a = Astar()
        solution = a.solve_by_astar(block)
        memory_used, peak_memory = tracemalloc.get_traced_memory()
        if solution:
            cnt_success += 1
            print("Level ", str(level), ":     Found solution in    ", round(time.time() - start_time, 9), ("s"))
            print(f"Memory used: {memory_used} Bytes")
        else:
            print("Failed to find solution :( ")
            print("==========================================================")
        tracemalloc.stop()
    print(cnt_success ,"/33 level success")