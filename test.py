import game_setup
from read_level_input import read_file
from block import Block
from BFS_algorithm import BFS
import time
import tracemalloc

def test():
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
            # with open('test_result.txt', 'a') as f:
            #     print('success\n''Level ', str(level), ":     \
            #     Found solution in    ", round(time.time() - start_time, 9), '("s")', file=f)
            print("Level ", str(level), ":     Found solution in    ", round(time.time() - start_time, 9), ("s"))
            print(f"Memory used: {memory_used} Bytes")
        else:
            print("Failed to find solution :( ")
        print("===========================================")
        tracemalloc.stop()
    print(cnt_success ,"/33 level success")