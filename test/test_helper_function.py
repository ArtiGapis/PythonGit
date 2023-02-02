from src.helper_functions import add, multiply
import sys
sys.path.append('../')

def test_add_two_possitive_numbers_produce_positive_number():
    # give
    i, j = 1, 2
    # when
    rest = add(i, j)
    # then
    assert  rest ==3
def test_add_two_negatyve_number():
    # give
    i, j = -1, -2
    # when
    rest = add(i, j)
    # then
    assert rest == -3

def test_add_possitive_add_zero():
    # give
    i, j = 1, 2
    # when
    rest = add(i, j)
    # then
    assert rest == 3

if __name__ == '__main__':
    test_add_two_negatyve_number()
    test_add_possitive_add_zero()
    test_add_possitive_add_zero()