import re


def wire_locations(wire_path):
    cur_x = 0
    cur_y = 0
    locations = []

    for path_part in wire_path:
        regex_match = re.search(r'^([UDLR])(\d+)$', path_part)
        direction = regex_match.group(1)
        distance = int(regex_match.group(2))

        if direction == 'U':
            new_ys = range(cur_y + 1, cur_y + distance + 1)
            cur_y += distance
            for new_y in new_ys:
                locations.append([cur_x, new_y])
        elif direction == 'D':
            new_ys = range(cur_y - 1, cur_y - distance - 1, -1)
            cur_y -= distance
            for new_y in new_ys:
                locations.append([cur_x, new_y])
        if direction == 'R':
            new_xs = range(cur_x + 1, cur_x + distance + 1)
            cur_x += distance
            for new_x in new_xs:
                locations.append([new_x, cur_y])
        if direction == 'L':
            new_xs = range(cur_x - 1, cur_x - distance - 1, -1)
            cur_x -= distance
            for new_x in new_xs:
                locations.append([new_x, cur_y])

    return locations


def csv_location_distance_from_origin(csv_location):
    coordinates = csv_location.split(',')

    return abs(int(coordinates[0])) + abs(int(coordinates[1]))


def shortest_route_to_intersection(intersection, locations_1, locations_2):
    try:
        index_1 = locations_1.index(intersection)
        index_2 = locations_2.index(intersection)
    except ValueError:
        return None

    return index_1 + index_2 + 2


f = open('day_03/input.txt', 'r')
wire_paths = f.readlines()
f.close()

wire_1_path = wire_paths[0].split(',')
wire_2_path = wire_paths[1].split(',')

wire_1_locations = wire_locations(wire_1_path)
wire_2_locations = wire_locations(wire_2_path)

wire_1_strings = list(map(lambda x: "{},{}".format(x[0], x[1]), wire_1_locations))
wire_2_strings = list(map(lambda x: "{},{}".format(x[0], x[1]), wire_2_locations))

intersections = list(set(wire_1_strings) & set(wire_2_strings))
intersect_distances = map(csv_location_distance_from_origin, intersections)

print('Part 1')
print('  Intersection distance nearest [0, 0]: {}'.format(min(intersect_distances)))

combined_intersection_lengths = map(
    lambda x: shortest_route_to_intersection(x, wire_1_strings, wire_2_strings),
    intersections)

print()
print('Part 2')
print('  Shortest intersect combined lengths: {}'.format(min(combined_intersection_lengths)))
