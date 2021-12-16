from math import prod


def parse_data(data):
    return ''.join(format(int(x, 16), '04b') for x in data.strip())


def parse_packet(packets):
    values = []
    versions = [int(packets[:3], 2)]
    type_id = int(packets[3:6], 2)
    packets = packets[6:]

    if type_id == 4:
        packets, value = parse_literal_packet(packets)
        values.append(value)
    else:
        packets, subversions, subvalues = parse_operator_packet(packets)
        versions += subversions

        if type_id == 0:
            values.append(sum(subvalues))
        elif type_id == 1:
            values.append(prod(subvalues))
        elif type_id == 2:
            values.append(min(subvalues))
        elif type_id == 3:
            values.append(max(subvalues))
        elif type_id == 5:
            values.append(1 if subvalues[0] > subvalues[1] else 0)
        elif type_id == 6:
            values.append(1 if subvalues[0] < subvalues[1] else 0)
        elif type_id == 7:
            values.append(1 if subvalues[0] == subvalues[1] else 0)

    return packets, versions, values


def parse_literal_packet(packets):
    same_packet = True
    bits = ''
    while same_packet:
        if packets[0] == '0':
            same_packet = False

        bits += packets[1:5]
        packets = packets[5:]

    value = int(bits, 2)
    return packets, value


def parse_operator_packet(packets):
    values = []
    length_type_id = packets[0]
    packets = packets[1:]
    versions = []

    if length_type_id == '0':
        total_length = int(packets[:15], 2)
        packets = packets[15:]

        subpackets = packets[:total_length]
        packets = packets[total_length:]

        while subpackets:
            subpackets, subversions, subvalues = parse_packet(subpackets)
            versions += subversions
            values += subvalues
    else:
        n_subpackets = int(packets[:11], 2)
        packets = packets[11:]

        for _ in range(n_subpackets):
            packets, subversions, subvalues = parse_packet(packets)
            versions += subversions
            values += subvalues

    return packets, versions, values


def main():
    with open("y2021/input/d16.txt") as file:
        data = file.read()

    packets = parse_data(data)
    _, versions, values = parse_packet(packets)

    print(f"Part 1: {sum(versions)}")
    print(f"Part 2: {values[0]}")


if __name__ == "__main__":
    main()
