def run_int_code(code):
    pos = 0

    try:
        while code[pos] != 99:
            if code[pos] == 1:
                code[code[pos + 3]] = code[code[pos + 1]] + code[code[pos + 2]]
            elif code[pos] == 2:
                code[code[pos + 3]] = code[code[pos + 1]] * code[code[pos + 2]]
            else:
                raise ValueError('Operator code {} is not recognised.'.format(code[pos]))
            pos += 4
    except IndexError:
        return None

    return code


f = open('input.txt', 'r')
cs_int_code = f.read()
f.close()

orig_int_code = list(map((lambda x: int(x)), cs_int_code.split(',')))
int_code = list(orig_int_code)
int_code[1] = 12
int_code[2] = 2
run_code = run_int_code(int_code)

print('Part 1')
print('  After running, position 0 contains: {}'.format(run_code[0]))


def find_noun_verb(input_code, target_output):
    for noun_candidate in range(100):
        for verb_candidate in range(100):
            new_int_code = list(input_code)
            new_int_code[1] = noun_candidate
            new_int_code[2] = verb_candidate
            output_code = run_int_code(new_int_code)

            if output_code is not None and output_code[0] == target_output:
                return noun_candidate, verb_candidate


(noun, verb) = find_noun_verb(list(orig_int_code), 19690720)

print()
print('Part 2')
print('  Input noun is {} and verb is {}'.format(noun, verb))
