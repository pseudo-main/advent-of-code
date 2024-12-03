from collections import Counter


FILEPATH = "y2024/input/input_d01.txt"


def read_input(filepath: str) -> (list, list):
    location_ids_a = []
    location_ids_b = []

    with open(filepath, "r") as f:
        for line in f:
            a, b = line.split()
            location_ids_a.append(int(a))
            location_ids_b.append(int(b))

    return location_ids_a, location_ids_b


if __name__ == "__main__":
    ids_a, ids_b = read_input(FILEPATH)

    total_distance = sum(abs(a - b) for a, b in zip(sorted(ids_a), sorted(ids_b)))
    print(f"Part 1: {total_distance}")

    ids_b_counts = Counter(ids_b)
    similarity_score = sum(a * ids_b_counts[a] for a in ids_a)
    print(f"Part 2: {similarity_score}")
