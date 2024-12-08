from collections import defaultdict
from itertools import combinations

FILEPATH = "y2024/input/input_d08.txt"


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        lines = f.read().splitlines()

    antennas = defaultdict(set)
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c != ".":
                antennas[c].add((x, y))

    combos = [
        combo for locations in antennas.values() for combo in combinations(locations, 2)
    ]

    antinodes = set()
    for (x1, y1), (x2, y2) in combos:
        dx, dy = (x2 - x1, y2 - y1)
        antinodes.add((x1 - dx, y1 - dy))
        antinodes.add((x2 + dx, y2 + dy))

    n_valid = sum(
        0 <= x < len(lines[0]) and 0 <= y < len(lines) for (x, y) in antinodes
    )
    print(f"Part 1: {n_valid}")

    antinodes_harmonic = {
        location for locations in antennas.values() for location in locations
    }
    for (x1, y1), (x2, y2) in combos:
        dx, dy = (x2 - x1, y2 - y1)

        x, y = (x1 - dx, y1 - dy)
        while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
            antinodes_harmonic.add((x, y))
            x, y = (x - dx, y - dy)

        x, y = (x2 + dx, y2 + dy)
        while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
            antinodes_harmonic.add((x, y))
            x, y = (x + dx, y + dy)

    print(f"Part 2: {len(antinodes_harmonic)}")
