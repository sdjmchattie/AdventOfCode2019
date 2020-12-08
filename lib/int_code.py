from enum import Enum


class ValueMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


def parse_op_code(code):
    code_string = str(code)
    op_code = int(code_string[-2:])
    code_string = code_string[:-2]

    value_modes = []
    while len(code_string) > 0:
        value_modes.append(ValueMode(int(code_string[-1:])))
        code_string = code_string[:-1]

    while len(value_modes) < 4:
        value_modes.append(ValueMode.POSITION)

    return op_code, value_modes


class IntCode:
    def __init__(self, code):
        self.initial_code = code
        self.code = None
        self.input = None
        self.output = None

    def run(self):
        pos = 0
        self.code = list(self.initial_code)
        self.output = None

        try:
            while self.code[pos] != 99:
                (op_code, value_modes) = parse_op_code(self.get_value(pos, ValueMode.IMMEDIATE))
                if op_code == 1:
                    self.add(pos + 1, value_modes)
                    pos += 4
                elif op_code == 2:
                    self.multiply(pos + 1, value_modes)
                    pos += 4
                elif op_code == 3:
                    self.set_value(pos + 1, self.input, value_modes[0])
                    pos += 2
                elif op_code == 4:
                    self.output = self.get_value(pos + 1, value_modes[0])
                    pos += 2
                else:
                    raise ValueError('Operator code {} is not recognised.'.format(op_code))
        except IndexError:
            pass

    def get_value(self, position, mode):
        if mode == ValueMode.POSITION:
            return self.code[self.code[position]]
        elif mode == ValueMode.IMMEDIATE:
            return self.code[position]
        else:
            raise ValueError('Value Mode {} is not recognised.'.format(mode))

    def set_value(self, position, new_value, mode):
        if mode == ValueMode.POSITION:
            self.code[self.code[position]] = new_value
        elif mode == ValueMode.IMMEDIATE:
            self.code[position] = new_value
        else:
            raise ValueError('Value Mode {} is not recognised.'.format(mode))

    def add(self, position, value_modes):
        op_result = self.get_value(position, value_modes[0]) + self.get_value(position + 1, value_modes[1])
        self.set_value(position + 2, op_result, value_modes[2])

    def multiply(self, position, value_modes):
        op_result = self.get_value(position, value_modes[0]) * self.get_value(position + 1, value_modes[1])
        self.set_value(position + 2, op_result, value_modes[2])
