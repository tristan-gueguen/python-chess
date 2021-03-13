from board import main

# def test_nb_moves_1():
#     fen = "r2k1b1r/p1p1pppp/1PP5/8/3P2n1/8/PP3PPP/RNB1K1NR b KQ - 0 10"
#     b = main.Board()
#     b.init_fen(fen)
#     moves = b.get_possible_moves()
#     print(moves)
#     assert len(moves) == 23


def test_lonely_centered_pawn_black():
    b = main.Board(white_to_play=False)
    b.add_piece('p', 'd4', False)
    moves = [m.to_string() for m in b.get_naive_moves(from_white=False)]
    assert len(moves) == 1
    assert 'd3' in moves

def test_lonely_start_row_pawn_white():
    b = main.Board()
    b.add_piece('p', 'a2', True)
    moves = [m.to_string() for m in b.get_naive_moves(from_white=True)]
    assert len(moves) == 2
    assert 'a3' in moves
    assert 'a4' in moves

def test_lonely_centered_pawn_white():
    b = main.Board()
    b.add_piece('p', 'd4', True)
    b.add_piece('k', 'a1', True)
    b.add_piece('k', 'a8', False)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 4
    assert 'd5' in moves

def test_lonely_no_move_pawn_white():
    b = main.Board()
    b.add_piece('p', 'd8', True)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 0

def test_lonely_no_move_pawn_black():
    b = main.Board(white_to_play=False)
    b.add_piece('p', 'd1', False)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 0

def test_lonely_centered_knight_white():
    b = main.Board()
    b.add_piece('n', 'd4', True)
    b.add_piece('k', 'a1', True)
    b.add_piece('k', 'a8', False)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 11
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
    b.add_piece('k', 'h1', True)
    b.add_piece('k', 'h8', False)
    moves = b.get_possible_moves()
    assert len(moves) == 5

def test_lonely_centered_bishop_white():
    b = main.Board()
    b.add_piece('b', 'd4', True)
    b.add_piece('k', 'h2', True)
    b.add_piece('k', 'h7', False)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 18
    assert 'Ba7' in moves
    assert 'Bg7' in moves
    assert 'Bh8' in moves
    assert 'Bg1' in moves

def test_lonely_centered_rook_white():
    b = main.Board()
    b.add_piece('r', 'd4', True)
    b.add_piece('k', 'a1', True)
    b.add_piece('k', 'a8', False)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 17
    assert 'Rd8' in moves
    assert 'Rd5' in moves
    assert 'Rd1' in moves
    assert 'Rh4' in moves

def test_lonely_centered_king_white():
    b = main.Board()
    b.add_piece('k', 'd4', True)
    moves = [m.to_string() for m in b.get_possible_moves()]
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
    b.add_piece('k', 'a2', True)
    b.add_piece('k', 'a7', False)
    moves = b.get_possible_moves()
    assert len(moves) == 32

def test_bishop_blocked_by_pawn():
    b = main.Board()
    b.add_piece('b', 'a1', True)
    b.add_piece('p', 'b2', True)
    b.add_piece('k', 'h1', True)
    b.add_piece('k', 'h8', False)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 5


def test_knight_blocked_by_pawn():
    b = main.Board()
    b.add_piece('n', 'a1', True)
    b.add_piece('p', 'c2', True)
    b.add_piece('k', 'h1', True)
    b.add_piece('k', 'h8', False)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 6
    assert 'c3' in moves
    assert 'c4' in moves
    assert 'Nb3' in moves

def test_rook_blocked_by_pawn():
    b = main.Board()
    b.add_piece('r', 'a1', True)
    b.add_piece('p', 'a2', True)
    b.add_piece('p', 'b1', True)
    b.add_piece('k', 'h2', True)
    b.add_piece('k', 'h7', False)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 8
    assert 'a3' in moves
    assert 'a4' in moves
    assert 'b2' in moves

def test_queen_blocked_by_pawn():
    b = main.Board()
    b.add_piece('q', 'a1', True)
    b.add_piece('p', 'a2', True)
    b.add_piece('p', 'b1', True)
    b.add_piece('k', 'h2', True)
    b.add_piece('k', 'h7', False)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 15
    assert 'a3' in moves
    assert 'a4' in moves
    assert 'b2' in moves

def test_king_blocked_by_pawn():
    b = main.Board()
    b.add_piece('k', 'a1', True)
    b.add_piece('p', 'a2', True)
    b.add_piece('p', 'b1', True)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 4
    assert 'a3' in moves
    assert 'a4' in moves
    assert 'b2' in moves

def test_pawn_blocked_by_pawn():
    b = main.Board()
    b.add_piece('p', 'd2', True)
    b.add_piece('p', 'd3', True)
    b.add_piece('k', 'a1', True)
    b.add_piece('k', 'a8', False)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 4
    assert 'd4' in moves

def test_number_moves_default():
    b = main.Board()
    b.init_default()
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert len(moves) == 20
