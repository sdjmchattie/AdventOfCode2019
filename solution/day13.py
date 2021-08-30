import re

from lib.int_code import IntCode


class ArcadeGame:
  BLOCK_TYPES = {
    0: "", 1: "|", 2: "#", 3: "=", 4: "O"
  }

  def __init__(self, code):
    self.__game = IntCode(code)
    self.tiles = {}

  def run(self):
    while not self.__game.completed:
      self.__game.run(until_output = True)
      x = self.__game.output
      self.__game.run(until_output = True)
      y = self.__game.output
      self.__game.run(until_output = True)
      block = self.BLOCK_TYPES[self.__game.output]

      location = str([x, y])
      if block:
        self.tiles[location] = block
      else:
        try:
          del self.tiles[location]
        except KeyError:
          pass


def solve():
  f = open("input/day13.txt", "r")
  raw_code = f.read()
  f.close()

  orig_int_code = list(map((lambda x: int(x)), raw_code.split(',')))
  arcade = ArcadeGame(list(orig_int_code))
  arcade.run()

  print("Part 1")
  print(f'  Number of block tiles = {list(arcade.tiles.values()).count("#")}')

  print()
  print("Part 2")
  print(f'  Number of painted panels = ')
  print()
