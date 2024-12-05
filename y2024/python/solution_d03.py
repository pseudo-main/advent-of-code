import re

FILEPATH = "y2024/input/input_d03.txt"


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        lines = f.readlines()

    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    muls = [tuple(map(int, mul)) for line in lines for mul in pattern.findall(line)]
    total = sum(a * b for a, b in muls)
    print(f"Part 1: {total}")
