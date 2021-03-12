from board import main

def test_simple_move():
    b = main.Board()
    b.add_piece('p', 'd2', is_white=True)
    b.add_piece('p', 'c3', is_white=False)
    b.process_move('dxc3')

    should_be = ['........']
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('........')
    should_be.append('..P.....')
    should_be.append('........')
    should_be.append('........')
    assert should_be == b.get_board()

def test_multiple_takes_bishop():
    b = main.Board()
    b.add_piece('b', 'a1', is_white=True)
    b.add_piece('p', 'b2', is_white=False)
    b.add_piece('p', 'c4', is_white=False)
    b.process_move('Bxb2')
    b.process_move('c3')
    b.process_move('Bxc3')