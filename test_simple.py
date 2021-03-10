import pytest
from board import main

# class TestInit(unittest.TestCase):

def test_add_piece():
    b = main.Board()
    b.add_piece('p', 'b2', False)
    should_be = ['........']
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('.p......')
    should_be.append('........')
    assert should_be == b.get_board()

def test_default():
    b = main.Board()
    b.init_default()
    should_be = ['rnbqkbnr']
    should_be.append('pppppppp')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('PPPPPPPP')
    should_be.append('RNBQKBNR')
    assert should_be == b.get_board()
#
def test_simple():
    b = main.Board()
    b.init_simple()
    should_be = ['........']
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('.P......')
    assert should_be == b.get_board()

def test_add_piece_already_here():
    with pytest.raises(Exception):
        b = main.Board()
        b.add_piece('p', 'a1', is_white=True)
        b.add_piece('p', 'a1', is_white=True)
#
# class TestPositions(unittest.TestCase):
def test_a1():
    assert main.pos_to_string((0,0)) == 'a1'

def test_a8():
    assert main.pos_to_string((7,0)) == 'a8'

def test_g5():
    assert main.pos_to_string((4,6)) == 'g5'

def test_reverse_a1():
    assert main.string_to_pos('a1') == (0,0)

def test_reverse_a8():
    assert main.string_to_pos('a8') == (7,0)

def test_reverse_g5():
    assert main.string_to_pos('g5') == (4,6)

def test_reverse_b1():
    assert main.string_to_pos('b1') == (0,1)

def test_lonely_centered_pawn_black():
    b = main.Board(white_to_play=False)
    b.add_piece('p', 'd4', False)
    moves = b.get_possible_moves()
    assert len(moves) == 1
    assert 'd3' in moves

def test_lonely_start_row_pawn_white():
    b = main.Board()
    b.add_piece('p', 'a2', True)
    moves = b.get_possible_moves()
    assert len(moves) == 2
    assert 'a3' in moves
    assert 'a4' in moves

def test_lonely_centered_pawn_white():
    b = main.Board()
    b.add_piece('p', 'd4', True)
    moves = b.get_possible_moves()
    assert len(moves) == 1
    assert 'd5' in moves

def test_lonely_no_move_pawn_white():
    b = main.Board()
    b.add_piece('p', 'd8', True)
    moves = b.get_possible_moves()
    assert len(moves) == 0

def test_lonely_no_move_pawn_black():
    b = main.Board(white_to_play=False)
    b.add_piece('p', 'd1', False)
    moves = b.get_possible_moves()
    assert len(moves) == 0

def test_lonely_centered_knight_white():
    b = main.Board()
    b.add_piece('n', 'd4', True)
    moves = b.get_possible_moves()
    assert len(moves) == 8
    assert 'Ne6' in moves
    assert 'Nf5' in moves
    assert 'Nc6' in moves
    assert 'Nb5' in moves
    assert 'Ne2' in moves
    assert 'Nf3' in moves
    assert 'Nc2' in moves
    assert 'Nb3' in moves

def test_lonely_bordered_knight_white():
    b = main.Board()
    b.add_piece('n', 'a1', True)
    moves = b.get_possible_moves()
    assert len(moves) == 2

def test_lonely_centered_bishop_white():
    b = main.Board()
    b.add_piece('b', 'd4', True)
    moves = b.get_possible_moves()
    assert len(moves) == 13
    assert 'Ba7' in moves
    assert 'Bg7' in moves
    assert 'Bh8' in moves
    assert 'Bg1' in moves

def test_lonely_centered_rook_white():
    b = main.Board()
    b.add_piece('r', 'd4', True)
    moves = b.get_possible_moves()
    assert len(moves) == 14
    assert 'Rd8' in moves
    assert 'Rd5' in moves
    assert 'Rd1' in moves
    assert 'Rh4' in moves

def test_lonely_centered_king_white():
    b = main.Board()
    b.add_piece('k', 'd4', True)
    moves = b.get_possible_moves()
    assert len(moves) == 8
    assert 'Kd5' in moves
    assert 'Kd3' in moves
    assert 'Ke5' in moves
    assert 'Ke3' in moves
    assert 'Kc5' in moves
    assert 'Kc3' in moves
    assert 'Kc4' in moves
    assert 'Ke4' in moves

def test_lonely_centered_queen_white():
    b = main.Board()
    b.add_piece('q', 'd4', True)
    moves = b.get_possible_moves()
    assert len(moves) == 27

def test_bishop_blocked_by_pawn():
    b = main.Board()
    b.add_piece('b', 'a1', True)
    b.add_piece('p', 'b2', True)
    moves = b.get_possible_moves()
    assert len(moves) == 2


