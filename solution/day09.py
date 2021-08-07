from lib.int_code import IntCode


def solve():
  f = open("input/day09.txt", "r")
  raw_code = f.read().strip('\n')
  f.close()

  orig_int_code = list(map((lambda x: int(x)), raw_code.split(',')))
  int_code = IntCode(list(orig_int_code))
  int_code.input = 1
  int_code.run()

  print("Part 1")
  print(f"  Outputs after run: {int_code.outputs}")

  int_code.reset()
  int_code.input = 2
  int_code.run()

  print()
  print("Part 2")
  print(f"  Outputs after run: {int_code.outputs}")
