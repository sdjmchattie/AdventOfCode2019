def is_password_valid_1(int_password):
    str_digits = list(str(int_password))
    digits = list(map(lambda x: int(x), str_digits))

    adjacent_pair = any(map(
        lambda i: digits[i] == digits[i + 1],
        range(len(digits) - 1)
    ))

    digits_are_ascending = all(map(
        lambda i: digits[i] <= digits[i + 1],
        range(len(digits) - 1)
    ))

    return adjacent_pair and digits_are_ascending


def is_password_valid_2(int_password):
    str_digits = list(str(int_password))
    digits = list(map(lambda x: int(x), str_digits))

    first_pair_valid = digits[0] == digits[1] and digits[1] != digits[2]
    last_pair_valid = digits[len(digits) - 1] == digits[len(digits) - 2] and \
        digits[len(digits) - 2] != digits[len(digits) - 3]

    middle_pair_valid = any(map(
        lambda i: int(digits[i]) != int(digits[i + 1]) and
        int(digits[i + 1]) == int(digits[i + 2]) and
        int(digits[i + 2]) != int(digits[i + 3]),
        range(len(digits) - 3)
    ))

    return first_pair_valid or middle_pair_valid or last_pair_valid


min_password = 357253
max_password = 892942

valid_passwords_1 = list(filter(is_password_valid_1, range(min_password, max_password + 1)))

print('Part 1')
print('  Total valid passwords: {}'.format(len(valid_passwords_1)))

valid_passwords_2 = list(filter(is_password_valid_2, valid_passwords_1))

print()
print('Part 2')
print('  Total valid passwords: {}'.format(len(valid_passwords_2)))
