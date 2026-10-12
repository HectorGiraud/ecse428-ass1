from ass1.calculator import Calculator

class Decoder():
    def __init__(self) -> None:
        self.calc = Calculator()
        self.NUMBER_RESERVED = set("j-+0123456789")

    def decode(self, string):
        tokens = string.split()
        current = 0
        if tokens[current] == "push":
            current += 1
            possible_number = ""
            while (not current >= len(tokens)) and (set(tokens[current]) <= self.NUMBER_RESERVED):
                possible_number+=tokens[current]
                current+=1

            jbuffer = False
            pythonic_possible_number = ""
            for char in possible_number:
                if char=="j":
                    if jbuffer:
                        raise SyntaxError()
                    jbuffer = True
                else:
                    if jbuffer:
                        if char not in "1234567890":
                            pythonic_possible_number+="j"
                            jbuffer = False
                    pythonic_possible_number+=char
            if jbuffer:
                pythonic_possible_number+="j"

            self.calc.push(eval(pythonic_possible_number))

        elif tokens[current] == "pop":
            return self.calc.pop()