import unittest

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
