class IntCode:
    def __init__(self, code):
        self.initial_code = code
        self.result_code = None

    def run(self):
        pos = 0
        code = list(self.initial_code)

        try:
            while code[pos] != 99:
                if code[pos] == 1:
                    code[code[pos + 3]] = code[code[pos + 1]] + code[code[pos + 2]]
                    pos += 4
                elif code[pos] == 2:
                    code[code[pos + 3]] = code[code[pos + 1]] * code[code[pos + 2]]
                    pos += 4
                else:
                    raise ValueError('Operator code {} is not recognised.'.format(code[pos]))
        except IndexError:
            pass

        self.result_code = code
