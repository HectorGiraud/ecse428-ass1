import pytest

from ass1.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_calculator_instantiates(calc):
    assert isinstance(calc, Calculator)

def test_calculator_has_push(calc):
    assert calc.push(0)

@pytest.mark.parametrize("arg", ["string", 1e333, True])
def test_calculator_push_is_safe(calc, arg):
    with pytest.raises(ValueError):
        calc.push(arg)

def test_calculator_has_working_pop(calc):
    numbers = [0, -1, 2.5]
    for n in numbers:
        calc.push(n)
    for n in reversed(numbers):
        assert calc.pop() == n


@pytest.mark.parametrize(
        "a, b, result",
        [
            (1, 2, -1),
            (1033, 334, 699),
            (1, 100, -99)
        ]
)
def test_calculator_does_substract(calc, a, b, result):
    calc.push(3)
    calc.push(a)
    calc.push(b)
    calc.sub()
    assert calc.pop() == result
    
def test_if_stack_underflow_while_substract_number_is_not_lost(calc):
    calc.push(3)
    try:
        calc.sub()
    except:
        pass
    assert calc.pop() == 3

@pytest.mark.parametrize(
        "a, b, result",
        [
            (1, 2, 0.5),
            (1033, 334, 3.092814371257485),
            (-1, 100, -0.01),
        ]
)
def test_calculator_does_divide(calc, a, b, result):
    calc.push(3)
    calc.push(a)
    calc.push(b)
    calc.div()
    assert calc.pop() == pytest.approx(result)