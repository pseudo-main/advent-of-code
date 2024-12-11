FILEPATH = "y2024/input/input_d11.txt"


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        stones = [int(x) for x in f.read().split()]

    for _ in range(25):
        i = 0
        while i < len(stones):
            stone = stones[i]
            if stone == 0:
                stones[i] = 1
            elif len(str(stone)) % 2 == 0:
                split = len(str(stone)) // 2
                stones[i] = int(str(stone)[:split])
                stones.insert(i + 1, int(str(stone)[split:]))
                i += 1
            else:
                stones[i] = stone * 2024

            i += 1

    print(f"Part 1: {len(stones)}")
