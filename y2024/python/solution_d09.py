FILEPATH = "y2024/input/input_d09.txt"


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        disk = [
            block
            for i, c in enumerate(f.read().strip())
            for block in ([i // 2] * int(c) if i % 2 == 0 else ["."] * int(c))
        ]

    disk_blocks = disk.copy()
    j = len(disk_blocks) - 1
    i = 0
    while i < j:
        if disk_blocks[i] != ".":
            i += 1
            continue

        disk_blocks[i] = disk_blocks[j]
        disk_blocks[j] = "."

        while disk_blocks[j] == ".":
            j -= 1

    checksum_blocks = sum(i * x for i, x in enumerate(disk_blocks) if x != ".")
    print(f"Part 1: {checksum_blocks}")

    disk_files = disk.copy()
    file_size = 0
    for i in range(len(disk_files))[::-1]:
        if file_size == 0 and disk_files[i] == ".":
            continue

        if disk_files[i + file_size] == disk_files[i]:
            file_size += 1
            continue

        space_size = 0
        for j in range(i + 2):
            if space_size == file_size:
                disk_files[j - space_size : j] = disk_files[i + 1 : i + file_size + 1]
                disk_files[i + 1 : i + file_size + 1] = "." * file_size
                break

            if disk_files[j] == ".":
                space_size += 1
                continue

            space_size = 0

        if disk_files[i] != ".":
            file_size = 1
        else:
            file_size = 0

    checksum_files = sum(i * x for i, x in enumerate(disk_files) if x != ".")
    print(f"Part 2: {checksum_files}")
