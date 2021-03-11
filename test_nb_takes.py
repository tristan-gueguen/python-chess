from board import main

def test_pawn_takes_pawn():
    b = main.Board()
    b.add_piece('p', 'd4', is_white=True)
    b.add_piece('p', 'e5', is_white=False)
    moves = b.get_possible_moves()
    takes = [m for m in moves if m.is_take]
    assert len(moves) == 2
    assert len(takes) == 1
    moves_san = [m.to_string() for m in moves]
    assert 'd5' in moves_san
    assert 'dxe5' in moves_san

def test_pawn_takes_pawns():
    b = main.Board()
    b.add_piece('p', 'd4', is_white=True)
    b.add_piece('p', 'e5', is_white=False)
    b.add_piece('p', 'c5', is_white=False)
    moves = b.get_possible_moves()
    moves_san = [m.to_string() for m in moves]
    takes = [m for m in moves if m.is_take]
    assert len(takes) == 2
    assert len(moves) == 3
    assert 'd5' in moves_san
    assert 'dxe5' in moves_san
    assert 'dxc5' in moves_san

def test_knight_takes_pawns():
    b = main.Board()
    b.add_piece('n', 'd4', is_white=True)
    b.add_piece('p', 'e6', is_white=False)
    b.add_piece('p', 'c2', is_white=False)
    moves = b.get_possible_moves()
    moves_san = [m.to_string() for m in moves]
    takes = [m for m in moves if m.is_take]
    assert len(moves) == 8
    assert len(takes) == 2
    assert 'Nf5' in moves_san
    assert 'Nxe6' in moves_san
    assert 'Nxc2' in moves_san

def test_rook_takes_pawn():
    b = main.Board()
    b.add_piece('r', 'a1', is_white=True)
    b.add_piece('p', 'a8', is_white=False)
    moves = b.get_possible_moves()
    moves_san = [m.to_string() for m in moves]
    takes = [m for m in moves if m.is_take]
    assert len(moves) == 14
    assert len(takes) == 1
    assert 'Ra4' in moves_san
    assert 'Rxa8' in moves_san

def test_bishop_takes_pawn():
    b = main.Board()
    b.add_piece('b', 'a1', is_white=True)
    b.add_piece('p', 'b2', is_white=False)
    moves = b.get_possible_moves()
    moves_san = [m.to_string() for m in moves]
    takes = [m for m in moves if m.is_take]
    assert len(moves) == 1
    assert len(takes) == 1
    assert 'Bxb2' in moves_san

def test_king_takes_pawns():
    b = main.Board()
    b.add_piece('k', 'a1', is_white=True)
    b.add_piece('p', 'a2', is_white=False)
    b.add_piece('p', 'b1', is_white=False)
    b.add_piece('p', 'b2', is_white=False)
    moves = b.get_possible_moves()
    moves_san = [m.to_string() for m in moves]
    takes = [m for m in moves if m.is_take]
    assert len(moves) == 3
    assert len(takes) == 3
    assert 'Kxa2' in moves_san
    assert 'Kxb1' in moves_san
    assert 'Kxb2' in moves_san

def test_queen_takes_pawns():
    b = main.Board()
    b.add_piece('q', 'd4', is_white=True)
    b.add_piece('p', 'd5', is_white=False)
    b.add_piece('p', 'd3', is_white=False)
    b.add_piece('p', 'e3', is_white=False)
    b.add_piece('p', 'e4', is_white=False)
    b.add_piece('p', 'e5', is_white=False)
    b.add_piece('p', 'c3', is_white=False)
    b.add_piece('p', 'c4', is_white=False)
    b.add_piece('p', 'c5', is_white=False)
    moves = b.get_possible_moves()
    # moves_san = [m.to_string() for m in moves]
    takes = [m for m in moves if m.is_take]
    assert len(moves) == 8
    assert len(takes) == 8