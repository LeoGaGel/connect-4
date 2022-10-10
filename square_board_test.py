from square_board import *

def test_empty_test():
    board = SquareBoard()
    assert board.is_full() == False
    assert board.is_victory() == False

