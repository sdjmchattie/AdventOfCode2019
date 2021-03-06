from enum import Enum


class ValueMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


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
                (op_code, value_modes) = self.__parse_op_code(pos)
                if op_code == 1:
                    self.__add(pos + 1, value_modes)
                    pos += 4
                elif op_code == 2:
                    self.__multiply(pos + 1, value_modes)
                    pos += 4
                elif op_code == 3:
                    self.__set_value(pos + 1, self.input, value_modes[0])
                    pos += 2
                elif op_code == 4:
                    self.output = self.__get_value(pos + 1, value_modes[0])
                    pos += 2
                elif op_code == 5:
                    if self.__get_value(pos + 1, value_modes[0]) != 0:
                        pos = self.__get_value(pos + 2, value_modes[1])
                    else:
                        pos += 3
                elif op_code == 6:
                    if self.__get_value(pos + 1, value_modes[0]) == 0:
                        pos = self.__get_value(pos + 2, value_modes[1])
                    else:
                        pos += 3
                elif op_code == 7:
                    new_value = 0
                    if self.__get_value(pos + 1, value_modes[0]) < self.__get_value(pos + 2, value_modes[1]):
                        new_value = 1
                    self.__set_value(pos + 3, new_value, value_modes[2])
                    pos += 4
                elif op_code == 8:
                    new_value = 0
                    if self.__get_value(pos + 1, value_modes[0]) == self.__get_value(pos + 2, value_modes[1]):
                        new_value = 1
                    self.__set_value(pos + 3, new_value, value_modes[2])
                    pos += 4
                else:
                    raise ValueError('Operator code {} is not recognised.'.format(op_code))
        except IndexError:
            pass

    def __parse_op_code(self, position):
        code_string = str(self.__get_value(position, ValueMode.IMMEDIATE))
        op_code = int(code_string[-2:])
        code_string = code_string[:-2]

        value_modes = []
        while len(code_string) > 0:
            value_modes.append(ValueMode(int(code_string[-1:])))
            code_string = code_string[:-1]

        while len(value_modes) < 4:
            value_modes.append(ValueMode.POSITION)

        return op_code, value_modes

    def __get_value(self, position, mode):
        if mode == ValueMode.POSITION:
            return self.code[self.code[position]]
        elif mode == ValueMode.IMMEDIATE:
            return self.code[position]
        else:
            raise ValueError('Value Mode {} is not recognised.'.format(mode))

    def __set_value(self, position, new_value, mode):
        if mode == ValueMode.POSITION:
            self.code[self.code[position]] = new_value
        elif mode == ValueMode.IMMEDIATE:
            self.code[position] = new_value
        else:
            raise ValueError('Value Mode {} is not recognised.'.format(mode))

    def __add(self, position, value_modes):
        op_result = self.__get_value(position, value_modes[0]) + self.__get_value(position + 1, value_modes[1])
        self.__set_value(position + 2, op_result, value_modes[2])

    def __multiply(self, position, value_modes):
        op_result = self.__get_value(position, value_modes[0]) * self.__get_value(position + 1, value_modes[1])
        self.__set_value(position + 2, op_result, value_modes[2])
