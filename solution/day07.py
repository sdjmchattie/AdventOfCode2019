from itertools import permutations
from lib.int_code import IntCode


def make_amplifier(orig_code, phase_code):
  int_code = IntCode(orig_code)
  int_code.input = phase_code
  int_code.run(max_steps = 1)

  return int_code


def solve():
  f = open("input/day07.txt", "r")
  raw_code = f.read()
  f.close()

  orig_int_code = list(map((lambda x: int(x)), raw_code.split(',')))

  phase_codes = permutations(range(5))
  best_output = 0

  for phase_code_list in phase_codes:
    output_code = 0

    for phase_code in phase_code_list:
      amplifier = make_amplifier(list(orig_int_code), phase_code)
      amplifier.input = output_code
      amplifier.run()
      output_code = amplifier.output

    best_output = max(best_output, output_code)

  print("Part 1")
  print(f"  Best thruster input: {best_output}")

  def loop_amplifiers(amplifiers):
    output_code = 0

    while True:
      for amplifier in amplifiers:
        amplifier.input = output_code
        amplifier.run(until_output=True)
        output_code = amplifier.output

      if amplifiers[-1].completed:
        return amplifiers[-1].output

  phase_codes = permutations(range(5, 10))
  best_thruster_input = 0

  for phase_code_list in phase_codes:
    thruster_input = loop_amplifiers([make_amplifier(list(orig_int_code), pc) for pc in phase_code_list])
    best_thruster_input = max(best_thruster_input, thruster_input)

  print()
  print("Part 2")
  print(f"  Best thruster input: {best_thruster_input}")
