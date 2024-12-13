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
    for dx_a, dy_a, dx_b, dy_b, x_p, y_p in instructions:
        solutions = []

        for i in range(101):
            dx, dy = (x_p - dx_a * i, y_p - dy_a * i)
            if (dx or dy) <= 0:
                break
            
            j = dx // dx_b
            if j <= 100 and (j * dy_b == dy):
                solutions.append((i*3 + j, i, j))

        if solutions:
            tokens_spent += sorted(solutions)[0][0]

    print(f"Part 1: {tokens_spent}")
