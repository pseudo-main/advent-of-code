from statistics import median


def parse_data(data):
    return [int(x) for x in data.split(",")]


def main():
    with open("y2021/input/d07.txt") as file:
        data = file.read()

    ps = parse_data(data)
    fuel_cost = sum(abs(p - median(ps)) for p in ps)

    print(f"Part 1: {fuel_cost}")


if __name__ == "__main__":
    main()
