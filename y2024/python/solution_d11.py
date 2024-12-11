FILEPATH = "y2024/input/input_d11.txt"


def blink(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        split = len(str(stone)) // 2
        return [int(str(stone)[:split]), int(str(stone)[split:])]
    else:
        return [stone * 2024]


def count_after_blinking(stone: int, iteration: int) -> int:
    stones_after_blinking = blink(stone)

    if iteration == 1:
        return len(stones_after_blinking)

    n_stones = 0
    for stone_after_blinking in stones_after_blinking:
        n_stones += count_after_blinking(stone_after_blinking, iteration - 1)

    return n_stones


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        stones = [int(x) for x in f.read().split()]

    n_stones_25_iterations = sum(count_after_blinking(stone, 25) for stone in stones)
    print(f"Part 1: {n_stones_after_25_iterations}")
