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
    antinodes_harmonic = {l for locations in antennas.values() for l in locations}
    for (x1, y1), (x2, y2) in combos:
        dx, dy = (x2 - x1, y2 - y1)

        x, y = (x1 - dx, y1 - dy)
        if 0 <= x < len(lines[0]) and 0 <= y < len(lines):
            antinodes.add((x, y))

        while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
            antinodes_harmonic.add((x, y))
            x, y = (x - dx, y - dy)

        x, y = (x2 + dx, y2 + dy)
        if 0 <= x < len(lines[0]) and 0 <= y < len(lines):
            antinodes.add((x, y))

        while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
            antinodes_harmonic.add((x, y))
            x, y = (x + dx, y + dy)

    print(f"Part 1: {len(antinodes)}")
    print(f"Part 2: {len(antinodes_harmonic)}")
