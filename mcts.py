import math
import random
from functions import is_valid_move, is_win, process_state
def getFloor(node):
    res = 0
    while(node.parent):
        res = res + 1
        node = node.parent
    return res

def random_valid_step(block, list_step):
    if block.status != 'SPLIT':
        steps = [block.move_up(), block.move_right(), block.move_down(), block.move_left()]
        valid_steps = []
        for step in steps:
            if (is_valid_move(step) and not check_is_duplicate_step(step, list_step) ):
                valid_steps.append(step)
        if len(valid_steps) == 0: return None
        return random.choice(valid_steps)
    else:
        steps = [block.S1_move_up(), block.S1_move_right(), block.S1_move_down(),
                block.S1_move_left(), block.S2_move_up(), block.S2_move_right(),
                block.S2_move_down(), block.S2_move_left()]
        valid_steps = []
        
        for step in steps:
            if (is_valid_move(step) and not check_is_duplicate_step(step, list_step) ):
                valid_steps.append(step)
        if len(valid_steps) == 0: return None
        
        return random.choice(valid_steps)

def check_is_duplicate_step(step, list_step):
    if step.status != "SPLIT":
        for i in list_step:
            if i.x == step.x and i.y == step.y \
                    and i.status == step.status and i.game_map == step.game_map:
                return True
    else:
        for i in list_step:
            if i.x == step.x and i.y == step.y \
                    and i.x_split == step.x_split and i.y_split == step.y_split \
                    and i.status == step.status and i.game_map == step.game_map:
                return True
    return False

class Node:
    def __init__(self, current, prev):
        self.current = current
        self.wins = 0
        self.games = 0
        self.parent = prev
        self.childs = []
        self.is_visited = False
        self.is_generate_childs = False
    def generate_childs(self):
        if self.current.status != 'SPLIT':
            if is_valid_move(self.current.move_up()) and not Node(self.current.move_up(), self).is_existed():
                self.childs.append(Node(self.current.move_up(), self))
            if is_valid_move(self.current.move_right()) and not Node(self.current.move_right(), self).is_existed():
                self.childs.append(Node(self.current.move_right(), self))
            if is_valid_move(self.current.move_down()) and not Node(self.current.move_down(), self).is_existed():
                self.childs.append(Node(self.current.move_down(), self))
            if is_valid_move(self.current.move_left()) and not Node(self.current.move_left(), self).is_existed():
                self.childs.append(Node(self.current.move_left(), self))
        else:
            if is_valid_move(self.current.S1_move_up()) and not Node(self.current.S1_move_up(), self).is_existed():
                self.childs.append(Node(self.current.S1_move_up(), self))
            if is_valid_move(self.current.S1_move_right()) and not Node(self.current.S1_move_right(), self).is_existed():
                self.childs.append(Node(self.current.S1_move_right(), self))
            if is_valid_move(self.current.S1_move_down()) and not Node(self.current.S1_move_down(), self).is_existed():
                self.childs.append(Node(self.current.S1_move_down(), self))
            if is_valid_move(self.current.S1_move_left()) and not Node(self.current.S1_move_left(), self).is_existed():
                self.childs.append(Node(self.current.S1_move_left(), self))

            if is_valid_move(self.current.S2_move_up()) and not Node(self.current.S2_move_up(), self).is_existed():
                self.childs.append(Node(self.current.S2_move_up(), self))
            if is_valid_move(self.current.S2_move_right()) and not Node(self.current.S2_move_right(), self).is_existed():
                self.childs.append(Node(self.current.S2_move_right(), self))
            if is_valid_move(self.current.S2_move_down()) and not Node(self.current.S2_move_down(), self).is_existed():
                self.childs.append(Node(self.current.S2_move_down(), self))
            if is_valid_move(self.current.S2_move_left()) and not Node(self.current.S2_move_left(), self).is_existed():
                self.childs.append(Node(self.current.S2_move_left(), self))

    def propagate(self, is_win):
        self.games += 1
        self.wins = self.wins + 1 if is_win else self.wins

        if self.parent is not None:
            self.parent.propagate(is_win)

    # def simulate(self):
    #     iterator = 100
    #     step = self.current
    #     while iterator:
    #         iterator -= 1
    #         step = random_valid_step(step)
    #         if is_win(step):
    #             return True
    #     return False

    def simulate(self):
        iterator = 100
        step = self.current
        list_step = [self.current]
        tmp = self.parent
        while tmp is not None:
            list_step.append(tmp.current)
            tmp = tmp.parent
        while iterator:
            iterator -= 1
            # step = random_step(step)
            # if not is_valid_move(step):
            #     return False
            step = random_valid_step(step, list_step)
            if (step is None): 
                print('huuhuhuhu')
                return False
            if not process_state(step):
                return False

            list_step.append(step)
            if is_win(step):
                print('winwinwinwinwinwinwinwinwinwinwinwinwinwinwinwin')
                return True
        print('lose')
        return False

    def select_child(self):
        if not self.is_generate_childs:
            self.is_generate_childs = True
            self.generate_childs()
        if (len(self.childs) == 0): 
            self.propagate(False)
            # print('ceccecec')
            return None        
        for child in self.childs:
            if not child.is_visited:
                child.is_visited = True
                return child
        
        ln_games = math.log(self.games)
        
        def ucb_score(child):
            return (child.wins / child.games) + 1.41 * math.sqrt(ln_games / child.games)

        good_child = max(self.childs, key=ucb_score)
        return good_child.select_child()

    def is_existed(self):
        curNode = self
        if curNode.current.status != "SPLIT":        
            while(curNode.parent):
                if self.current.x == curNode.parent.current.x and self.current.y == curNode.parent.current.y \
                        and self.current.status == curNode.parent.current.status and self.current.game_map == curNode.parent.current.game_map:
                    return True
                else: curNode = curNode.parent
        else:
             while(curNode.parent):
                if self.current.x == curNode.parent.current.x and self.current.y == curNode.parent.current.y \
                        and self.current.x_split == curNode.parent.current.x_split and self.current.y_split == curNode.parent.current.y_split \
                        and self.current.status == curNode.parent.current.status and self.current.game_map == curNode.parent.current.game_map:
                    return True
                else: curNode = curNode.parent
        return False                



def get_solution(node):
    solution = [node.current]
    temp = node.parent
    while temp is not None:
        solution.append(temp.current)
        temp = temp.parent
    solution.reverse()
    return solution

def monte_carlo_tree_search(block):
    root_node = Node(block, None)
    iterator = 0
    while True:
        iterator += 1
        node = root_node.select_child()
        if (node is None): continue
        process_state(node.current)
        print(getFloor(node))
        if is_win(node.current):
            print(node.current.x, node.current.y)
            return get_solution(node)
        is_win = node.simulate()
        node.propagate(is_win)
        print(f'end iterator {iterator}')

