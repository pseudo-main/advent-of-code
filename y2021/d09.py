def parse_data(data):
    return {
        (x, y): int(n) for x, l in enumerate(data) for y, n in enumerate(l)}


def is_low_point(h_map, c):
    cs_adj = [(c[0]-1, c[1]), (c[0]+1, c[1]), (c[0], c[1]-1), (c[0], c[1]+1)]
    return all(h_map[c] < h_map[c_adj] for c_adj in cs_adj if c_adj in h_map)


def main():
    with open("y2021/input/d09.txt") as file:
        data = file.read().splitlines()

    h_map = parse_data(data)
    risk_sum = sum(h_map[c] + 1 for c in h_map if is_low_point(h_map, c))

    print(f"Part 1: {risk_sum}")


if __name__ == "__main__":
    main()
