def parse_data(data):
    return [int(measurement) for measurement in data]


def count_increasing(numbers):
    return sum(numbers[i] < numbers[i+1] for i in range(len((numbers)) - 1))


def moving_average(numbers, window_size=3):
    moving_averages = []
    for i in range(len(numbers) - window_size + 1):
        window = numbers[i:i+window_size]
        moving_average = sum(window) / len(window)
        moving_averages.append(moving_average)
    return moving_averages


def main():
    with open("y2021/input/d01.txt") as file:
        data = file.read().splitlines()

    depths = parse_data(data)
    n_increasing = count_increasing(depths)

    depths_moving_averages = moving_average(depths)
    n_increasing_moving_averages = count_increasing(depths_moving_averages)

    print(f"Part 1: {n_increasing}")
    print(f"Part 2: {n_increasing_moving_averages}")


if __name__ == "__main__":
    main()
