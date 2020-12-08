from enum import Enum


class ValueMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class IntCode:
    def __init__(self, code):
        self.initial_code = code
        self.code = None

    def run(self):
        pos = 0
        self.code = list(self.initial_code)

        try:
            while self.code[pos] != 99:
                op_code = self.get_value(pos, ValueMode.IMMEDIATE)
                if op_code == 1:
                    self.add(pos)
                    pos += 4
                elif op_code == 2:
                    self.multiply(pos)
                    pos += 4
                else:
                    raise ValueError('Operator code {} is not recognised.'.format(op_code))
        except IndexError:
            pass

    def get_value(self, position, mode=ValueMode.POSITION):
        if mode == ValueMode.POSITION:
            return self.code[self.code[position]]
        elif mode == ValueMode.IMMEDIATE:
            return self.code[position]
        else:
            raise ValueError('Value Mode {} is not recognised.'.format(mode))

    def set_value(self, position, new_value, mode=ValueMode.POSITION):
        if mode == ValueMode.POSITION:
            self.code[self.code[position]] = new_value
        elif mode == ValueMode.IMMEDIATE:
            self.code[position] = new_value
        else:
            raise ValueError('Value Mode {} is not recognised.'.format(mode))

    def add(self, position):
        self.set_value(position + 3, self.get_value(position + 1) + self.get_value(position + 2))

    def multiply(self, position):
        self.set_value(position + 3, self.get_value(position + 1) * self.get_value(position + 2))
