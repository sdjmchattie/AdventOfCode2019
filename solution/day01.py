def fuel(mass):
    try:
        mass_int = int(mass)
        return max(int(mass_int / 3) - 2, 0)
    except ValueError:
        return 0


def fuel_recursive(mass):
    try:
        mass_int = int(mass)
        fuel_mass = fuel(mass_int)
        fuel_total = fuel_mass

        while fuel_mass > 0:
            fuel_mass = fuel(fuel_mass)
            fuel_total += fuel_mass

        return fuel_total
    except ValueError:
        return 0


def solve():
    f = open("input/day01.txt", "r")
    masses = f.readlines()
    f.close()

    print("Part 1")
    print(f"  Fuel for modules: {sum(map(fuel, masses))}")
    print()
    print("Part 2")
    print(f"  Fuel for modules: {sum(map(fuel_recursive, masses))}")
