from board import main
import pytest

def test_find_king_correct():
    b = main.Board()
    b.add_piece('k', 'e4', is_white=True)
    pos = b.get_king_position(white_king=True)
    assert pos == 'e4'

def test_find_king_several():
    b = main.Board()
    b.add_piece('k', 'e4', is_white=True)
    b.add_piece('k', 'e5', is_white=True)
    with pytest.raises(Exception):
        pos = b.get_king_position(white_king=True)
        assert pos == 'e4'

def test_find_king_no_king():
    b = main.Board()
    with pytest.raises(Exception):
        pos = b.get_king_position(white_king=True)
        assert pos == 'e4'

def test_recognize_check():
    b = main.Board()
    b.add_piece('k', 'd4', is_white=True)
    b.add_piece('p', 'e5', is_white=False)
    assert b.is_check(against_white=True)

def test_no_check():
    b = main.Board()
    b.add_piece('k', 'd4', is_white=True)
    b.add_piece('p', 'a1', is_white=False)
    assert not b.is_check(against_white=True)


def test_recognize_check_bishop_from_distance():
    b = main.Board()
    b.add_piece('k', 'h8', is_white=True)
    b.add_piece('b', 'a1', is_white=False)
    assert b.is_check(against_white=True)

def test_if_check_have_to_move():
    b = main.Board(white_to_play=False)
    b.add_piece('k', 'e8', is_white=False)
    b.add_piece('p', 'a7', is_white=False)
    b.add_piece('q', 'e1', is_white=True)
    b.add_piece('k', 'h1', is_white=True)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 4
