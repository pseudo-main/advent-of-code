def parse_data(data):
    axes = [axis.split("=")[1] for axis in data[14:].strip().split(",")]
    return [tuple(map(int, axis.split(".."))) for axis in axes]


def check_trajectory(dx, dy, x_min, x_max, y_min, y_max):
    x, y = 0, 0
    while x <= x_max and y >= y_min:
        if x >= x_min and y <= y_max:
            return True

        x += dx
        y += dy
        dx = max(0, dx - 1)
        dy -= 1

    return False


def main():
    with open("y2021/input/d17.txt") as file:
        data = file.read()

    (x_min, x_max), (y_min, y_max) = parse_data(data)
    max_height = y_min * (y_min + 1) // 2

    min_dx = int((x_min * 2) ** 0.5)
    n_trajectories = 0
    for dx in range(min_dx, x_max + 1):
        for dy in range(y_min, -y_min):
            if check_trajectory(dx, dy, x_min, x_max, y_min, y_max):
                n_trajectories += 1

    print(f"Part 1: {max_height}")
    print(f"Part 2: {n_trajectories}")


if __name__ == "__main__":
    main()
