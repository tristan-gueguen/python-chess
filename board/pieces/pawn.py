from .piece import Piece
from .move import Move

class Pawn(Piece):
    def __init__(self, is_white):
        Piece.__init__(self, is_white=is_white)
        self.symbol = 'p'

    def available_moves(self, curr_pos, board):
        naives = []
        takes = []
        if self.is_white:
            pos = (curr_pos[0] + 1, curr_pos[1])
            if board.is_empty_cell(pos):
                naives.append(pos)
                if curr_pos[0] == 1:
                    pos = (curr_pos[0] + 2, curr_pos[1])
                    if board.is_empty_cell(pos):
                        naives.append(pos)
            pos_takes = [(curr_pos[0] + 1, curr_pos[1] + 1), (curr_pos[0] + 1, curr_pos[1] - 1)]
        else:
            pos = (curr_pos[0] - 1, curr_pos[1])
            if board.is_empty_cell(pos):
                naives.append(pos)
                if curr_pos[0] == 6:
                    pos = (curr_pos[0] - 2, curr_pos[1])
                    if board.is_empty_cell(pos):
                        naives.append(pos)
            pos_takes = [(curr_pos[0] - 1, curr_pos[1] + 1), (curr_pos[0] - 1, curr_pos[1] - 1)]
        naives = [m for m in naives if board.is_valid_cell(m)]

        pos_takes = [m for m in pos_takes if not board.is_empty_cell(m)]
        pos_takes = [m for m in pos_takes if board.pieces[m].is_white != self.is_white]
        takes = [Move(from_pos=curr_pos, to_pos=m, is_take=True, piece=self) for m in pos_takes]
        moves = [Move(piece=self, from_pos=curr_pos, to_pos=m, is_take=False) for m in naives]
        return moves, takes
