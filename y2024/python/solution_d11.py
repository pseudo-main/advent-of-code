from functools import lru_cache

FILEPATH = "y2024/input/input_d11.txt"


@lru_cache(maxsize=None)
def blink(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        split = len(str(stone)) // 2
        return [int(str(stone)[:split]), int(str(stone)[split:])]
    else:
        return [stone * 2024]


@lru_cache(maxsize=None)
def count_after_blinking(stone: int, iteration: int) -> int:
    stones = blink(stone)

    if iteration == 1:
        return len(stones)

    return sum(count_after_blinking(s, iteration - 1) for s in stones)


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        stones = [int(x) for x in f.read().split()]

    n_stones_25 = sum(count_after_blinking(stone, 25) for stone in stones)
    print(f"Part 1: {n_stones_25}")

    n_stones_75 = sum(count_after_blinking(stone, 75) for stone in stones)
    print(f"Part 2: {n_stones_75}")
