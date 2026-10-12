from ass1.calculator import Calculator
import sys

class Decoder():
    def __init__(self) -> None:
        self.calc = Calculator()
        self.NUMBER_RESERVED = set("j-+.0123456789")

    def token_is_number(self, token):
        try:
            value = eval(token)
            return True, value
        except:
            return False, None

    def decode(self, string):
        tokens = string.split()

        #Firt pass to handle numbers
        current = 0
        while current < len(tokens):
            if set(tokens[current]) <= self.NUMBER_RESERVED:
                start_index = current
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

                
                tokens[start_index:current] = [pythonic_possible_number]
                current = start_index
            current+=1
        

        #Second pass for logic
        current = 0
        self.calc.backup()
        try:
            while current < len(tokens):
                token = tokens[current]
                if self.token_is_number(token)[0]: raise SyntaxError()
                elif token == "push":
                    current+=1
                    if current >= len(tokens): raise SyntaxError()
                    isNumber, value = self.token_is_number(tokens[current])
                    if not isNumber: raise SyntaxError()
                    self.calc.push(value)
                elif token == "pop":
                    if current!=len(tokens)-1: raise SyntaxError()
                    return self.calc.pop()
                elif token == "add":
                    self.calc.add()
                elif token == "sub":
                    self.calc.sub()
                elif token == "mul":
                    self.calc.mul()
                elif token == "div":
                    self.calc.div()
                else:
                    raise SyntaxError()
                current+=1
        except Exception:
            self.calc.restore()
            raise

def to_string(number):
    return f"{number.real} {"-" if number.imag<0 else "+"} j{abs(number.imag)}"

def run(stdin, stdout) -> int:
    decoder = Decoder()
    while True:
        stdout.write("$>")
        stdout.flush()
        line = stdin.readline()
        if line == "":            # EOF (Ctrl+D)
            stdout.write("\n")
            return 0
        line = line.strip()
        if not line:
            continue
        result = decoder.decode(line)
        if result:
            stdout.write(to_string(result) + "\n")

if __name__ == "__main__":
    sys.exit(run(sys.stdin, sys.stdout))