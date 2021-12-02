def parse_data(data):
    return [command.split() for command in data]


def main():
    with open("y2021/input/d02.txt") as file:
        data = file.read().splitlines()

    commands = parse_data(data)

    x = 0
    y = 0

    direction_map = {
        'forward': {'x': 1, 'y': 0},
        'down': {'x': 0, 'y': 1},
        'up': {'x': 0, 'y': -1}
    }

    for direction, units in commands:
        dx = direction_map[direction]['x'] * int(units)
        dy = direction_map[direction]['y'] * int(units)
        x += dx
        y += dy

    multiple = x * y
    print(f"Part 1: {multiple}")


if __name__ == "__main__":
    main()
