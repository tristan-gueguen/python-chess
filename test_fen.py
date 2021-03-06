import pytest
from board import main

def test_start_position():
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    b = main.Board()
    b.init_fen(fen)

    should_be = ['rnbqkbnr']
    should_be.append('pppppppp')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('PPPPPPPP')
    should_be.append('RNBQKBNR')
    assert should_be == b.get_board()
    assert b.white_to_play == True

def test_reverse_start_position():
    b = main.Board()
    b.init_default()
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    assert b.to_fen() == fen

def test_reverse_few_moves():
    b = main.Board()
    b.init_default()
    b.process_move('d4')
    b.process_move('e5')
    b.process_move('dxe5')
    b.process_move('Nf6')
    b.process_move('f3')
    b.process_move('Bb4')
    b.process_move('Qd2')
    b.process_move('O-O')
    fen = "rnbq1rk1/pppp1ppp/5n2/4P3/1b6/5P2/PPPQP1PP/RNB1KBNR w KQ - 0 1"
    assert b.to_fen() == fen


def test_few_moves():
    fen = "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"
    b = main.Board()
    b.init_fen(fen)

    should_be = ['rnbqkbnr']
    should_be.append('pp.ppppp')
    should_be.append('........')
    should_be.append('..p.....')
    should_be.append('....P...')
    should_be.append('.....N..')
    should_be.append('PPPP.PPP')
    should_be.append('RNBQKB.R')
    assert should_be == b.get_board()
    assert b.white_to_play == False

def test_random():
    fen = "r2k1b1r/p1p1pppp/1PP5/8/3P2n1/8/PP3PPP/RNB1K1NR b KQ - 0 10"
    b = main.Board()
    b.init_fen(fen)

    should_be = ['r..k.b.r']
    should_be.append('p.p.pppp')
    should_be.append('.PP.....')
    should_be.append('........')
    should_be.append('...P..n.')
    should_be.append('........')
    should_be.append('PP...PPP')
    should_be.append('RNB.K.NR')
    assert should_be == b.get_board()
    assert b.white_to_play == False

def test_castle_1():
    fen = "r2k1b1r/p1p1pppp/1PP5/8/3P2n1/8/PP3PPP/RNB1K1NR b KQ - 0 10"
    b = main.Board()
    b.init_fen(fen)
    assert not b.black_can_castle_q
    assert not b.black_can_castle_k
    assert b.white_can_castle_k
    assert b.white_can_castle_q
