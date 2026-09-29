from .tools import is_valid_number

class Calculator():
    def __init__(self) -> None:
        self.stack = []

    def push(self, number):
        if not is_valid_number(number):
            raise ValueError(f"Argument '{number}' is not a valid number.")
        self.stack.append(number)
        return True