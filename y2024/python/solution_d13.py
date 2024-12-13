import re

FILEPATH = "y2024/input/input_d13.txt"


if __name__ == "__main__":
    pattern = re.compile(r"(\d+)")
    with open(FILEPATH, "r") as f:
        instructions = [
            list(map(int, pattern.findall(part)))
            for part in f.read().split("\n\n")
        ]

    tokens_spent = 0
    c1 = 3
    c2 = 1
    for v1_x, v1_y, v2_x, v2_y, v3_x, v3_y in instructions:
        det = v1_x * v2_y - v1_y * v2_x
        if det != 0:
            x1 = (v3_x * v2_y - v3_y * v2_x) / det
            x2 = (v1_x * v3_y - v1_y * v3_x) / det
            
            if (x1 % 1 == 0) and (x2 % 1 == 0) and (0 <= x1 <= 100) and (0 <= x2 <= 100):
                tokens_spent += int(x1 * c1 + x2 * c2)

    print(f"Part 1: {tokens_spent}")
