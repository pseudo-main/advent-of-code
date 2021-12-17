def parse_data(data):
    axes = [axis.split("=")[1] for axis in data[14:].strip().split(",")]
    return [tuple(map(int, axis.split(".."))) for axis in axes]


def main():
    with open("y2021/input/d17.txt") as file:
        data = file.read()

    (x__min, x_max), (y_min, y_max) = parse_data(data)

    max_height = (y_min * (y_min + 1)) // 2

    print(f"Part 1: {max_height}")


if __name__ == "__main__":
    main()
