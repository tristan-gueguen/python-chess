import pytest
from board import main

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

