def parse_data(data):
    return {
        (x, y): int(n) for x, l in enumerate(data) for y, n in enumerate(l)}


def is_low_point(h_map, c):
    cs_adj = adjacent_coordinates(h_map, c)
    return all(h_map[c] < h_map[c_adj] for c_adj in cs_adj)


def adjacent_coordinates(h_map, c):
    cs_adj = [(c[0]-1, c[1]), (c[0]+1, c[1]), (c[0], c[1]-1), (c[0], c[1]+1)]
    return [c for c in cs_adj if c in h_map]


def get_basin_coordinates(h_map, c):
    cs_adj = adjacent_coordinates(h_map, c)
    basin_local = set(c_adj for c_adj in cs_adj if h_map[c] < h_map[c_adj] < 9)

    basin = set([c])
    for c_basin in basin_local:
        basin = basin.union(get_basin_coordinates(h_map, c_basin))

    return basin


def main():
    with open("y2021/input/d09.txt") as file:
        data = file.read().splitlines()

    h_map = parse_data(data)

    low_point_coords = [c for c in h_map if is_low_point(h_map, c)]
    risk_sum = sum(h_map[c] + 1 for c in low_point_coords)

    basins = []
    for c in low_point_coords:
        basin_size = len(get_basin_coordinates(h_map, c))
        basins.append((basin_size, c))

    basins.sort(reverse=True)
    product_largest_3_basins = basins[0][0] * basins[1][0] * basins[2][0]

    print(f"Part 1: {risk_sum}")
    print(f"Part 2: {product_largest_3_basins}")


if __name__ == "__main__":
    main()
