from enum import Enum


class ValueMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class IntCode:
    def __init__(self, code):
        self.initial_code = code
        self.reset()

    @property
    def output(self):
        return self.outputs[-1]

    @property
    def completed(self):
        return self.code[self.pos] == 99

    def reset(self):
        self.pos = 0
        self.code = { index: value for index, value in enumerate(self.initial_code) }
        self.input = 0
        self.outputs = []
        self.relative_base = 0

    def run(self, until_input=False, until_output=False):
        try:
            while not self.completed:
                (op_code, value_modes) = self.__parse_op_code(self.pos)

                if op_code == 1:
                    self.__add(self.pos + 1, value_modes)
                    self.pos += 4
                elif op_code == 2:
                    self.__multiply(self.pos + 1, value_modes)
                    self.pos += 4
                elif op_code == 3:
                    self.__set_value(self.pos + 1, self.input, value_modes[0])
                    self.pos += 2
                    if until_input:
                        return
                elif op_code == 4:
                    self.outputs.append(self.__get_value(self.pos + 1, value_modes[0]))
                    self.pos += 2
                    if until_output:
                        return
                elif op_code == 5:
                    if self.__get_value(self.pos + 1, value_modes[0]) != 0:
                        self.pos = self.__get_value(self.pos + 2, value_modes[1])
                    else:
                        self.pos += 3
                elif op_code == 6:
                    if self.__get_value(self.pos + 1, value_modes[0]) == 0:
                        self.pos = self.__get_value(self.pos + 2, value_modes[1])
                    else:
                        self.pos += 3
                elif op_code == 7:
                    new_value = 0
                    if self.__get_value(self.pos + 1, value_modes[0]) < self.__get_value(self.pos + 2, value_modes[1]):
                        new_value = 1
                    self.__set_value(self.pos + 3, new_value, value_modes[2])
                    self.pos += 4
                elif op_code == 8:
                    new_value = 0
                    if self.__get_value(self.pos + 1, value_modes[0]) == self.__get_value(self.pos + 2, value_modes[1]):
                        new_value = 1
                    self.__set_value(self.pos + 3, new_value, value_modes[2])
                    self.pos += 4
                elif op_code == 9:
                    self.relative_base += self.__get_value(self.pos + 1, value_modes[0])
                    self.pos += 2
                else:
                    raise ValueError(f'Operator code {op_code} is not recognised.')

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
        try:
            if mode == ValueMode.POSITION:
                mem_address = self.__get_value(position, ValueMode.IMMEDIATE)
                return self.code[mem_address]
            elif mode == ValueMode.IMMEDIATE:
                return self.code[position]
            elif mode == ValueMode.RELATIVE:
                mem_address = self.__get_value(position, ValueMode.IMMEDIATE)
                return self.code[mem_address + self.relative_base]
            else:
                raise ValueError(f'Value Mode {mode} is not recognised.')
        except KeyError:
            return 0

    def __set_value(self, position, new_value, mode):
        if mode == ValueMode.POSITION:
            mem_address = self.__get_value(position, ValueMode.IMMEDIATE)
            self.code[mem_address] = new_value
        elif mode == ValueMode.IMMEDIATE:
            self.code[position] = new_value
        elif mode == ValueMode.RELATIVE:
            mem_address = self.__get_value(position, ValueMode.IMMEDIATE)
            self.code[mem_address + self.relative_base] = new_value
        else:
            raise ValueError(f'Value Mode {mode} is not recognised.')

    def __add(self, position, value_modes):
        op_result = self.__get_value(position, value_modes[0]) + self.__get_value(position + 1, value_modes[1])
        self.__set_value(position + 2, op_result, value_modes[2])

    def __multiply(self, position, value_modes):
        op_result = self.__get_value(position, value_modes[0]) * self.__get_value(position + 1, value_modes[1])
        self.__set_value(position + 2, op_result, value_modes[2])
