from ass1.calculator import Calculator

class Decoder():
    def __init__(self) -> None:
        self.calc = Calculator()
        self.NUMBER_RESERVED = set("j-+.0123456789")

    def decode(self, string):
        tokens = string.split()
        current = 0
        if tokens[current] == "push":
            current += 1
            possible_number = ""
            while (not current >= len(tokens)) and (set(tokens[current]) <= self.NUMBER_RESERVED):
                if (possible_number != ""
                    and possible_number[-1] in ".0123456789"
                    and tokens[current][0] in ".0123456789" 
                ):
                    raise SyntaxError()

                possible_number+=tokens[current]
                current+=1

            jbuffer = False
            pythonic_possible_number = ""
            for i, char in enumerate(possible_number):
                if char == ".":
                    if i == 0 or possible_number[i-1] not in "0123456789" or i==len(possible_number)-1 or possible_number[i+1] not in "0123456789":
                        raise SyntaxError()
                if char=="j":

                    if i!=0 and i!=len(possible_number)-1 and possible_number[i-1] in "0123456789" and possible_number[i+1] in "0123456789":
                        raise SyntaxError()

                    if jbuffer:
                        raise SyntaxError()
                    jbuffer = True
                else:
                    if jbuffer:
                        if char not in ".1234567890":
                            pythonic_possible_number+="j"
                            jbuffer = False
                    pythonic_possible_number+=char
            if jbuffer:
                pythonic_possible_number+="j"

            self.calc.push(eval(pythonic_possible_number))

        elif tokens[current] == "pop":
            return self.calc.pop()