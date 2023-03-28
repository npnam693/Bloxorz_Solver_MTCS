import game_setup
class Block:
    def __init__(self, x, y, status, prev, game_map, x_split=None, y_split=None, id=0, map=""):
        self.x = x
        self.y = y
        self.status = status
        self.prev = prev
        self.game_map = [x[:] for x in game_map]  # copy
        self.x_split = x_split
        self.y_split = y_split
        self.id = id
        self.map = ''.join(''.join(l) for l in self.game_map)

    def move_up(self):
        game_setup.block_id += 1
        new_block = Block(self.x, self.y, self.status, self, self.game_map, id=game_setup.block_id)
        if self.status == "STAND":
            new_block.y -= 2
            new_block.status = "VERTICAL"
        elif self.status == "VERTICAL":
            new_block.y -= 1
            new_block.status = "STAND"
        elif self.status == "HORIZONTAL":
            new_block.y -= 1

        return new_block

    def move_right(self):
        game_setup.block_id += 1
        new_block = Block(self.x, self.y, self.status, self, self.game_map, id=game_setup.block_id)

        if self.status == "STAND":
            new_block.x += 1
            new_block.status = "HORIZONTAL"

        if self.status == "VERTICAL":
            new_block.x += 1

        if self.status == "HORIZONTAL":
            new_block.x += 2
            new_block.status = "STAND"

        return new_block

    def move_left(self):
        game_setup.block_id += 1
        new_block = Block(self.x, self.y, self.status, self, self.game_map, id=game_setup.block_id)

        if self.status == "STAND":
            new_block.x -= 2
            new_block.status = "HORIZONTAL"

        if self.status == "HORIZONTAL":
            new_block.x -= 1
            new_block.status = "STAND"

        if self.status == "VERTICAL":
            new_block.x -= 1

        return new_block

    def move_down(self):
        game_setup.block_id += 1
        new_block = Block(self.x, self.y, self.status, self, self.game_map, id=game_setup.block_id)

        if self.status == "STAND":
            new_block.y += 1
            new_block.status = "VERTICAL"

        if self.status == "VERTICAL":
            new_block.y += 2
            new_block.status = "STAND"

        if self.status == "HORIZONTAL":
            new_block.y += 1

        return new_block

    def S1_move_up(self):
        game_setup.block_id += 1
        new_block = Block(self.x, self.y, self.status, self, self.game_map,
                          self.x_split, self.y_split, id=game_setup.block_id)
        new_block.y -= 1
        return new_block

    def S1_move_right(self):
        game_setup.block_id += 1
        new_block = Block(self.x, self.y, self.status, self, self.game_map,
                          self.x_split, self.y_split, id=game_setup.block_id)
        new_block.x += 1

        return new_block

    def S1_move_left(self):
        game_setup.block_id += 1
        new_block = Block(self.x, self.y, self.status, self, self.game_map,
                          self.x_split, self.y_split, id=game_setup.block_id)
        new_block.x -= 1

        return new_block

    def S1_move_down(self):
        game_setup.block_id += 1
        new_block = Block(self.x, self.y, self.status, self, self.game_map,
                          self.x_split, self.y_split, id=game_setup.block_id)
        new_block.y += 1

        return new_block

    # split other
    def S2_move_up(self):
        game_setup.block_id += 1
        new_block = Block(self.x, self.y, self.status, self, self.game_map,
                          self.x_split, self.y_split, id=game_setup.block_id)
        new_block.y_split -= 1

        return new_block

    def S2_move_right(self):
        game_setup.block_id += 1
        new_block = Block(self.x, self.y, self.status, self, self.game_map,
                          self.x_split, self.y_split, id=game_setup.block_id)
        new_block.x_split += 1

        return new_block

    def S2_move_left(self):
        game_setup.block_id += 1
        new_block = Block(self.x, self.y, self.status, self, self.game_map,
                          self.x_split, self.y_split, id=game_setup.block_id)
        new_block.x_split -= 1

        return new_block

    def S2_move_down(self):
        game_setup.block_id += 1
        new_block = Block(self.x, self.y, self.status, self, self.game_map,
                          self.x_split, self.y_split, id=game_setup.block_id)
        new_block.y_split += 1

        return new_block

    def print_state(self):
        if self.status != "SPLIT":
            print(self.status, self.x, self.y)
        else:
            print(self.status, self.x, self.y, self.x_split, self.y_split)

    def print_map(self):
        x = self.x
        y = self.y
        x_split = self.x_split
        y_split = self.y_split
        status = self.status
        game_map = self.game_map
        if status != "SPLIT":
            for i in range(len(game_map)):
                print("", end='  ')
                for j in range(len(game_map[i])):
                    if (i == y and j == x and status == "STAND") \
                            or ((i == y and j == x) or (i == y and j == x + 1) and status == "HORIZONTAL") \
                            or ((i == y and j == x) or (i == y + 1 and j == x) and status == "VERTICAL"):

                        print("+", end=' ')

                    elif game_map[i][j] == '.':
                        print(" ", end=' ')
                    else:
                        print(game_map[i][j], end=' ')
                print("")
        else:
            for i in range(len(game_map)):
                print("", end='  ')
                for j in range(len(game_map[i])):
                    if (i == y and j == x) or (i == y_split and j == x_split):
                        print("+", end=' ')
                    elif game_map[i][j] == ".":
                        print(" ", end=' ')
                    else:
                        print(game_map[i][j], end=' ')
                print("")