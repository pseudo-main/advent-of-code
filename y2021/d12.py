from collections import defaultdict


def parse_data(data):
    caves_map = defaultdict(list)
    for line in data:
        x, y = line.split("-")
        if x != 'end' and y != 'start':
            caves_map[x].append(y)
        if x != 'start' and y != 'end':
            caves_map[y].append(x)

    return caves_map


def traverse(caves_map, cave='start', path=[], small_twice=False):
    caves_next = caves_map[cave]

    n_paths = 0
    for cave_next in caves_next:
        if cave_next.islower() and cave_next in path:
            if small_twice:
                n_paths += traverse(caves_map, cave_next, path+[cave])
        elif cave_next != 'end':
            n_paths += traverse(caves_map, cave_next, path+[cave], small_twice)
        else:
            n_paths += 1

    return n_paths


def main():
    with open("y2021/input/d12.txt") as file:
        data = file.read().splitlines()

    caves_map = parse_data(data)

    n_paths = traverse(caves_map)
    n_paths_special = traverse(caves_map, small_twice=True)

    print(f"Part 1: {n_paths}")
    print(f"Part 2: {n_paths_special}")


if __name__ == "__main__":
    main()
