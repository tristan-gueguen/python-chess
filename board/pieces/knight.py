from .piece import Piece
from .move import Move

class Knight(Piece):
    def __init__(self, is_white):
        Piece.__init__(self, is_white=is_white)
        self.symbol = 'n'

    def available_moves(self, curr_pos, board):
        candidates = []
        curr_row = curr_pos[0]
        curr_col = curr_pos[1]
        candidates.append((curr_row + 1, curr_col + 2))
        candidates.append((curr_row + 1, curr_col - 2))
        candidates.append((curr_row - 1, curr_col + 2))
        candidates.append((curr_row - 1, curr_col - 2))
        candidates.append((curr_row + 2, curr_col + 1))
        candidates.append((curr_row - 2, curr_col + 1))
        candidates.append((curr_row + 2, curr_col - 1))
        candidates.append((curr_row - 2, curr_col - 1))
        candidates = [m for m in candidates if board.is_valid_cell(m)]

        moves = [m for m in candidates if board.is_empty_cell(m)]
        takes = [m for m in candidates if not board.is_empty_cell(m)]
        takes = [m for m in takes if board.pieces[m].is_white != self.is_white]
        # moves = ['N' + pos_to_string(p) for p in moves]
        # takes = ['Nx' + pos_to_string(p) for p in takes]

        takes = [Move(self, curr_pos, m, is_take=True) for m in takes]
        moves = [Move(self, curr_pos, m, is_take=False) for m in moves]
        return moves, takes
