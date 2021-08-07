import math


def radial_angle(dx, dy):
  if dx == 0 and dy < 0:
    return 0.0

  try:
    ratio = dy / dx
  except ZeroDivisionError:
    ratio = math.inf

  radians = math.atan(ratio) + math.pi / 2
  radians += math.pi if dx < 0 else 0
  return radians


def solve():
  # f = open("input/day09.txt", "r")
  # raw_code = f.read().strip('\n')
  # f.close()

  map = [
    '......#.#.',
    '#..#.#....',
    '..#######.',
    '.#.#.###..',
    '.#..#.....',
    '..#....#.#',
    '#..#....#.',
    '.##.#..###',
    '##...#..#.',
    '.#....####',
  ]

  print("Part 1")

  print()
  print("Part 2")
