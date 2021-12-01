def parse_data(data):
    return [int(measurement) for measurement in data]


def main():
    with open("y2021/input/d01.txt") as file:
        data = file.read().splitlines()

    depths = parse_data(data)
    n_increasing = sum(
        depths[i] < depths[i+1] for i in range(len((depths)) - 1))

    print(f"Part 1: {n_increasing}")


if __name__ == "__main__":
    main()
