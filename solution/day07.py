from itertools import permutations
from lib.int_code import IntCode

def solve():
  f = open("input/day07.txt", "r")
  raw_code = f.read()
  f.close()

  orig_int_code = list(map((lambda x: int(x)), raw_code.split(',')))
  best_output = 0

  phase_codes = permutations(range(5))

  for phase_code_list in phase_codes:
    output_code = 0

    for phase_code in phase_code_list:
      int_code = IntCode(list(orig_int_code))
      int_code.input = phase_code
      int_code.run(steps = 1)
      int_code.input = output_code
      int_code.run()
      output_code = int_code.output

    best_output = max(best_output, output_code)

  print("Part 1")
  print(f"  Best thruster input: {best_output}")

  print()
  print("Part 2")
  print(f"  Answer:")
