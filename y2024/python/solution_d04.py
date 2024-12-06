from collections import Counter

FILEPATH = "y2024/input/input_d04.txt"


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        word_search = {
            (x, y): c
            for y, line in enumerate(f.read().splitlines())
            for x, c in enumerate(line)
        }

    deltas_xmas = (-1, 0, 1)
    deltas_x_mas = (-1, 1)
    n_matches_xmas = 0
    n_matches_x_mas = 0
    for (x, y), c in word_search.items():
        if c == "X":
            for dx in deltas_xmas:
                for dy in deltas_xmas:
                    coordinates = [(x + dx * i, y + dy * i) for i in range(4)]
                    search = [word_search.get((x, y), "") for x, y in coordinates]
                    n_matches_xmas += "".join(search) == "XMAS"

        elif c == "A":
            n_matches = 0
            for dx in deltas_x_mas:
                for dy in deltas_x_mas:
                    coordinates = [(x + dx * i, y + dy * i) for i in range(-1, 2)]
                    search = [word_search.get((x, y), "") for x, y in coordinates]
                    n_matches += "".join(search) == "MAS"

            n_matches_x_mas += n_matches == 2

    print(f"Part 1: {n_matches_xmas}")
    print(f"Part 2: {n_matches_x_mas}")
