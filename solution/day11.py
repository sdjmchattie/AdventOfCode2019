from lib.int_code import IntCode


def solve():
  f = open("input/day11.txt", "r")
  raw_code = f.read()
  f.close()

  orig_int_code = list(map((lambda x: int(x)), raw_code.split(',')))

  print("Part 1")

  print()
  print("Part 2")
