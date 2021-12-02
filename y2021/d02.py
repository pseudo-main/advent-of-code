def parse_data(data):
    return [command.split() for command in data]


def course_simple(commands):
    x, y = 0, 0

    direction_map = {
        'forward': {'x': 1, 'y': 0},
        'down': {'x': 0, 'y': 1},
        'up': {'x': 0, 'y': -1}
    }

    for direction, units in commands:
        x += direction_map[direction]['x'] * int(units)
        y += direction_map[direction]['y'] * int(units)

    return x, y


def course_complex(commands):
    x, y, aim = 0, 0, 0
    aim_map = {'down': 1, 'up': -1}

    for instruction, units in commands:
        if instruction == 'forward':
            x += int(units)
            y += aim * int(units)
        else:
            aim += aim_map[instruction] * int(units)

    return x, y


def main():
    with open("y2021/input/d02.txt") as file:
        data = file.read().splitlines()

    commands = parse_data(data)
    x_simple, y_simple = course_simple(commands)
    multiple_simple = x_simple * y_simple

    x_complex, y_complex = course_complex(commands)
    multiple_complex = x_complex * y_complex

    print(f"Part 1: {multiple_simple}")
    print(f"Part 2: {multiple_complex}")


if __name__ == "__main__":
    main()
