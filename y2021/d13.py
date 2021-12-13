def parse_data(data):
    dots = set(tuple(map(int, d.split(','))) for d in data[0].splitlines())
    folds = []
    for f in data[1].splitlines():
        if 'x' in f:
            folds.append((int(f.split('=')[-1]), 0))
        else:
            folds.append((0, int(f.split('=')[-1])))

    return dots, folds


def fold_paper(dots, fold):
    dx, dy = fold
    dots_new = set()
    for x, y in dots:
        if dx:
            x_new = min(x, 2 * dx - x)
            dots_new.add((x_new, y))
        else:
            y_new = min(y, 2 * dy - y)
            dots_new.add((x, y_new))

    return dots_new


def print_paper(dots):
    x_max, y_max = max(dots)
    for y in range(y_max+1):
        print(''.join('#' if (x, y) in dots else '.' for x in range(x_max+1)))


def main():
    with open("y2021/input/d13.txt") as file:
        data = file.read().split("\n\n")

    dots, folds = parse_data(data)

    for i, fold in enumerate(folds):
        dots = fold_paper(dots, fold)
        if i == 0:
            n_dots_1 = len(dots)

    print(f"Part 1: {n_dots_1}")
    print("Part 2:")
    print_paper(dots)


if __name__ == "__main__":
    main()
