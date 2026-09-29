import pytest

from ass1.file_template import add

def test_1():
    assert True

def test_2():
    assert False

def test_add():
    assert add(3,4) == 7

@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(2, 3, 5, id="positives"),
        pytest.param(-2, -3, -5, id="negatives"),
        pytest.param(-2, 3, 1, id="mixed-signs"),
        pytest.param(0, 0, 0, id="zeros"),
        pytest.param(7, 0, 7, id="add-zero"),
        pytest.param(10**18, 10**18, 2 * 10**18, id="big-ints"),
    ],
)
def test_add_integers(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(0.1, 0.2, 0.3, id="classic-float-error"),
        pytest.param(1.5, 2.25, 3.75, id="simple-floats"),
        pytest.param(1, 0.5, 1.5, id="int-plus-float"),
    ],
)
def test_add_floats(a, b, expected):
    assert add(a, b) == pytest.approx(expected)