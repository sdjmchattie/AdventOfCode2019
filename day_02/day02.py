from common.int_code import IntCode

f = open('input.txt', 'r')
cs_int_code = f.read()
f.close()

orig_int_code = list(map((lambda x: int(x)), cs_int_code.split(',')))
int_code_input = list(orig_int_code)
int_code_input[1] = 12
int_code_input[2] = 2
int_code = IntCode(int_code_input)
int_code.run()

print('Part 1')
print('  After running, position 0 contains: {}'.format(int_code.result_code[0]))


def find_noun_verb(input_code, target_output):
    for noun_candidate in range(100):
        for verb_candidate in range(100):
            new_int_code = list(input_code)
            new_int_code[1] = noun_candidate
            new_int_code[2] = verb_candidate
            int_code_machine = IntCode(new_int_code)
            int_code_machine.run()

            if int_code_machine.result_code is not None and \
                    int_code_machine.result_code[0] == target_output:
                return noun_candidate, verb_candidate


(noun, verb) = find_noun_verb(list(orig_int_code), 19690720)

print()
print('Part 2')
print('  Input noun is {} and verb is {}'.format(noun, verb))
