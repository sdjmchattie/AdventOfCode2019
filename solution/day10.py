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

  best_visibility = 0
  best_location = None
  for asteroid in asteroids:
    angles = [radial_angle(a[0] - asteroid[0], a[1] - asteroid[1]) for a in asteroids if a != asteroid]
    score = len(set(angles))
    if best_visibility < score:
      best_visibility = score
      best_location = asteroid

  print("Part 1")
  print(f'  Best visibility is {best_visibility}')
  print(f'  Best location is {best_location}')

  # Get the angle of each asteroid from the best location
  asteroids_at_angle = {}
  for asteroid in asteroids:
    if asteroid == best_location:
      continue

    angle = radial_angle(asteroid[0] - best_location[0], asteroid[1] - best_location[1])
    inline_asteroids = asteroids_at_angle.get(angle, [])
    inline_asteroids.append(asteroid)
    asteroids_at_angle[angle] = inline_asteroids

  # Find the 200th angle and then the nearest asteroid at that angle
  angle_200 = sorted(list(asteroids_at_angle.keys()))[199]

  def distance(asteroid):
    math.sqrt(math.pow(asteroid[0] - best_location[0], 2) + math.pow(asteroid[1] - best_location[1], 2))

  closest_asteroid = min(asteroids_at_angle[angle_200], key = distance)

  print()
  print("Part 2")
  print(f'  200th asteroid to be vaporised is at {closest_asteroid}')
