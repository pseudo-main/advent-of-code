import re

FILEPATH = "y2024/input/input_d13.txt"


def cramers_rule(
    v1_x: int, v1_y: int, v2_x: int, v2_y: int, v3_x: int, v3_y: int
) -> tuple[float, float]:
    det = v1_x * v2_y - v1_y * v2_x
    if det == 0:
        return -1.0, -1.0

    x1 = (v3_x * v2_y - v3_y * v2_x) / det
    x2 = (v1_x * v3_y - v1_y * v3_x) / det
    return x1, x2


if __name__ == "__main__":
    pattern = re.compile(r"(\d+)")
    with open(FILEPATH, "r") as f:
        instructions = [
            list(map(int, pattern.findall(part))) for part in f.read().split("\n\n")
        ]

    tokens_spent = 0
    tokens_spent_p2 = 0
    c1 = 3
    c2 = 1

    for v1_x, v1_y, v2_x, v2_y, v3_x, v3_y in instructions:
        x1, x2 = cramers_rule(v1_x, v1_y, v2_x, v2_y, v3_x, v3_y)
        if (x1 % 1 == 0) and (x2 % 1 == 0) and (0 <= x1 <= 100) and (0 <= x2 <= 100):
            tokens_spent += int(x1 * c1 + x2 * c2)

        x1_p2, x2_p2 = cramers_rule(
            v1_x, v1_y, v2_x, v2_y, v3_x + int(1e13), v3_y + int(1e13)
        )
        if (x1_p2 % 1 == 0) and (x2_p2 % 1 == 0):
            tokens_spent_p2 += int(x1_p2 * c1 + x2_p2 * c2)

    print(f"Part 1: {tokens_spent}")
    print(f"Part_2: {tokens_spent_p2}")
