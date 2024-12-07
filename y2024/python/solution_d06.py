FILEPATH = "y2024/input/input_d06.txt"


def patrol(map: dict[(int, int):str], x: int, y: int) -> (bool, set[(int, int)]):
    dx, dy = (0, -1)
    directions = {
        (0, -1): (1, 0),
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
    }
    visited = {(x, y)}
    turns = {(x, y, dx, dy)}

    while (x, y) in map:
        if (x + dx, y + dy) not in map:
            return False, visited

        if map[(x + dx, y + dy)] == "#":
            dx, dy = directions[(dx, dy)]

            if (x, y, dx, dy) in turns:
                return True, visited

            turns.add((x, y, dx, dy))

        x += dx
        y += dy
        visited.add((x, y))


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        map = {
            (x, y): c
            for y, row in enumerate(f.read().splitlines())
            for x, c in enumerate(row)
        }

    x, y = list(map.keys())[list(map.values()).index("^")]
    _, visited = patrol(map, x, y)
    print(f"Part 1: {len(visited)}")

    n_obstruction_positions = 0
    for coordinate in visited:
        map[coordinate] = "#"
        is_loop, _ = patrol(map, x, y)
        n_obstruction_positions += is_loop
        map[coordinate] = "."

    print(f"Part 2: {n_obstruction_positions}")
