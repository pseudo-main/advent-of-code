def parse_data(data):
    return [list(map(int, x)) for x in data]


def bit_list_to_decimal(bit_list):
    decimal = 0
    for bit in bit_list:
        decimal = (decimal << 1) | bit
    return decimal


def common_bit_list(bit_lists, most_common=True):
    bit_averages = [sum(b) / len(bit_lists) for b in zip(*bit_lists)]
    if most_common:
        bit_averages = [1 if b == 0.5 else b for b in bit_averages]
        return [round(b) for b in bit_averages]
    return [round(1 - b) for b in bit_averages]


def filter_bit_lists(bit_lists, most_common=True):
    n_bits = len(bit_lists[0])
    for i in range(n_bits):
        if len(bit_lists) == 1:
            break
        bit_common = common_bit_list(bit_lists, most_common)[i]
        bit_lists = [bl for bl in bit_lists if bl[i] == bit_common]
        i += 1
    return bit_lists[0]


def main():
    with open("y2021/input/d03.txt") as file:
        data = file.read().splitlines()

    bit_lists = parse_data(data)

    gamma_rate = bit_list_to_decimal(common_bit_list(bit_lists, True))
    epsilon_rate = bit_list_to_decimal(common_bit_list(bit_lists, False))
    power_consumption = gamma_rate * epsilon_rate

    oxygen_rating = bit_list_to_decimal(filter_bit_lists(bit_lists, True))
    co2_rating = bit_list_to_decimal(filter_bit_lists(bit_lists, False))
    life_rating = oxygen_rating * co2_rating

    print(f"Part 1: {power_consumption}")
    print(f"Part 2: {life_rating}")


if __name__ == "__main__":
    main()
