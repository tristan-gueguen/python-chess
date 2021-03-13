from board import main

def test_cant_move_if_check():
    b = main.Board()
    b.add_piece('k', 'd4', is_white=True)
    b.add_piece('p', 'c5', is_white=True)
    b.add_piece('b', 'b6', is_white=False)
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert 'c6' not in moves