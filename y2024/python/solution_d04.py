FILEPATH = "y2024/input/input_d04.txt"


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        word_search = {
            (x, y): c
            for y, line in enumerate(f.read().splitlines())
            for x, c in enumerate(line)
        }

    word = list("XMAS")
    deltas = (-1, 0, 1)
    searches = []
    for (x, y), c in word_search.items():
        if not c == word[0]:
            continue

        for dx in deltas:
            for dy in deltas:
                coordinates = [(x + dx * i, y + dy * i) for i in range(len(word))]
                searches.append([word_search.get((x, y), "") for x, y in coordinates])

    n_matches = sum(search == word for search in searches)
    print(f"Part 1: {n_matches}")
