from board import main

def test_same_col_rooks():
    fen = "k7/6KR/8/8/8/6PR/8/8 w - - 0 1"
    b = main.Board()
    b.init_fen(fen)
    moves = [m.to_string() for m in b.get_possible_moves()]
    print(moves)
    assert 'Rh5' not in moves
    assert 'R7h5' in moves
    assert 'R3h5' in moves

def test_same_row_rooks():
    fen = "k7/8/8/8/8/3R3R/K7/8 w - - 0 1"
    b = main.Board()
    b.init_fen(fen)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert 'Re3' not in moves
    assert 'Rde3' in moves
    assert 'Rhe3' in moves
    assert 'Rd6' in moves

def test_same_target_knights():
    fen = "k4n2/8/8/2n5/8/8/K7/8 b - - 0 1"
    b = main.Board()
    b.init_fen(fen)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert 'Ne6' not in moves
    assert 'Nce6' in moves
    assert 'Nfe6' in moves

def test_same_target_knights_2():
    fen = "k7/8/3n4/8/3n4/8/K7/8 b - - 0 1"
    b = main.Board()
    b.init_fen(fen)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert 'Nf5' not in moves
    assert 'N4f5' in moves
    assert 'N6f5' in moves