def test_knight_blocked_by_pawn():
    b = main.Board()
    b.add_piece('n', 'a1', True)
    b.add_piece('p', 'c2', True)
    moves = b.get_possible_moves()
    assert len(moves) == 3
    assert 'c3' in moves
    assert 'c4' in moves
    assert 'Nb3' in moves

def test_rook_blocked_by_pawn():
    b = main.Board()
    b.add_piece('r', 'a1', True)
    b.add_piece('p', 'a2', True)
    b.add_piece('p', 'b1', True)
    moves = b.get_possible_moves()
    assert len(moves) == 3
    assert 'a3' in moves
    assert 'a4' in moves
    assert 'b2' in moves

def test_queen_blocked_by_pawn():
    b = main.Board()
    b.add_piece('q', 'a1', True)
    b.add_piece('p', 'a2', True)
    b.add_piece('p', 'b1', True)
    moves = b.get_possible_moves()
    assert len(moves) == 10
    assert 'a3' in moves
    assert 'a4' in moves
    assert 'b2' in moves

def test_king_blocked_by_pawn():
    b = main.Board()
    b.add_piece('k', 'a1', True)
    b.add_piece('p', 'a2', True)
    b.add_piece('p', 'b1', True)
    moves = b.get_possible_moves()
    assert len(moves) == 4
    assert 'a3' in moves
    assert 'a4' in moves
    assert 'b2' in moves

def test_pawn_blocked_by_pawn():
    b = main.Board()
    b.add_piece('p', 'd2', True)
    b.add_piece('p', 'd3', True)
    moves = b.get_possible_moves()
    assert len(moves) == 1
    assert 'd4' in moves

def test_number_moves_default():
    b = main.Board()
    b.init_default()
    moves = b.get_possible_moves()
    assert len(moves) == 20

def test_pawn_takes_pawn():
    b = main.Board()
    b.add_piece('p', 'd4', is_white=True)
    b.add_piece('p', 'e5', is_white=False)
    moves = b.get_possible_moves()
    assert len(moves) == 2
    assert 'd5' in moves
    assert 'dxe5' in moves

def test_pawn_takes_pawns():
    b = main.Board()
    b.add_piece('p', 'd4', is_white=True)
    b.add_piece('p', 'e5', is_white=False)
    b.add_piece('p', 'c5', is_white=False)
    moves = b.get_possible_moves()
    assert len(moves) == 3
    assert 'd5' in moves
    assert 'dxe5' in moves
    assert 'dxc5' in moves

def test_knight_takes_pawns():
    b = main.Board()
    b.add_piece('n', 'd4', is_white=True)
    b.add_piece('p', 'e6', is_white=False)
    b.add_piece('p', 'c2', is_white=False)
    moves = b.get_possible_moves()
    assert len(moves) == 8
    assert 'Nf5' in moves
    assert 'Nxe6' in moves
    assert 'Nxc2' in moves

def test_rook_takes_pawn():
    b = main.Board()
    b.add_piece('r', 'a1', is_white=True)
    b.add_piece('p', 'a8', is_white=False)
    moves = b.get_possible_moves()
    assert len(moves) == 14
    assert 'Ra4' in moves
    assert 'Rxa8' in moves

def test_bishop_takes_pawn():
    b = main.Board()
    b.add_piece('b', 'a1', is_white=True)
    b.add_piece('p', 'b2', is_white=False)
    moves = b.get_possible_moves()
    assert len(moves) == 1
    assert 'Bxb2' in moves

def test_king_takes_pawns():
    b = main.Board()
    b.add_piece('k', 'a1', is_white=True)
    b.add_piece('p', 'a2', is_white=False)
    b.add_piece('p', 'b1', is_white=False)
    b.add_piece('p', 'b2', is_white=False)
    moves = b.get_possible_moves()
    assert len(moves) == 3
    assert 'Kxa2' in moves
    assert 'Kxb1' in moves
    assert 'Kxb2' in moves

def test_queen_takes_pawns():
    b = main.Board()
    b.add_piece('Q', 'd4', is_white=True)
    b.add_piece('p', 'd5', is_white=False)
    b.add_piece('p', 'd3', is_white=False)
    b.add_piece('p', 'e3', is_white=False)
    b.add_piece('p', 'e4', is_white=False)
    b.add_piece('p', 'e5', is_white=False)
    b.add_piece('p', 'c3', is_white=False)
    b.add_piece('p', 'c4', is_white=False)
    b.add_piece('p', 'c5', is_white=False)
    moves = b.get_possible_moves()
    assert len(moves) == 8
