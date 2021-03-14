from board import main
import pytest

def test_can_castle_init():
    b = main.Board()
    b.init_default()
    assert b.black_can_castle_k
    assert b.black_can_castle_q
    assert b.white_can_castle_k
    assert b.white_can_castle_q

def test_cant_castle_king_moved():
    b = main.Board()
    b.init_default()
    b.process_move('e4')
    b.process_move('e5')
    b.process_move('Ke2')
    assert b.black_can_castle_k
    assert b.black_can_castle_q
    assert not b.white_can_castle_k
    assert not b.white_can_castle_q

def test_cant_castle_rook_moved():
    b = main.Board()
    b.init_default()
    b.process_move('h4')
    b.process_move('h5')
    b.process_move('Rh2')
    assert not b.white_can_castle_k
    b.process_move('e6')
    b.process_move('a4')
    b.process_move('e5')
    b.process_move('Ra2')
    assert not b.white_can_castle_q

def test_cant_castle_cause_check():
    b = main.Board()
    b.add_piece('k', 'e8', is_white=False)
    b.add_piece('k', 'e1', is_white=True)
    b.add_piece('r', 'h1', is_white=True)
    b.add_piece('q', 'e4', is_white=False)
    assert not b.can_castle_k_white()

def test_cant_castle_cause_check_2():
    b = main.Board()
    b.add_piece('k', 'e8', is_white=False)
    b.add_piece('k', 'e1', is_white=True)
    b.add_piece('r', 'h1', is_white=True)
    b.add_piece('q', 'f4', is_white=False)
    assert not b.can_castle_k_white()

def test_cant_castle_cause_check_3():
    b = main.Board()
    b.add_piece('k', 'e8', is_white=False)
    b.add_piece('k', 'e1', is_white=True)
    b.add_piece('r', 'h1', is_white=True)
    b.add_piece('q', 'g4', is_white=False)
    assert not b.can_castle_k_white()

def test_cant_castle_q_cause_check():
    b = main.Board()
    b.add_piece('k', 'e8', is_white=False)
    b.add_piece('k', 'e1', is_white=True)
    b.add_piece('r', 'a1', is_white=True)
    b.add_piece('q', 'e4', is_white=False)
    assert not b.can_castle_q_white()

def test_cant_castle_q_cause_check_2():
    b = main.Board()
    b.add_piece('k', 'e8', is_white=False)
    b.add_piece('k', 'e1', is_white=True)
    b.add_piece('r', 'a1', is_white=True)
    b.add_piece('q', 'd4', is_white=False)
    assert not b.can_castle_q_white()

def test_cant_castle_q_cause_check_3():
    b = main.Board()
    b.add_piece('k', 'e8', is_white=False)
    b.add_piece('k', 'e1', is_white=True)
    b.add_piece('r', 'a1', is_white=True)
    b.add_piece('q', 'c4', is_white=False)
    assert not b.can_castle_q_white()
