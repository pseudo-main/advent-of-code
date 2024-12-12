from collections import defaultdict, deque

FILEPATH = "y2024/samples/sample_d12_p01.txt"


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

    directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    graph = defaultdict(set)
    perimeter_map = {}

    for x, y in map.keys():
        surrounding = {(x + dx, y + dy) for dx, dy in directions}
        same_plot = {s for s in surrounding if map.get(s) == map[(x, y)]}
        graph[(x, y)].update(same_plot)
        perimeter_map[(x, y)] = 4 - len(same_plot)

    total_price = 0
    seen = set()
    for c in map.keys():
        if c in seen:
            continue

        plot = depth_first_search(graph, c)
        seen.update(plot)
        total_price += sum(perimeter_map[pc] for pc in plot) * len(plot)

    print(f"Part 1: {total_price}")
