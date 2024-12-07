FILEPATH = "y2024/input/input_d06.txt"


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        map = {
            (x, y): c
            for y, row in enumerate(f.read().splitlines())
            for x, c in enumerate(row)
        }

    x, y = list(map.keys())[list(map.values()).index("^")]
    visited = {(x, y)}
    dx, dy = (0, -1)
    turns = {
        (0, -1): (1, 0),
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
    }

    while (x, y) in map:
        if (x + dx, y + dy) not in map:
            break

        if map[(x + dx, y + dy)] != "#":
            x += dx
            y += dy
            visited.add((x, y))
        else:
            dx, dy = turns[(dx, dy)]

    print(f"Part 1: {len(visited)}")
