import re

FILEPATH = "y2024/input/input_d03.txt"


def extract_muls(memory: str) -> list[tuple[int, int]]:
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    return [(int(a), int(b)) for a, b in pattern.findall(memory)]


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        memory = f.read()

    total = sum(a * b for a, b in extract_muls(memory))
    print(f"Part 1: {total}")

    enabled_memory = "".join(part.split("don't()")[0] for part in memory.split("do()"))
    enabled_total = sum(a * b for a, b in extract_muls(enabled_memory))
    print(f"Part 2: {enabled_total}")
