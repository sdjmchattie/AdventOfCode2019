import re

from itertools import islice
from lib.int_code import IntCode


def partition(iterable, partition_size):
  dup_iter = iter(iterable)
  while part := list(islice(dup_iter, partition_size)):
    yield part


class ArcadeGame:
  BLOCK_TYPES = {
    0: "", 1: "|", 2: "#", 3: "=", 4: "O"
  }

  def __init__(self, code):
    self.__game = IntCode(code)
    self.score = 0
    self.__tiles = {}


  def run(self):
    while not self.__game.completed:
      self.__tiles = {}
      self.__game.run()
      for triplet in partition(self.__game.outputs, 3):
        x = triplet[0]
        y = triplet[1]
        code = triplet[2]

        location = (x, y)
        if location == (-1, 0):
          self.score = code
        else:
          self.__tiles[location] = self.BLOCK_TYPES[code]

      ball = self.locations_of_tile("O")[0]
      paddle = self.locations_of_tile("=")[0]

      if ball[0] < paddle[0]:
        self.__game.input = -1
      elif ball[0] > paddle[0]:
        self.__game.input = 1
      else:
        self.__game.input = 0

      if self.count_tiles("#") == 0:
        return


  def locations_of_tile(self, tile_char):
    return [k for k, v in self.__tiles.items() if v == tile_char]


  def count_tiles(self, tile_char):
    return list(self.__tiles.values()).count(tile_char)


def solve():
  f = open("input/day13.txt", "r")
  raw_code = f.read()
  f.close()

  orig_int_code = list(map((lambda x: int(x)), raw_code.split(',')))
  arcade = ArcadeGame(list(orig_int_code))
  arcade.run()

  print("Part 1")
  print(f'  Number of block tiles = {arcade.count_tiles("#")}')

  new_code = list(orig_int_code)
  new_code[0] = 2
  arcade = ArcadeGame(new_code)
  arcade.run()

  print()
  print("Part 2")
  print(f'  Score = {arcade.score}')
  print()
