from .tools import is_valid_number

class Calculator():
    def __init__(self) -> None:
        self.stack = []

    def push(self, number):
        if not is_valid_number(number):
            raise ValueError(f"Argument '{number}' is not a valid number.")
        self.stack.append(number)
        return True

    def pop(self):
        return self.stack.pop()

    def sub(self):
        if len(self.stack) < 2:
            raise IndexError()
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a-b)

    def div(self):
        if len(self.stack) < 2:
            raise IndexError()
        b = self.stack.pop()
        if b==0:
            self.stack.append(b)
            raise ZeroDivisionError()
        a = self.stack.pop()
        self.stack.append(a/b)