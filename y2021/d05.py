from collections import defaultdict


def parse_data(data):
    lines_coords = []
    for line in data:
        coords = [tuple(map(int, c.split(","))) for c in line.split(" -> ")]
        lines_coords.append(coords)
    return lines_coords


def main():
    with open("y2021/input/d05.txt") as file:
        data = file.read().splitlines()

    lines_coords = parse_data(data)
    positions = defaultdict(int)

    for (x1, y1), (x2, y2) in lines_coords:
        if x1 == x2:
            line = [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
            for c in line:
                positions[c] += 1
        elif y1 == y2:
            line = [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
            for c in line:
                positions[c] += 1

    n_line_intersections = sum(p >= 2 for p in positions.values())

    print(f"Part 1: {n_line_intersections}")


if __name__ == "__main__":
    main()
