FILEPATH = "y2024/samples/sample_d06_p01.txt"


def patrol(map: dict[(int, int): str], x: int, y: int) -> set[(int, int)]:
    dx, dy = (0, -1)
    directions = {
        (0, -1): (1, 0),
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
    }
    visited = {(x, y)}

    while (x, y) in map:
        if (x + dx, y + dy) not in map:
            return visited

        if map[(x + dx, y + dy)] != "#":
            x += dx
            y += dy
            visited.add((x, y))
        else:
            dx, dy = directions[(dx, dy)]


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        map = {
            (x, y): c
            for y, row in enumerate(f.read().splitlines())
            for x, c in enumerate(row)
        }

    x, y = list(map.keys())[list(map.values()).index("^")]
    visited = patrol(map, x, y)
    print(f"Part 1: {len(visited)}")
