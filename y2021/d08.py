def parse_data(data):
    notes = []
    for line in data:
        note = [signals.split() for signals in line.split(" | ")]
        notes.append(note)
    return notes


def main():
    with open("y2021/input/d08.txt") as file:
        data = file.read().splitlines()

    notes = parse_data(data)
    n_1478 = sum(1 for n in notes for s in n[1] if len(s) in [2, 3, 4, 7])

    print(f"Part 1: {n_1478}")


if __name__ == "__main__":
    main()
