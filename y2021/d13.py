def parse_data(data):
    dots = set(tuple(map(int, d.split(','))) for d in data[0].splitlines())
    folds = []
    for f in data[1].splitlines():
        if 'x' in f:
            folds.append((int(f.split('=')[-1]), 0))
        else:
            folds.append((0, int(f.split('=')[-1])))
    return dots, folds


def main():
    with open("y2021/input/d13.txt") as file:
        data = file.read().split("\n\n")

    dots, folds = parse_data(data)

    dx, dy = folds[0]
    dots_new = set()
    for x, y in dots:
        if dx:
            if x - dx < 0:
                dots_new.add((x, y))
            else:
                dots_new.add((2 * dx - x, y))
        else:
            if y - dy < 0:
                dots_new.add((x, y))
            else:
                dots_new.add((x, 2 * dy - y))

    n_dots = len(dots_new)
    print(f"Part 1: {n_dots}")


if __name__ == "__main__":
    main()
