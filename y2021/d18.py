import ast
from itertools import permutations
from math import floor, ceil


def parse_data(data):
    return [ast.literal_eval(sn) for sn in data.splitlines()]


def add_left(pair, addition):
    if isinstance(pair, list):
        return [pair[0], add_left(pair[1], addition)]
    else:
        return pair + addition


def add_right(pair, addition):
    if isinstance(pair, list):
        return [add_right(pair[0], addition), pair[1]]
    else:
        return pair + addition


def explode(pair, depth=0):
    if isinstance(pair, list):
        subpair_l, subpair_r = pair
        if depth == 4:
            return True, subpair_l, 0, subpair_r

        else:
            exploded_l, l, subpair_l, r = explode(subpair_l, depth+1)
            if exploded_l:
                return True, l, [subpair_l, add_right(subpair_r, r)], 0

            exploded_r, l, subpair_r, r = explode(subpair_r, depth+1)
            if exploded_r:
                return True, 0, [add_left(subpair_l, l), subpair_r], r

            if not exploded_l or exploded_r:
                return False, 0, pair, 0

    else:
        return False, 0, pair, 0


def split(pair):
    if isinstance(pair, list):
        subpair_l, subpair_r = pair
        did_split_l, subpair_l = split(subpair_l)
        if did_split_l:
            return True, [subpair_l, subpair_r]

        did_split_r, subpair_r = split(subpair_r)
        if did_split_r:
            return True, [subpair_l, subpair_r]

        if not did_split_l or did_split_r:
            return False, [subpair_l, subpair_r]

    else:
        if pair > 9:
            return True, [floor(pair / 2), ceil(pair / 2)]
        else:
            return False, pair


def add_reduce(snailfish_number_l, snailfish_number_r):
    snailfish_number = [snailfish_number_l, snailfish_number_r]
    while True:
        exploded, _, snailfish_number, _ = explode(snailfish_number)
        if exploded:
            continue

        did_split, snailfish_number = split(snailfish_number)
        if not did_split:
            return snailfish_number


def magnitude(pair):
    if isinstance(pair, list):
        subpair_l, subpair_r = pair
        magnitude_l = magnitude(subpair_l)
        magnitude_r = magnitude(subpair_r)
        return 3 * magnitude_l + 2 * magnitude_r
    else:
        return pair


def main():
    with open("y2021/input/d18.txt") as file:
        data = file.read()

    snailfish_numbers = parse_data(data)

    final_sum = snailfish_numbers[0]
    for snailfish_number in snailfish_numbers[1:]:
        final_sum = add_reduce(final_sum, snailfish_number)

    final_sum_magnitude = magnitude(final_sum)
    final_sum_magnitude_max = max(
        magnitude(add_reduce(*p)) for p in permutations(snailfish_numbers, 2))

    print(f"Part 1: {final_sum_magnitude}")
    print(f"Part 2: {final_sum_magnitude_max}")


if __name__ == "__main__":
    main()
