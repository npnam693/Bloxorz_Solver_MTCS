import math
import random
from functions import is_win, process_state, is_valid_move
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
def random_action(block):
        if block.status != 'SPLIT':
            actions = [block.move_up(), block.move_right(), block.move_down(), block.move_left()]
        else:
            actions = [block.S1_move_up(), block.S1_move_right(),
                    block.S1_move_down(), block.S1_move_left(), 
                    block.S2_move_up(), block.S2_move_right(),
                    block.S2_move_down(), block.S2_move_left()]
        return random.choice(actions)

class Node:
    def __init__(self, block, parent=None):
        self.block = block
        self.parent = parent
        self.children = []
        self.is_visited = False
        self.is_generate_children = False
        self.wins = 0
        self.games = 0
        self.countNode = 1,
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
        return None
    
    def generate_childrens(self, countNode):
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
                countNode[0]+=1
                self.children.append(newChild)
    
    def select_child(self, countNode):
        # Child nodes have not been generated yet
        if not self.is_generate_children:
            self.is_generate_children = True
            self.generate_childrens(countNode)
        # Can't generate child nodes (all action are invalid)
        if (len(self.children) == 0): 
            self.propagate(False)
            return None        
        # Node hasn't been fully expansion yet.
        for child in self.children:
            if not child.is_visited:
                child.is_visited = True
                return child
        ln_games = math.log(self.games)
        def uct_score(child):
            return (child.wins / child.games) + 1.41 * math.sqrt(ln_games / child.games)
        good_child = max(self.children, key=uct_score)
        return good_child.select_child(countNode)

    def simulate(self):
        numAction_limit = 200
        block = self.block
        # Save the states of the simulation
        listBlock = [block]
        temp = self.parent
        while temp:
            listBlock.append(temp.block)
            temp = temp.parent
        while numAction_limit > 0:
            numAction_limit -= 1
            block = random_action(block)
            if block is None: return False
            if(not is_valid_move(block)): return False
            else: process_state(block)
            if(check_existed_block(block, listBlock)): return False
            listBlock.append(block)
            if is_win(block):return True
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

def MCTS(block):
    root_node = Node(block, None)
    iterator = 0
    countNode = [0]
    while True:
        iterator += 1
        node = root_node.select_child(countNode)
        if (node is None): continue
        if is_win(node.block):
            return get_solution(node)
        resultSimulate = node.simulate()
        node.propagate(resultSimulate)


