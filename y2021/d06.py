from collections import Counter


def parse_data(data):
    return Counter([int(n) for n in data.split(",")])


def main():
    with open("y2021/input/d06.txt") as file:
        data = file.read()

    n_fish = parse_data(data)

    for i in range(256):
        n_offspring = n_fish[0]
        for age in range(8):
            n_fish[age] = n_fish[age + 1]

        n_fish[6] += n_offspring
        n_fish[8] = n_offspring

        if i == 79:
            n_fish_80d = sum(n_fish.values())

    n_fish_256d = sum(n_fish.values())

    print(f"Part 1: {n_fish_80d}")
    print(f"Part 2: {n_fish_256d}")


if __name__ == "__main__":
    main()
