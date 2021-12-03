def parse_data(data):
    return [list(map(int, x)) for x in data]


def bit_list_to_decimal(bit_list):
    decimal = 0
    for bit in bit_list:
        decimal = (decimal << 1) | bit
    return decimal


def main():
    with open("y2021/input/d03.txt") as file:
        data = file.read().splitlines()

    binary_numbers = parse_data(data)
    bit_averages = [sum(b) / len(binary_numbers) for b in zip(*binary_numbers)]
    bit_common = [round(b) for b in bit_averages]
    bit_uncommon = [round(1 - b) for b in bit_averages]

    gamma_rate = bit_list_to_decimal(bit_common)
    epsilon_rate = bit_list_to_decimal(bit_uncommon)
    power_consumption = gamma_rate * epsilon_rate

    print(f"Part 1: {power_consumption}")


if __name__ == "__main__":
    main()
