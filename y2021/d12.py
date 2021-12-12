from collections import defaultdict


def parse_data(data):
    caves_map = defaultdict(set)
    for line in data:
        x, y = line.split("-")
        if x != 'end' and y != 'start':
            caves_map[x].add(y)
        if x != 'start' and y != 'end':
            caves_map[y].add(x)

    return caves_map


def traverse(caves_map, current, traversed=[]):
    traversed_small = set(cave for cave in traversed if cave.islower())
    caves_next = caves_map[current].difference(traversed_small)

    n_paths = 0
    for cave_next in caves_next:
        if cave_next != 'end':
            n_paths += traverse(caves_map, cave_next, traversed + [current])
        else:
            n_paths += 1

    return n_paths


def main():
    with open("y2021/input/d12.txt") as file:
        data = file.read().splitlines()

    caves_map = parse_data(data)
    n_paths = sum(traverse(caves_map, cave) for cave in caves_map['start'])

    print(f"Part 1: {n_paths}")


if __name__ == "__main__":
    main()
