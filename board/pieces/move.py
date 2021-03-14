from ..utils import pos_to_string

class Move:
    def __init__(self, piece, from_pos, to_pos, is_take=False):
        self.piece = piece
        self.from_pos = from_pos
        self.to_pos = to_pos
        self.is_take = is_take

    def to_string(self):
        if self.piece.symbol.upper() == 'K':
            if pos_to_string(self.from_pos) == 'e1' and pos_to_string(self.to_pos) == 'g1':
                return 'O-O'
            if pos_to_string(self.from_pos) == 'e1' and pos_to_string(self.to_pos) == 'c1':
                return 'O-O-O'
            if pos_to_string(self.from_pos) == 'e8' and pos_to_string(self.to_pos) == 'g8':
                return 'O-O'
            if pos_to_string(self.from_pos) == 'e8' and pos_to_string(self.to_pos) == 'c8':
                return 'O-O-O'

        str_takes = ''
        if self.is_take:
            str_takes = 'x'
        str_piece = ''
        if self.piece.symbol.upper() != 'P':
            str_piece = self.piece.symbol.upper()
        else:
            if self.is_take:
                str_piece = pos_to_string(self.from_pos)[0]
        return str_piece + str_takes + pos_to_string(self.to_pos)

    # def __str__(self):
    #     return self.piece_symbol
