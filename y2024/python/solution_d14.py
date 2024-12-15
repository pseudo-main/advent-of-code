import re

FILEPATH = "y2024/input/input_d14.txt"


if __name__ == "__main__":
    pattern = re.compile(r"-?\d+")
    with open(FILEPATH, "r") as f:
        robots = [
            list(map(int, pattern.findall(line))) for line in f.read().splitlines()
        ]

    max_x, max_y = 101, 103
    split_x = max_x // 2
    split_y = max_y // 2
    s = 100

    robots = [
        [(x + s * dx) % max_x, (y + s * dy) % max_y, dx, dy] for x, y, dx, dy in robots
    ]
    q_counts = [0, 0, 0, 0]
    for x, y, _, _ in robots:
        if x < split_x and y < split_y:
            q_counts[0] += 1
        elif x > split_x and y < split_y:
            q_counts[1] += 1
        elif x < split_x and y > split_y:
            q_counts[2] += 1
        elif x > split_x and y > split_y:
            q_counts[3] += 1

    safety_factor = q_counts[0] * q_counts[1] * q_counts[2] * q_counts[3]
    print(f"Part 1: {safety_factor}")
