import pytest
from board import main

def test_invalid_move():
    b = main.Board()
    b.add_piece('p', 'd2', is_white=True)
    with pytest.raises(Exception):
        b.process_move('h8')

def test_simple_move():
    b = main.Board()
    b.add_piece('p', 'd2', is_white=True)
    b.process_move('d3')

    should_be = ['........']
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('...P....')
    should_be.append('........')
    should_be.append('........')
    assert should_be == b.get_board()


def test_move_lonely_bishop():
    b = main.Board()
    b.add_piece('b', 'd2', is_white=True)
    b.process_move('Bb4')

    should_be = ['........']
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('.B......')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    assert should_be == b.get_board()


def test_move_lonely_rook():
    b = main.Board()
    b.add_piece('r', 'a1', is_white=True)
    b.process_move('Ra8')
    b.process_move('Rh8')

    should_be = ['.......R']
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    assert should_be == b.get_board()


def test_move_lonely_rook():
    b = main.Board()
    b.add_piece('r', 'a1', is_white=True)
    b.add_piece('p', 'd5', is_white=False)
    b.process_move('Ra8')
    b.process_move('d4')
    b.process_move('Rh8')

    should_be = ['.......R']
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('...p....')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    assert should_be == b.get_board()