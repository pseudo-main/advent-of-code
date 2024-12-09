FILEPATH = "y2024/input/input_d09.txt"


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        disk = [
            block
            for i, c in enumerate(f.read().strip())
            for block in ([i // 2] * int(c) if i % 2 == 0 else ["."] * int(c))
        ]

    idx_last_digit = len(disk) - 1
    idx = 0
    while idx < idx_last_digit:
        if disk[idx] == ".":
            disk[idx] = disk[idx_last_digit]
            disk[idx_last_digit] = "."

            while disk[idx_last_digit] == ".":
                idx_last_digit -= 1

        idx += 1

    checksum = sum(i * x for i, x in enumerate(disk) if x != ".")
    print(f"Part 1: {checksum}")
