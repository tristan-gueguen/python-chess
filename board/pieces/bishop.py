from .piece import Piece
from .move import Move

class Bishop(Piece):
    def __init__(self, is_white):
        Piece.__init__(self, is_white=is_white)
        self.symbol = 'b'

    def available_moves(self, curr_pos, board):
        moves = []
        consider_takes = []
        curr_row = curr_pos[0]
        curr_col = curr_pos[1]

        tmp_row = curr_row + 1
        tmp_col = curr_col + 1
        while tmp_row < 8 and tmp_col < 8:
            pos = (tmp_row, tmp_col)
            if not board.is_empty_cell(pos):
                consider_takes.append(pos)
                break
            moves.append(pos)
            tmp_row += 1
            tmp_col += 1

        tmp_row = curr_row - 1
        tmp_col = curr_col - 1
        while tmp_row >= 0 and tmp_col >= 0:
            pos = (tmp_row, tmp_col)
            if not board.is_empty_cell(pos):
                consider_takes.append(pos)
                break
            moves.append(pos)
            tmp_row -= 1
            tmp_col -= 1

        tmp_row = curr_row + 1
        tmp_col = curr_col - 1
        while tmp_row < 8 and tmp_col >= 0:
            pos = (tmp_row, tmp_col)
            if not board.is_empty_cell(pos):
                consider_takes.append(pos)
                break
            moves.append(pos)
            tmp_row += 1
            tmp_col -= 1

        tmp_row = curr_row - 1
        tmp_col = curr_col + 1
        while tmp_row >= 0 and tmp_col < 8:
            pos = (tmp_row, tmp_col)
            if not board.is_empty_cell(pos):
                consider_takes.append(pos)
                break
            moves.append(pos)
            tmp_row -= 1
            tmp_col += 1

        takes = [m for m in consider_takes if board.pieces[m].is_white != self.is_white]
        # takes = ['Bx' + pos_to_string(m) for m in takes]
        takes = [Move(self, curr_pos, m, is_take=True) for m in takes]

        # moves = ['B' + pos_to_string(p) for p in naives]
        moves = [Move(self, curr_pos, m, is_take=False) for m in moves]
        return (moves, takes)
