from board import main

def test_en_passant_move_after():
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    b = main.Board()
    b.init_fen(fen)
    assert b.en_passant == '-'
    b.process_move('d4')
    assert b.en_passant == 'd3'
    b.process_move('d5')
    assert b.en_passant == 'd6'
    b.process_move('a3')
    assert b.en_passant == '-'

def test_en_passant_take():
    fen = 'rnbqkbnr/ppp3pp/4p3/3pPp2/3P4/8/PPP2PPP/RNBQKBNR w KQkq f6 0 4'
    b = main.Board()
    b.init_fen(fen)
    assert b.en_passant == 'f6'
    moves = [m.to_string() for m in b.get_possible_moves()]
    assert 'exf6' in moves
    b.process_move('exf6')

    should_be = ['rnbqkbnr']
    should_be.append('ppp...pp')
    should_be.append('....pP..')
    should_be.append('...p....')
    should_be.append('...P....')
    should_be.append('........')
    should_be.append('PPP..PPP')
    should_be.append('RNBQKBNR')
    assert should_be == b.get_board()

