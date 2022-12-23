from random import shuffle
from copy import deepcopy
class Game:
    def __init__(self):
        self.reset()
    
    def reset(self) -> None:
        self.board = [[1,2,3], [4,5,6],[7,8,0]]
    
    def copy(self):
        ret_val = Game()
        ret_val.board = deepcopy(self.board)
        return ret_val

    def legal_moves(self):
        r, c = self._find_zero()
        moves = set(["u", "d", "l", "r"])
        if r == 0:
            moves.remove("u")
        if r == 2:
            moves.remove("d")
        if c == 0:
            moves.remove("l")
        if c == 2:
            moves.remove("r")
        return moves
    
    #you insert the move you desire and you are returned
    def submit_move(self, move:str):
        offsets = {
            "l" : (0, -1),
            "r" : (0, +1),
            "u" : (-1, 0),
            "d" : (+1, 0)
        }
        horizontal, vertical = offsets[move]
        return self._after_move(horizontal, vertical)
    
    def submit_moves(self, moves:str):
        curr = self.copy()
        for move in moves:
            curr = curr.submit_move(move)
        return curr

    # all the moves you are allowed to make
    def all_moves(self):
        return [(move, self.submit_move(move)) for move in self.legal_moves()]
    
    # state of the board after submitting a move
    def _after_move(self, horizontal:int, vertical:int):
        ret_val = self.copy()
        r,c = ret_val._find_zero()
        ret_val._switch(r, c, r + horizontal, c + vertical)
        return ret_val
    
    # finds pos of the zero
    def _find_zero(self) -> (int, int):
        for r, row in enumerate(self.board):
            for c, elem in enumerate(row):
                if elem == 0:
                    return (r, c)
    # switches the position of two letters
    def _switch(self, r1:int, c1:int, r2:int, c2:int) -> None:
        self.board[r1][c1], self.board[r2][c2] = self.board[r2][c2], self.board[r1][c1]

    
    def __str__(self) -> str:
        return str(self.board[0]) + "\n" + str(self.board[1]) + "\n" + str(self.board[2]) + "\n"

g = Game()
gae = g.all_moves()

for move, board in gae:
    print(f"{move} :\n{board}")

print(g.submit_moves("lluurd"))