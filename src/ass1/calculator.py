class Calculator():
    def __init__(self) -> None:
        self.stack = []

    def push(self, number):
        self.stack.append(number)
        return True