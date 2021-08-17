from functools import reduce

class Moon:
  def __init__(self, start_pos) -> None:
    self.pos = list(start_pos)
    self.velocity = [0] * len(start_pos)
    self.initial_state = self.state()

  def calc_delta_v(self, other_moons_pos):
    delta_v = [0] * len(self.velocity)
    for i in range(len(delta_v)):
      for other_moon in other_moons_pos:
        if other_moon[i] > self.pos[i]:
          delta_v[i] += 1
        elif other_moon[i] < self.pos[i]:
          delta_v[i] -= 1

    return (delta_v)

  def update(self, other_moons_pos):
    delta_v = self.calc_delta_v(other_moons_pos)
    self.velocity = [self.velocity[i] + delta_v[i] for i in range(len(delta_v))]
    self.pos = [self.pos[i] + self.velocity[i] for i in range(len(delta_v))]

  def energy(self):
    pot = reduce(lambda t, p: t + abs(p), self.pos, 0)
    kin = reduce(lambda t, v: t + abs(v), self.velocity, 0)

    return(pot * kin)

  def state(self):
    return(f"{str(self.pos)},{str(self.velocity)}")


MOONS_POS_START = [
  [14, 9, 14],
  [9, 11, 6],
  [-6, 14, -4],
  [4, -4, -3],
]

def solve():
  moons = [Moon(start_pos) for start_pos in MOONS_POS_START]

  for _ in range(1000):
    all_pos = list(map(lambda m: list(m.pos), moons))
    for i in range(len(moons)):
      other_pos = list(all_pos)
      del(other_pos[i])
      moons[i].update(other_pos)

  print("Part 1")
  print(f'  Energy after 1000 iterations = {reduce(lambda t, m: t + m.energy(), moons, 0)}')
  print()
  print("Part 2")
  print("  Crunching! ...")

  def shortest_cycle(i):
    moons = [Moon([start_pos[i]]) for start_pos in MOONS_POS_START]

    current_iter = 0
    while current_iter == 0 or not all([moon.state() == moon.initial_state for moon in moons]):
      current_iter += 1

      all_pos = list(map(lambda m: list(m.pos), moons))
      for i in range(len(moons)):
        other_pos = list(all_pos)
        del(other_pos[i])
        moons[i].update(other_pos)

    return current_iter

  def find_lcm(x, y):
    largest = max(x, y)
    smallest = min(x, y)
    answer = largest
    while True:
      if answer % smallest == 0:
        return answer

      answer += largest

  shortest_cycles = [shortest_cycle(i) for i in range(len(MOONS_POS_START[0]))]
  print(f'  Iterations to reach initial state (per dimension) = {shortest_cycles}')

  lcm = reduce(find_lcm, shortest_cycles)
  print(f'  Iterations needed for all dimensions to return to initial state = {lcm}')
