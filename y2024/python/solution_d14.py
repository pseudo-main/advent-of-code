import re

FILEPATH = "y2024/input/input_d14.txt"


def move_robots(
    robots: list[list[int]], max_x: int, max_y: int, s: int
) -> list[list[int]]:
    return [
        [(x + s * dx) % max_x, (y + s * dy) % max_y, dx, dy] for x, y, dx, dy in robots
    ]


def robots_overlap(robots: list[list[int]]) -> int:
    positions = {(x, y) for x, y, _, _ in robots}
    return len(positions) < len(robots)


if __name__ == "__main__":
    pattern = re.compile(r"-?\d+")
    with open(FILEPATH, "r") as f:
        robots = [
            list(map(int, pattern.findall(line))) for line in f.read().splitlines()
        ]

    max_x, max_y = 101, 103
    robots_100s = move_robots(robots, max_x, max_y, 100)

    split_x = max_x // 2
    split_y = max_y // 2
    q_counts = [0, 0, 0, 0]
    for x, y, _, _ in robots_100s:
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

    s = 0
    while robots_overlap(robots):
        robots = move_robots(robots, max_x, max_y, 1)
        s += 1

    print(f"Part 2: {s}")
