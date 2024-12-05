from collections import Counter

FILEPATH = "y2024/input/input_d01.txt"


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        line_ids = [map(int, line.split()) for line in f]

    ids_a, ids_b = map(list, zip(*line_ids))
    total_distance = sum(abs(a - b) for a, b in zip(sorted(ids_a), sorted(ids_b)))
    print(f"Part 1: {total_distance}")

    ids_b_counts = Counter(ids_b)
    similarity_score = sum(a * ids_b_counts[a] for a in ids_a)
    print(f"Part 2: {similarity_score}")
