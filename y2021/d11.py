def parse_data(data):
    return {
        (x, y): int(n) for x, l in enumerate(data) for y, n in enumerate(l)}


def octos_adj(grid, octo):
    x, y = octo
    octos_adj = set((x+dx, y+dy) for dx in range(-1, 2) for dy in range(-1, 2))
    return octos_adj.intersection(grid)


def step(grid):
    grid = {octo: energy + 1 for octo, energy in grid.items()}
    octos_f = set(octo for octo, energy in grid.items() if energy > 9)
    octos_f_done = set()

    while octos_f:
        for octo in octos_f:
            octos_f_done.add(octo)
            octos_adj_f = octos_adj(grid, octo)
            for octo_adj in octos_adj_f:
                grid[octo_adj] += 1

        octos_e9 = set(octo for octo, energy in grid.items() if energy > 9)
        octos_f = octos_e9.difference(octos_f_done)

    for octo in octos_f_done:
        grid[octo] = 0

    return grid, len(octos_f_done)


def main():
    with open("y2021/input/d11.txt") as file:
        data = file.read().splitlines()

    grid = parse_data(data)

    n_flashes_100s = 0
    n_steps = 0
    while True:
        n_steps += 1
        grid, n_flashes = step(grid)
        if n_steps <= 100:
            n_flashes_100s += n_flashes

        if n_flashes == 100:
            break

    print(f"Part 1: {n_flashes_100s}")
    print(f"Part 2: {n_steps}")


if __name__ == "__main__":
    main()
