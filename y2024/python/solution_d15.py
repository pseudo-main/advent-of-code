FILEPATH = "y2024/input/input_d15.txt"


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        warehouse_raw, moves_raw = f.read().split("\n\n")

    warehouse = {
        (x, y): c
        for y, row in enumerate(warehouse_raw.splitlines())
        for x, c in enumerate(row)
    }
    moves = [x for row in moves_raw for x in row.strip()]
    x, y = list(warehouse.keys())[list(warehouse.values()).index("@")]
    warehouse[(x, y)] = "."
    directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

    for move in moves:
        dx, dy = directions[move]
        x_dir, y_dir = x + dx, y + dy

        if warehouse[(x_dir, y_dir)] == ".":
            x, y = x_dir, y_dir
            continue

        while warehouse[(x_dir, y_dir)] == "O":
            x_dir, y_dir = x_dir + dx, y_dir + dy

        if warehouse[(x_dir, y_dir)] == ".":
            warehouse[(x_dir, y_dir)] = "O"
            warehouse[(x + dx, y + dy)] = "."
            x, y = x + dx, y + dy

    boxes = [c for c in warehouse if warehouse[c] == "O"]
    gps_sum = sum(100 * y + x for x, y in boxes)
    print(f"Part 1: {gps_sum}")
