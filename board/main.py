def pos_to_string(pos):
    row = pos[0]
    col = pos[1]
    return chr(97 + col) + str(row + 1)

def string_to_pos(str):
    letter = str[0]
    digit = int(str[1])
    return (digit - 1, ord(letter) - 97)

class Board:
    def __init__(self, white_to_play=True):
        self.pieces = {}
        self.white_to_play = white_to_play

    def add_piece(self, symbol, pos_str, is_white):
        pos = string_to_pos(pos_str)
        if pos in self.pieces:
            raise Exception('position + {} already taken'.format(pos))

        if symbol == 'b':
            piece = Bishop(is_white=is_white)
        elif symbol == 'p':
            piece = Pawn(is_white=is_white)
        elif symbol == 'n':
            piece = Knight(is_white=is_white)
        elif symbol == 'r':
            piece = Rook(is_white=is_white)
        elif symbol == 'q':
            piece = Queen(is_white=is_white)
        elif symbol == 'k':
            piece = King(is_white=is_white)
        else:
            raise Exception('symbol + {} not recognized'.format(symbol))
        self.pieces[pos] = piece

    def init_simple(self):
        self.add_piece('p', 'b1', is_white=True)

    def init_default(self):
        self.add_piece('r', 'a1', is_white=True)
        self.add_piece('n', 'b1', is_white=True)
        self.add_piece('b', 'c1', is_white=True)
        self.add_piece('q', 'd1', is_white=True)
        self.add_piece('k', 'e1', is_white=True)
        self.add_piece('b', 'f1', is_white=True)
        self.add_piece('n', 'g1', is_white=True)
        self.add_piece('r', 'h1', is_white=True)
        self.add_piece('p', 'a2', is_white=True)
        self.add_piece('p', 'b2', is_white=True)
        self.add_piece('p', 'c2', is_white=True)
        self.add_piece('p', 'd2', is_white=True)
        self.add_piece('p', 'e2', is_white=True)
        self.add_piece('p', 'f2', is_white=True)
        self.add_piece('p', 'g2', is_white=True)
        self.add_piece('p', 'h2', is_white=True)
        self.add_piece('p', 'a7', is_white=False)
        self.add_piece('p', 'b7', is_white=False)
        self.add_piece('p', 'c7', is_white=False)
        self.add_piece('p', 'd7', is_white=False)
        self.add_piece('p', 'e7', is_white=False)
        self.add_piece('p', 'f7', is_white=False)
        self.add_piece('p', 'g7', is_white=False)
        self.add_piece('p', 'h7', is_white=False)
        self.add_piece('r', 'a8', is_white=False)
        self.add_piece('n', 'b8', is_white=False)
        self.add_piece('b', 'c8', is_white=False)
        self.add_piece('q', 'd8', is_white=False)
        self.add_piece('k', 'e8', is_white=False)
        self.add_piece('b', 'f8', is_white=False)
        self.add_piece('n', 'g8', is_white=False)
        self.add_piece('r', 'h8', is_white=False)

    def init_fen(self, fen):
        parts = fen.split(' ')
        print(parts)
        self.white_to_play = parts[1] == 'w'

        row_idx = 0
        for row in reversed(parts[0].split('/')):
            col_idx = 0
            for c in row:
                if c.lower() in ['r', 'n', 'b', 'k', 'q', 'p']:
                    self.add_piece(c.lower(), pos_to_string((row_idx, col_idx)), c.isupper())
                elif c.isdigit():
                    nb_cells = int(c)
                    col_idx += nb_cells - 1
                col_idx += 1
            row_idx += 1


    def get_possible_moves(self):
        list_moves = []
        pieces_color = {pos: piece for (pos, piece) in self.pieces.items() if piece.is_white == self.white_to_play}
        for pos, piece in pieces_color.items():
            list_moves += piece.available_moves(pos, self)
        return list_moves

    def get_board(self):
        ret = []
        for col in reversed(range(8)):
            tmp_row = []
            for row in range(8):
                pos = (col, row)
                if pos in self.pieces:
                    tmp_row.append(self.pieces[pos].print_symbol())
                else:
                    tmp_row.append(('.'))
            ret.append(''.join(tmp_row))
        return ret

    def is_available_cell(self, pos):
        return self.is_empty_cell(pos) and self.is_valid_cell(pos)

    def is_empty_cell(self, pos):
        return pos not in self.pieces

    def is_valid_cell(self, pos):
        row = pos[0]
        col = pos[1]
        return row >= 0 and row <= 7 and col >= 0 and col <= 7

class Piece:
    def __init__(self, is_white):
        self.is_white = is_white

    def print_symbol(self):
        if self.is_white:
            return self.symbol.upper()
        return self.symbol

class Bishop(Piece):
    def __init__(self, is_white):
        Piece.__init__(self, is_white=is_white)
        self.symbol = 'b'

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

        takes = [m for m in consider_takes if board.pieces[m].is_white != self.is_white]
        takes = ['Bx' + pos_to_string(m) for m in takes]

        moves = ['B' + pos_to_string(p) for p in naives]

        # naives = [m for m in naives if board.is_available_cell(m)]
        return moves + takes

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
        takes = ['Qx' + pos_to_string(m) for m in takes]
        naives = [m for m in naives if board.is_available_cell(m)]

        moves = ['Q' + pos_to_string(p) for p in naives]
        return moves + takes

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
        moves = ['K' + pos_to_string(p) for p in moves]
        takes = ['Kx' + pos_to_string(p) for p in takes]
        return moves + takes

class Rook(Piece):
    def __init__(self, is_white):
        Piece.__init__(self, is_white=is_white)
        self.symbol = 'r'

    def available_moves(self, curr_pos, board):
        naives = []
        consider_takes = []
        curr_row = curr_pos[0]
        curr_col = curr_pos[1]

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
        takes = ['Rx' + pos_to_string(m) for m in takes]

        naives = [m for m in naives if board.is_available_cell(m)]
        moves = ['R' + pos_to_string(p) for p in naives]
        return moves + takes

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
        moves = ['N' + pos_to_string(p) for p in moves]
        takes = ['Nx' + pos_to_string(p) for p in takes]
        return moves + takes

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
        suffix_takes = pos_to_string(curr_pos)[0]
        takes = [suffix_takes + 'x' + pos_to_string(m) for m in pos_takes]
        moves = [pos_to_string(p) for p in naives]
        return moves + takes

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    b = Board()
    b.init_default()
    for r in b.get_board():
        print(r)
    moves = b.get_possible_moves()
    print("# moves: {}".format(len(moves)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
