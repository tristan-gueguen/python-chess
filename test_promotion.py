from board import main

def test_can_promote():
    fen = "rnbq3r/ppppkP1p/7n/6p1/4P3/8/PPPB1PPP/RN2KBNR w KQ - 1 8"
    b = main.Board()
    b.init_fen(fen)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert "f8=Q" in moves
    assert "f8=B" in moves
    assert "f8=N" in moves
    assert "f8=R" in moves

def test_black_can_promote():
    fen = "rnbqkbnr/ppp1pppp/B7/8/3P1P2/8/PPPKp1PP/RNBQ2NR b kq - 1 5"
    b = main.Board()
    b.init_fen(fen)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert "e1=Q" in moves
    assert "e1=B" in moves
    assert "e1=N" in moves
    assert "e1=R" in moves

def test_black_can_promote_by_taking():
    fen = "rnbqkbnr/ppp1pppp/B7/8/3P1P2/8/PPPKp1PP/RNBQ2NR b kq - 1 5"
    b = main.Board()
    b.init_fen(fen)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert "exd1=Q" in moves
    assert "exd1=B" in moves
    assert "exd1=N" in moves
    assert "exd1=R" in moves

def test_black_promote_ok_board():
    fen = "rnbqkbnr/ppp1pppp/B7/8/3P1P2/8/PPPKp1PP/RNBQ2NR b kq - 1 5"
    b = main.Board()
    b.init_fen(fen)
    b.process_move('exd1=Q')

    should_be = ['rnbqkbnr']
    should_be.append('ppp.pppp')
    should_be.append('B.......')
    should_be.append('........')
    should_be.append('...P.P..')
    should_be.append('........')
    should_be.append('PPPK..PP')
    should_be.append('RNBq..NR')

    assert should_be == b.get_board()

