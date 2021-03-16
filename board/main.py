import copy

from flask import jsonify

from .pieces import Pawn
from .pieces import Queen
from .pieces import King
from .pieces import Bishop
from .pieces import Rook
from .pieces import Knight
from .utils import pos_to_string
from .utils import string_to_pos

class Board:
    def __init__(self, white_to_play=True):
        self.pieces = {}
        self.white_to_play = white_to_play
        self.black_can_castle_q = True
        self.black_can_castle_k = True
        self.white_can_castle_q = True
        self.white_can_castle_k = True
        self.en_passant = '-'

    def reset(self):
        self.pieces = {}
        self.white_to_play = True
        self.black_can_castle_q = True
        self.black_can_castle_k = True
        self.white_can_castle_q = True
        self.white_can_castle_k = True
        self.en_passant = '-'


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
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.init_fen(fen)

    def init_fen(self, fen):
        self.reset()
        parts = fen.split(' ')
        self.white_to_play = parts[1] == 'w'

        self.en_passant = parts[3]

        castles = parts[2]
        self.black_can_castle_q = 'q' in castles
        self.black_can_castle_k = 'k' in castles
        self.white_can_castle_q = 'Q' in castles
        self.white_can_castle_k = 'K' in castles

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

    # find moves, without checking is there would be a check
    def get_naive_moves(self, from_white):
        moves = []
        takes = []
        pieces_color = {pos: piece for (pos, piece) in self.pieces.items() if piece.is_white == from_white}
        for pos, piece in pieces_color.items():
            tmpMoves, tmpTakes = piece.available_moves(pos, self)
            moves += tmpMoves
            takes += tmpTakes
        return moves + takes

    def remove_would_check_moves(self, moves, white_to_play):
        ret = []
        for m in moves:
            copy_board = copy.deepcopy(self)
            del copy_board.pieces[m.from_pos]
            copy_board.pieces[m.to_pos] = m.piece
            is_check = copy_board.is_check(white_to_play)
            if not is_check:
                ret.append(m)
        return ret

    def can_castle_k_positions_white(self):
        if self.get_king_position(white_king=True) != 'e1':
            return False
        if not self.is_empty_cell(string_to_pos('f1')):
            return False
        if not self.is_empty_cell(string_to_pos('g1')):
            return False
        if self.is_empty_cell(string_to_pos('h1')):
            return False
        if self.pieces[string_to_pos('h1')].symbol != 'r':
            return False
        return True

    def can_castle_q_positions_white(self):
        print('can_castle_q_positions_white')
        if self.get_king_position(white_king=True) != 'e1':
            print('king not in position')
            return False
        if not self.is_empty_cell(string_to_pos('d1')):
            print('d1 not empty')
            return False
        if not self.is_empty_cell(string_to_pos('c1')):
            print('c1 not empty')
            return False
        if not self.is_empty_cell(string_to_pos('b1')):
            print('b1 not empty')
            return False
        if self.is_empty_cell(string_to_pos('a1')):
            print('a1 empty')
            return False
        if self.pieces[string_to_pos('a1')].symbol != 'r':
            print('a1 not a rook')
            return False
        return True

    def can_castle_k_positions_black(self):
        if self.get_king_position(white_king=False) != 'e8':
            return False
        if not self.is_empty_cell(string_to_pos('f8')):
            return False
        if not self.is_empty_cell(string_to_pos('g8')):
            return False
        if self.is_empty_cell(string_to_pos('h8')):
            return False
        if self.pieces[string_to_pos('h8')].symbol != 'r':
            return False
        return True

    def can_castle_q_positions_black(self):
        if self.get_king_position(white_king=False) != 'e8':
            return False
        if not self.is_empty_cell(string_to_pos('d8')):
            return False
        if not self.is_empty_cell(string_to_pos('c8')):
            return False
        if not self.is_empty_cell(string_to_pos('b8')):
            return False
        if self.is_empty_cell(string_to_pos('a8')):
            return False
        if self.pieces[string_to_pos('a8')].symbol != 'r':
            return False
        return True


    def can_castle_q_white(self):
        if not self.white_can_castle_q:
            return False
        if self.is_check(against_white=True):
            return False

        copy_board = copy.deepcopy(self)
        del copy_board.pieces[string_to_pos('e1')]
        copy_board.add_piece('k', 'd1', is_white=True)
        if copy_board.is_check(against_white=True):
            return False

        copy_board = copy.deepcopy(self)
        del copy_board.pieces[string_to_pos('e1')]
        copy_board.add_piece('k', 'c1', is_white=True)
        if copy_board.is_check(against_white=True):
            return False

        return True

    def can_castle_k_white(self):
        if not self.white_can_castle_k:
            return False
        if self.is_check(against_white=True):
            return False

        copy_board = copy.deepcopy(self)
        del copy_board.pieces[string_to_pos('e1')]
        copy_board.add_piece('k', 'f1', is_white=True)
        if copy_board.is_check(against_white=True):
            return False

        copy_board = copy.deepcopy(self)
        del copy_board.pieces[string_to_pos('e1')]
        copy_board.add_piece('k', 'g1', is_white=True)
        if copy_board.is_check(against_white=True):
            return False

        return True

    def can_castle_q_black(self):
        if not self.black_can_castle_q:
            return False
        if self.is_check(against_white=False):
            return False

        copy_board = copy.deepcopy(self)
        del copy_board.pieces[string_to_pos('e8')]
        copy_board.add_piece('k', 'f8', is_white=False)
        if copy_board.is_check(against_white=False):
            return False

        copy_board = copy.deepcopy(self)
        del copy_board.pieces[string_to_pos('e8')]
        copy_board.add_piece('k', 'g8', is_white=False)
        if copy_board.is_check(against_white=False):
            return False

        return True

    def can_castle_k_black(self):
        if not self.black_can_castle_k:
            return False
        if self.is_check(against_white=False):
            return False

        copy_board = copy.deepcopy(self)
        del copy_board.pieces[string_to_pos('e8')]
        copy_board.add_piece('k', 'd8', is_white=False)
        if copy_board.is_check(against_white=False):
            return False

        copy_board = copy.deepcopy(self)
        del copy_board.pieces[string_to_pos('e8')]
        copy_board.add_piece('k', 'c8', is_white=False)
        if copy_board.is_check(against_white=False):
            return False

        return True

    def remove_illegal_castle(self, moves, white_to_play):
        ret = []
        for m in moves:
            if m.to_string() == 'O-O':
                if white_to_play:
                    if self.can_castle_k_white():
                        ret.append(m)
                else:
                    if self.can_castle_k_black():
                        ret.append(m)
            elif m.to_string() == 'O-O-O':
                if white_to_play:
                    if self.can_castle_q_white():
                        ret.append(m)
                else:
                    if self.can_castle_q_black():
                        ret.append(m)
            else:
                ret.append(m)
        return ret

    def get_possible_moves(self, from_white=None):
        white_to_play = self.white_to_play
        if from_white is not None:
            white_to_play = from_white
        naive_moves = self.get_naive_moves(white_to_play)
        print("len naive moves {}".format(len(naive_moves)))

        legal_moves = self.remove_would_check_moves(naive_moves, white_to_play)
        legal_moves = self.remove_illegal_castle(legal_moves, white_to_play)

        return legal_moves

    def process_move(self, move_str):
        all_moves = self.get_possible_moves()
        match_moves = [m for m in all_moves if m.to_string() == move_str]
        if len(match_moves) != 1:
            raise Exception("Move {} not found.".format(move_str))
        the_move = match_moves[0]

        ##if king move => disable castle
        if the_move.piece.symbol == 'k':
            if the_move.piece.is_white:
                self.white_can_castle_q = False
                self.white_can_castle_k = False
            else:
                self.black_can_castle_q = False
                self.black_can_castle_k = False
        ##if rook => disable castle
        if the_move.piece.symbol == 'r':
            if the_move.piece.is_white:
                if pos_to_string(the_move.from_pos) == 'a1':
                    self.white_can_castle_q = False
                if pos_to_string(the_move.from_pos) == 'h1':
                    self.white_can_castle_k = False
            else:
                if pos_to_string(the_move.from_pos) == 'a8':
                    self.white_can_castle_q = False
                if pos_to_string(the_move.from_pos) == 'h8':
                    self.white_can_castle_k = False

        del self.pieces[the_move.from_pos]
        self.pieces[the_move.to_pos] = the_move.piece

        if the_move.to_string() == 'O-O':
            if the_move.piece.is_white:
                del self.pieces[string_to_pos('h1')]
                self.pieces[string_to_pos('f1')] = Rook(is_white=True)
            else:
                del self.pieces[string_to_pos('h8')]
                self.pieces[string_to_pos('f8')] = Rook(is_white=False)

        if the_move.to_string() == 'O-O-O':
            print('doing a castle')
            if the_move.piece.is_white:
                print('for white')
                del self.pieces[string_to_pos('a1')]
                self.pieces[string_to_pos('d1')] = Rook(is_white=True)
            else:
                del self.pieces[string_to_pos('a8')]
                self.pieces[string_to_pos('d8')] = Rook(is_white=False)
        ##if move is a take en passant, remove captured piece
        if pos_to_string(the_move.to_pos) == self.en_passant and the_move.is_take:
            row_take = the_move.to_pos[0]
            col_take = the_move.to_pos[1]
            if row_take == 5:
                del self.pieces[(4, col_take)]
            else:
                del self.pieces[(3, col_take)]


        self.en_passant = the_move.get_en_passant()
        self.white_to_play = not self.white_to_play

    def get_king_position(self, white_king):
        tmp = [pos for (pos, piece) in self.pieces.items() if piece.symbol == 'k' and piece.is_white == white_king]
        if len(tmp) != 1:
            raise Exception('There is not one king')
        return pos_to_string(tmp[0])

    def is_check(self, against_white):
        king_position = self.get_king_position(against_white)
        op_moves = self.get_naive_moves(from_white=not against_white)
        op_takes = [m for m in op_moves if m.is_take]
        op_takes_king = [m for m in op_takes if pos_to_string(m.to_pos) == king_position]
        return len(op_takes_king) > 0

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

    def get_json(self):
        ret = {}
        ret['board'] = self.get_board()
        ret['moves'] = [m.to_json() for m in self.get_possible_moves()]
        return jsonify(ret)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    b = Board()
    b.init_default()
    for r in b.get_board():
        print(r)
    moves = b.get_possible_moves()
    print("# moves: {}".format(len(moves)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
