from .piece import Piece
from .move import Move
from ..utils import pos_to_string

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

        take_en_passant = [m for m in pos_takes if board.en_passant == pos_to_string(m)]
        other_takes = [m for m in pos_takes if not board.is_empty_cell(m)]
        other_takes = [m for m in other_takes if board.pieces[m].is_white != self.is_white]
        takes = take_en_passant + other_takes

        last_row = 7 if self.is_white else 0
        def_takes = []
        for t in takes:
            if t[0] == last_row:
                for s in ['Q', 'B', 'N', 'R']:
                    def_takes.append(Move(from_pos=curr_pos, to_pos=t, is_take=True, piece=self, prom_str=s))
            else:
                def_takes.append(Move(from_pos=curr_pos, to_pos=t, is_take=True, piece=self))

        def_moves = []
        for m in naives:
            if m[0] == last_row:
                for s in ['Q', 'B', 'N', 'R']:
                    def_moves.append(Move(from_pos=curr_pos, to_pos=m, is_take=False, piece=self, prom_str=s))
            else:
                def_moves.append(Move(from_pos=curr_pos, to_pos=m, is_take=False, piece=self))

        return def_moves, def_takes
