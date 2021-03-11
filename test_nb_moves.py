from board import main

def test_nb_moves_1():
    fen = "r2k1b1r/p1p1pppp/1PP5/8/3P2n1/8/PP3PPP/RNB1K1NR b KQ - 0 10"
    b = main.Board()
    b.init_fen(fen)
    moves = b.get_possible_moves()
    print(moves)
    assert len(moves) == 23
