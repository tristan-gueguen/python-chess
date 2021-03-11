
from board import main
def test_a1():
    assert main.pos_to_string((0,0)) == 'a1'

def test_a8():
    assert main.pos_to_string((7,0)) == 'a8'

def test_g5():
    assert main.pos_to_string((4,6)) == 'g5'

def test_reverse_a1():
    assert main.string_to_pos('a1') == (0,0)

def test_reverse_a8():
    assert main.string_to_pos('a8') == (7,0)

def test_reverse_g5():
    assert main.string_to_pos('g5') == (4,6)

def test_reverse_b1():
    assert main.string_to_pos('b1') == (0,1)
