import math
import random
from functions import is_win, process_state
def check_existed_block(block, listBlock):
    if block.status != "SPLIT":
        for i in listBlock:
            if i.x == block.x and i.y == block.y \
                    and i.status == block.status and i.game_map == block.game_map:
                return True
    else:
        for i in listBlock:
            if i.x == block.x and i.y == block.y \
                    and i.x_split == block.x_split and i.y_split == block.y_split \
                    and i.status == block.status and i.game_map == block.game_map:
                return True
    return False
def random_action_valid(block, listBlock):
        valid_actions = []
        if block.status != 'SPLIT':
            actions = [block.move_up(), block.move_right(), block.move_down(), block.move_left()]
        else:
            actions = [block.S1_move_up(), block.S1_move_right(),
                    block.S1_move_down(), block.S1_move_left(), 
                    block.S2_move_up(), block.S2_move_right(),
                    block.S2_move_down(), block.S2_move_left()]
        
        for action in actions:
            if process_state(action):
                if not check_existed_block(action, listBlock):
                    valid_actions.append(action)

        if len(valid_actions) == 0: return None
        return random.choice(valid_actions)
class Node:
    def __init__(self, block, parent=None):
        self.block = block
        self.parent = parent
        self.children = []
        self.is_visited = False
        self.is_generate_children = False
        self.wins = 0
        self.games = 0

    def is_existed(self, block):
        curNode = self
        if curNode.block.status != "SPLIT":        
            while(curNode):
                if block.x == curNode.block.x and block.y == curNode.block.y \
                    and block.status == curNode.block.status and block.game_map == curNode.block.game_map:
                        return True
                else: curNode = curNode.parent
        else:
             while(curNode):
                if block.x == curNode.block.x and block.y == curNode.block.y \
                    and block.x_split == curNode.block.x_split and block.y_split == curNode.block.y_split \
                    and block.status == curNode.block.status and block.game_map == curNode.block.game_map:
                        return True
                else: curNode = curNode.parent
        return False     
    def gen_child(self, block, parent):
        if process_state(block):
            if self.is_existed(block):
               return None
            else: return Node(block, parent) 
    def generate_childrens(self):
        if self.block.status != 'SPLIT':
            actions = [self.block.move_up(), self.block.move_right(), self.block.move_down(), self.block.move_left()]
        else:
            actions = [self.block.S1_move_up(), self.block.S1_move_right(),
                    self.block.S1_move_down(), self.block.S1_move_left(), 
                    self.block.S2_move_up(), self.block.S2_move_right(),
                    self.block.S2_move_down(), self.block.S2_move_left()
                    ]
        for action in actions:
            newChild = self.gen_child(action, self)
            if newChild is not None:
                self.children.append(newChild)
    
    def select_child(self):
        # Chua sinh ra cac node con
        if not self.is_generate_children:
            self.is_generate_children = True
            self.generate_childrens()
        # Khong the sinh ra node con moi (cac action deu khong hop le)
        if (len(self.children) == 0): 
            self.propagate(False)
            return None        
        # Cay chua fully_exspansion
        for child in self.children:
            if not child.is_visited:
                child.is_visited = True
                return child
        ln_games = math.log(self.games)
        def ucb_score(child):
            return (child.wins / child.games) + 0.5 * math.sqrt(ln_games / child.games)
        good_child = max(self.children, key=ucb_score)
        return good_child.select_child()

    def simulate(self):
        numAction_limit = 100
        block = self.block
        # Luu tru cac trang thai da di qua
        listBlock = [block]
        temp = self.parent
        while temp:
            listBlock.append(temp.block)
            temp = temp.parent
        while numAction_limit > 0:
            numAction_limit -= 1
            block = random_action_valid(block, listBlock)
            if block is None: 
                return False
            listBlock.append(block)
            if is_win(block):
                print('winwinwinwinwinwinwinwinwinwinwinwinwinwinwinwin')
                return True
        return False


    def propagate(self, is_win):
        self.games += 1
        self.wins = self.wins + 1 if is_win else self.wins
        if self.parent is not None:
            self.parent.propagate(is_win)


def get_solution(node):
    solution = [node.block]
    temp = node.parent
    while temp is not None:
        solution.append(temp.block)
        temp = temp.parent
    solution.reverse()
    return solution

def monte_carlo_tree_search_new(block):
    root_node = Node(block, None)
    iterator = 0
    while True:
        iterator += 1
        node = root_node.select_child()
        if (node is None): continue
        if is_win(node.block):
            return get_solution(node)
        is_win = node.simulate()
        node.propagate(is_win)
        print(f'end iterator {iterator}')