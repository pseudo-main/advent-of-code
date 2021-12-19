from math import floor, ceil
import ast


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
        final_sum = [final_sum, snailfish_number]
        while True:
            exploded, _, final_sum, _ = explode(final_sum)
            if exploded:
                continue

            did_split, final_sum = split(final_sum)
            if not did_split:
                break

    final_sum_magnitude = magnitude(final_sum)

    print(f"Part 1: {final_sum_magnitude}")


if __name__ == "__main__":
    main()
