import re

from enum import IntEnum
from lib.int_code import IntCode


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Robot:
  def __init__(self, code, initial_panels={}) -> None:
    self.__robot = IntCode(code)
    self.panels = initial_panels

  def run(self):
    direction = Direction.UP
    location = [0, 0]

    while not self.__robot.completed:
      self.__robot.input = self.panels.get(str(location), 0)
      self.__robot.run(until_output = True)
      self.panels[str(location)] = self.__robot.output
      self.__robot.run(until_output = True)
      direction = direction + (-1 if self.__robot.output == 0 else 1)

      while direction < 0:
        direction += 4
      while direction > 3:
        direction -= 4

      if direction == Direction.UP:
        location[1] -= 1
      elif direction == Direction.DOWN:
        location[1] += 1
      elif direction == Direction.LEFT:
        location[0] -= 1
      elif direction == Direction.RIGHT:
        location[0] += 1


def solve():
  f = open("input/day11.txt", "r")
  raw_code = f.read()
  f.close()

  orig_int_code = list(map((lambda x: int(x)), raw_code.split(',')))
  robot = Robot(list(orig_int_code))
  robot.run()

  print("Part 1")
  print(f'  Number of painted panels = {len(robot.panels.keys())}')

  robot = Robot(list(orig_int_code), { '[0, 0]': 1 })
  robot.run()

  print()
  print("Part 2")
  print(f'  Number of painted panels = {len(robot.panels.keys())}')
  print()

  def coords_from_string(s):
    matches = re.match(r'\[(\d+), (\d+)\]', s)
    return [int(matches.group(1)), int(matches.group(2))]

  coords = list(map(coords_from_string, robot.panels.keys()))
  x_max = max(map(lambda c: c[0], coords))
  y_max = max(map(lambda c: c[1], coords))

  for y in range(y_max + 1):
    for x in range(x_max + 1):
      pixel = robot.panels.get(str([x, y]), 0)

      if pixel == 0:
        pixel_char = '⬛️'
      else:
        pixel_char = '⬜️'

      print(pixel_char, end='')

    print()
  print()
