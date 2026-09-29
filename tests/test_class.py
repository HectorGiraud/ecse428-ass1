import pytest

from ass1.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_calculator_instantiates(calc):
    assert isinstance(calc, Calculator)

def test_calculator_has_push(calc):
    assert calc.push(0)