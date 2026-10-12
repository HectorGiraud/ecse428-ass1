import math

def is_valid_number(number):
    return (
        isinstance(number, (int, float, complex))
        and not isinstance(number, bool)
        and math.isfinite(number.real)
        and math.isfinite(number.imag)
    )