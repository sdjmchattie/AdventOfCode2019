import math


class Compound:
  def __init__(self, desc):
    qty, self.name = desc.split(" ")
    self.qty = int(qty)

  def __repr__(self):
    return f"{self.qty} x {self.name}"

  @staticmethod
  def find_with_name(name, compound_iter):
    return next((c for c in compound_iter if c.name == name), Compound(f"0 {name}"))


def parse_input():
  f = open("input/day14.txt", "r")
  raw_input = f.readlines()
  f.close()

  def parse_line(line):
    src_list, dest_desc = map(lambda x: x.strip(), line.split("=>"))
    src_compounds = tuple(map(lambda x: Compound(x.strip()), src_list.split(",")))
    return [Compound(dest_desc), src_compounds]

  return dict(map(parse_line, raw_input))


def solve():
  input = parse_input()
  dest_compounds = tuple(input.keys())

  have = {}
  need = { "FUEL": 1 }

  while(need_name := next((name for name in need.keys() if name != "ORE"), None)):
    need_qty = need[need_name]
    have_qty = have.get(need_name, 0)

    del need[need_name]

    if have_qty >= need_qty:
      have[need_name] = have_qty - need_qty
      continue

    need_qty -= have_qty

    reaction_key = next(c for c in input.keys() if c.name == need_name)
    reaction_multiplier = math.ceil(need_qty / reaction_key.qty)
    reaction_needs = list(input[reaction_key])

    have[need_name] = (reaction_key.qty * reaction_multiplier) - need_qty
    for reagent in reaction_needs:
      need[reagent.name] = need.get(reagent.name, 0) + (reagent.qty * reaction_multiplier)

  print("Part 1")
  print(f'  Needed Ore = {need["ORE"]}')

  print()
  print("Part 2")
  print(f'  Answer = {0}')
  print()
