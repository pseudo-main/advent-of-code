from collections import defaultdict, deque

FILEPATH = "y2024/input/input_d12.txt"


def depth_first_search(
    graph: dict[tuple[int, int], set[tuple[int, int]]], c: tuple[int, int]
) -> set[tuple[int, int]]:
    nodes = deque([c])
    seen = set()

    while nodes:
        node = nodes.pop()
        seen.add(node)

        for neighbour in graph[node]:
            if neighbour not in seen:
                nodes.append(neighbour)

    return seen


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        map = {
            (x, y): c
            for y, row in enumerate(f.read().splitlines())
            for x, c in enumerate(row)
        }

    directions = {"E": (1, 0), "W": (-1, 0), "S": (0, 1), "N": (0, -1)}
    graph = defaultdict(set)
    perimeter_map = defaultdict(set)

    for x, y in map.keys():
        for direction, (dx, dy) in directions.items():
            c = (x + dx, y + dy)
            if map.get(c) == map[(x, y)]:
                graph[(x, y)].add(c)
            else:
                perimeter_map[(x, y)].add(direction)

    total_price = 0
    seen = set()
    for c in map.keys():
        if c in seen:
            continue

        plot = depth_first_search(graph, c)
        seen.update(plot)
        total_price += sum(len(perimeter_map[pc]) for pc in plot) * len(plot)

    print(f"Part 1: {total_price}")
