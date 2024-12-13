import re

FILEPATH = "y2024/input/input_d13.txt"


def tokens_required(x_a: int, y_a: int, x_b: int, y_b: int, x_p: int, y_p: int) -> int:
    c_a = 3
    c_b = 1

    det = x_a * y_b - y_a * x_b
    if det == 0:
        return 0

    a = (x_p * y_b - y_p * x_b) / det
    b = (x_a * y_p - y_a * x_p) / det
    if not (a.is_integer() and b.is_integer()):
        return 0

    return int(a * c_a + b * c_b)


if __name__ == "__main__":
    pattern = re.compile(r"(\d+)")
    with open(FILEPATH, "r") as f:
        instructions = [
            list(map(int, pattern.findall(part))) for part in f.read().split("\n\n")
        ]

    tokens_spent = sum(tokens_required(*instruction) for instruction in instructions)
    print(f"Part 1: {tokens_spent}")

    tokens_spent_correct = sum(
        tokens_required(x_a, y_a, x_b, y_b, x_p + 10**13, y_p + 10**13)
        for x_a, y_a, x_b, y_b, x_p, y_p in instructions
    )
    print(f"Part_2: {tokens_spent_correct}")
