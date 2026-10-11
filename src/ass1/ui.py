from ass1.calculator import Calculator

class Decoder():
    def __init__(self) -> None:
        self.calc = Calculator()

    def decode(self, string):
        tokens = string.split()
        current_token = 0
        if tokens[current_token] == "push":
            real_number = 1
            current_token += 1
            while True:
                try: 
                    real_number = real_number*int(tokens[current_token])
                    break
                except:
                    if tokens[current_token] == "-":
                        real_number = -real_number
                current_token += 1
            self.calc.push(real_number)

        if tokens[current_token] == "pop":
            return self.calc.pop()