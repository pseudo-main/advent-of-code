from statistics import median
from sys import maxsize


def parse_data(data):
    return [int(x) for x in data.split(",")]


def triangle_n(n):
    return n * (n+1) // 2


def main():
    with open("y2021/input/d07.txt") as file:
        data = file.read()

    ps = parse_data(data)
    fuel_cost = int(sum(abs(p - median(ps)) for p in ps))

    fuel_cost_2 = maxsize
    for x in range(min(ps), max(ps) + 1):
        fuel_cost_2_next = sum(triangle_n(abs(p - x)) for p in ps)
        if fuel_cost_2_next > fuel_cost_2:
            break

        fuel_cost_2 = fuel_cost_2_next

    print(f"Part 1: {fuel_cost}")
    print(f"Part 2: {fuel_cost_2}")


if __name__ == "__main__":
    main()
