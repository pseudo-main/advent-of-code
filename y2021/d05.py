from collections import defaultdict


def parse_data(data):
    lines_coords = []
    for line in data:
        coords = [tuple(map(int, c.split(","))) for c in line.split(" -> ")]
        lines_coords.append(coords)
    return lines_coords


def coords_vertical_line(x, y1, y2):
    return [(x, y) for y in range(min(y1, y2), max(y1, y2) + 1)]


def coords_horizontal_line(x1, x2, y):
    return [(x, y) for x in range(min(x1, x2), max(x1, x2) + 1)]


def coords_diagonal_line(x1, x2, y1, y2):
    x_sign = int((x1 - x2) / -abs(x1 - x2))
    y_sign = int((y1 - y2) / -abs(y1 - y2))
    line_x = list(range(x1, x2 + x_sign, x_sign))
    line_y = list(range(y1, y2 + y_sign, y_sign))
    return zip(line_x, line_y)


def main():
    with open("y2021/input/d05.txt") as file:
        data = file.read().splitlines()

    lines_coords = parse_data(data)
    positions = defaultdict(int)
    positions_diag = defaultdict(int)

    for (x1, y1), (x2, y2) in lines_coords:
        if x1 == x2:
            line = coords_vertical_line(x1, y1, y2)
            for c in line:
                positions[c] += 1
        elif y1 == y2:
            line = coords_horizontal_line(x1, x2, y1)
            for c in line:
                positions[c] += 1
        else:
            line = coords_diagonal_line(x1, x2, y1, y2)
            for c in line:
                positions_diag[c] += 1

    for p in positions.keys():
        positions_diag[p] += positions[p]

    n_line_intersections = sum(p >= 2 for p in positions.values())
    n_line_intersections_diag = sum(p >= 2 for p in positions_diag.values())

    print(f"Part 1: {n_line_intersections}")
    print(f"Part 2: {n_line_intersections_diag}")


if __name__ == "__main__":
    main()
