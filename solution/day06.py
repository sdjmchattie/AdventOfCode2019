from functools import reduce
from typing import NewType


class OrbitalBody:
    def __init__(self, id) -> None:
        self.id = id
        self.parent = None

    def parental_orbits(self, accum=0):
        if self.parent is None:
            return accum
        else:
            return self.parent.parental_orbits(accum) + 1

    def ancestors(self, accum=[]):
        if self.parent is None:
            return accum
        else:
            return [self.parent.id] + self.parent.ancestors()


def get_or_create_body(bodies, id):
    try:
        return bodies[id]
    except KeyError:
        new_body = OrbitalBody(id)
        bodies[id] = new_body
        return new_body


def solve():
    f = open("input/day06.txt", "r")
    raw_orbits = f.read()
    f.close()

    bodies = {}
    for orbit_info in raw_orbits.split("\n"):
        try:
            parent_id, child_id = orbit_info.split(")")
        except ValueError:
            next

        parent = get_or_create_body(bodies, parent_id)
        child = get_or_create_body(bodies, child_id)
        child.parent = parent


    total_orbits = reduce(
        lambda accum, body: accum + body.parental_orbits(), bodies.values(), 0
    )

    print("Part 1")
    print(f"  Number of orbits: {total_orbits}")


    me_ancestors = bodies['YOU'].ancestors()
    santa_ancestors = bodies['SAN'].ancestors()
    common_ancestor = next(i for i in santa_ancestors if i in me_ancestors)

    print()
    print("Part 2")
    print(f"  Answer for part 2: {me_ancestors.index(common_ancestor) + santa_ancestors.index(common_ancestor)}")
