from lib.int_code import IntCode

f = open('input.txt', 'r')
cs_int_code = f.read()
f.close()

orig_int_code = list(map((lambda x: int(x)), cs_int_code.split(',')))
int_code_input = list(orig_int_code)
int_code = IntCode(int_code_input)
int_code.input = 1
int_code.run()

print('Part 1')
print('  After running, the output is: {}'.format(int_code.output))

print()
print('Part 2')
print('  Input noun is {} and verb is {}')