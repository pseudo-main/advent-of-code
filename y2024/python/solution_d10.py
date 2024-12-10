from collections import deque

FILEPATH = "y2024/input/input_d10.txt"


def get_valid_neighbours(
    map: dict[tuple[int, int] : int], x: int, y: int
) -> set[tuple[int, int]]:
    directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    neighbours = {(x + dx, y + dy) for dx, dy in directions}
    return {n for n in neighbours if map.get(n, -1) == map[(x, y)] + 1}


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        map = {
            (x, y): int(height)
            for y, row in enumerate(f.read().splitlines())
            for x, height in enumerate(row)
        }

    graph = {(x, y): get_valid_neighbours(map, x, y) for x, y in map.keys()}
    trailheads = {(x, y) for x, y in map.keys() if map[(x, y)] == 0}
    score = 0

    for x, y in trailheads:
        seen = set()
        nodes = deque([(x, y)])

        while nodes:
            node = nodes.pop()
            seen.add(node)

            for neighbour in graph[node]:
                nodes.append(neighbour)

        score += sum(map[node] == 9 for node in seen)

    print(f"Part 1: {score}")
