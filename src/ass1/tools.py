import math

def is_valid_number(number):
    return isinstance(number, (int, float)) and not isinstance(number, bool) and math.isfinite(number)