def parse_data(data):
    return [[part.split() for part in line.split(" | ")] for line in data]


def translate_digit(note):
    l_map = {len(x): set(x) for x in note[0] if len(x) in [2, 3, 4, 7]}

    digit = ""
    for y in note[1]:
        n_intersect_1 = len(set(y) & set(l_map[2]))
        n_intersect_4 = len(set(y) & set(l_map[4]))

        if len(y) == 6 and n_intersect_1 == 2 and n_intersect_4 == 3:
            digit += '0'
        elif len(y) == 2:
            digit += '1'
        elif len(y) == 5 and n_intersect_4 == 2:
            digit += '2'
        elif len(y) == 5 and n_intersect_1 == 2:
            digit += '3'
        elif len(y) == 4:
            digit += '4'
        elif len(y) == 5 and n_intersect_1 == 1:
            digit += '5'
        elif len(y) == 6 and n_intersect_1 == 1:
            digit += '6'
        elif len(y) == 3:
            digit += '7'
        elif len(y) == 7:
            digit += '8'
        elif len(y) == 6 and n_intersect_4 == 4:
            digit += '9'

    return int(digit)


def main():
    with open("y2021/input/d08.txt") as file:
        data = file.read().splitlines()

    notes = parse_data(data)
    n_1478 = sum(1 for n in notes for s in n[1] if len(s) in [2, 3, 4, 7])
    sum_digits = sum(translate_digit(note) for note in notes)

    print(f"Part 1: {n_1478}")
    print(f"Part 2: {sum_digits}")


if __name__ == "__main__":
    main()
