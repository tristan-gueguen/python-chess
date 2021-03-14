from .piece import Piece
from .move import Move
from ..utils import string_to_pos

class King(Piece):
    def __init__(self, is_white):
        Piece.__init__(self, is_white=is_white)
        self.symbol = 'k'

    def available_moves(self, curr_pos, board):
        naives = []

        naives.append((curr_pos[0] - 1, curr_pos[1] - 1))
        naives.append((curr_pos[0], curr_pos[1] - 1))
        naives.append((curr_pos[0] + 1, curr_pos[1] - 1))
        naives.append((curr_pos[0] - 1, curr_pos[1] + 1))
        naives.append((curr_pos[0], curr_pos[1] + 1))
        naives.append((curr_pos[0] + 1, curr_pos[1] + 1))
        naives.append((curr_pos[0] + 1, curr_pos[1]))
        naives.append((curr_pos[0] - 1, curr_pos[1]))
        naives = [m for m in naives if board.is_valid_cell(m)]
        moves = [m for m in naives if board.is_empty_cell(m)]
        takes = [m for m in naives if not board.is_empty_cell(m)]
        takes = [m for m in takes if board.pieces[m].is_white != self.is_white]
        # moves = ['K' + pos_to_string(p) for p in moves]
        # takes = ['Kx' + pos_to_string(p) for p in takes]
        # if string_to_pos('e1') == curr_pos:


        takes = [Move(self, curr_pos, m, is_take=True) for m in takes]
        moves = [Move(self, curr_pos, m, is_take=False) for m in moves]

        if self.is_white:
            if board.can_castle_q_positions_white():
                moves.append(Move(self, curr_pos, string_to_pos('c1')))
            if board.can_castle_k_positions_white():
                moves.append(Move(self, curr_pos, string_to_pos('g1')))
        else:
            if board.can_castle_q_positions_black():
                moves.append(Move(self, curr_pos, string_to_pos('c8')))
            if board.can_castle_k_positions_black():
                moves.append(Move(self, curr_pos, string_to_pos('g8')))

        return moves, takes
