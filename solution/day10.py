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
  f = open("input/day10.txt", "r")
  raw_map = f.readlines()
  f.close()

  asteroids = []
  for y, row in enumerate(raw_map):
    for x, marker in enumerate(row):
      if marker == '#':
        asteroids.append([x, y])

  best = 0
  for asteroid in asteroids:
    angles = [radial_angle(a[0] - asteroid[0], a[1] - asteroid[1]) for a in asteroids if a != asteroid]
    score = len(set(angles))
    best = max(best, score)

  print("Part 1")
  print(f'  Best visibility is {best}')

  print()
  print("Part 2")
