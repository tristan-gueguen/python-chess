from .piece import Piece
from .move import Move

class Queen(Piece):
    def __init__(self, is_white):
        Piece.__init__(self, is_white=is_white)
        self.symbol = 'q'

    def available_moves(self, curr_pos, board):
        naives = []
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
            naives.append(pos)
            tmp_row += 1
            tmp_col += 1

        tmp_row = curr_row - 1
        tmp_col = curr_col - 1
        while tmp_row >= 0 and tmp_col >= 0:
            pos = (tmp_row, tmp_col)
            if not board.is_empty_cell(pos):
                consider_takes.append(pos)
                break
            naives.append(pos)
            tmp_row -= 1
            tmp_col -= 1

        tmp_row = curr_row + 1
        tmp_col = curr_col - 1
        while tmp_row < 8 and tmp_col >= 0:
            pos = (tmp_row, tmp_col)
            if not board.is_empty_cell(pos):
                consider_takes.append(pos)
                break
            naives.append(pos)
            tmp_row += 1
            tmp_col -= 1

        tmp_row = curr_row - 1
        tmp_col = curr_col + 1
        while tmp_row >= 0 and tmp_col < 8:
            pos = (tmp_row, tmp_col)
            if not board.is_empty_cell(pos):
                consider_takes.append(pos)
                break
            naives.append(pos)
            tmp_row -= 1
            tmp_col += 1

        tmp_row = curr_row + 1
        while tmp_row < 8:
            pos = (tmp_row, curr_col)
            if not board.is_empty_cell(pos):
                consider_takes.append(pos)
                break
            naives.append(pos)
            tmp_row += 1

        tmp_row = curr_row - 1
        while tmp_row >= 0:
            pos = (tmp_row, curr_col)
            if not board.is_empty_cell(pos):
                consider_takes.append(pos)
                break
            naives.append(pos)
            tmp_row -= 1

        tmp_col = curr_col + 1
        while tmp_col < 8:
            pos = (curr_row, tmp_col)
            if not board.is_empty_cell(pos):
                consider_takes.append(pos)
                break
            naives.append(pos)
            tmp_col += 1

        tmp_col = curr_col - 1
        while tmp_col >= 0:
            pos = (curr_row, tmp_col)
            if not board.is_empty_cell(pos):
                consider_takes.append(pos)
                break
            naives.append(pos)
            tmp_col -= 1

        takes = [m for m in consider_takes if board.pieces[m].is_white != self.is_white]
        naives = [m for m in naives if board.is_available_cell(m)]
        takes = [Move(self, curr_pos, m, is_take=True) for m in takes]
        moves = [Move(self, curr_pos, m, is_take=False) for m in naives]

        return moves, takes
