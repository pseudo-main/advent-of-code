def parse_data(data):
    return [int(n) for n in data.split(",")]


def main():
    with open("y2021/input/d06.txt") as file:
        data = file.read()

    fish_ages = parse_data(data)
    for _ in range(80):
        fish_ages += [9] * fish_ages.count(0)
        fish_ages = [age - 1 if not age == 0 else 6 for age in fish_ages]

    print(f"Part 1: {len(fish_ages)}")


if __name__ == "__main__":
    main()
