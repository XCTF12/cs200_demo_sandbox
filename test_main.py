import main
import pytest

@pytest.mark.parameterize(
        ('input_x', 'input_y', 'expected'),
        (0, 0, 1),
        (1, 0, 1),
        (1, 1, 2),
        (2, 3, 5),
        (1, 7, 8)

)
def test_main():
    assert main.sum(3,6) == 9, 'noooooo'

def test_main2(input_x, input_y, expected):
    assert main.sum(input_x, input_y) == expected

test_main2()