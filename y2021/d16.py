def parse_data(data):
    return ''.join(format(int(x, 16), '04b') for x in data.strip())


def parse_packet(packets):
    versions = [int(packets[:3], 2)]
    type_id = int(packets[3:6], 2)
    packets = packets[6:]

    if type_id == 4:
        packets = parse_literal_packet(packets)
    else:
        packets, subversions = parse_operator_packet(packets)
        versions += subversions

    return packets, versions


def parse_literal_packet(packets):
    same_packet = True
    while same_packet:
        if packets[0] == '0':
            same_packet = False

        packets = packets[5:]

    return packets


def parse_operator_packet(packets):
    length_type_id = packets[0]
    packets = packets[1:]
    versions = []

    if length_type_id == '0':
        total_length = int(packets[:15], 2)
        packets = packets[15:]

        subpackets = packets[:total_length]
        packets = packets[total_length:]

        while subpackets:
            subpackets, subversions = parse_packet(subpackets)
            versions += subversions
    else:
        n_subpackets = int(packets[:11], 2)
        packets = packets[11:]

        for _ in range(n_subpackets):
            packets, subversions = parse_packet(packets)
            versions += subversions

    return packets, versions


def main():
    with open("y2021/input/d16.txt") as file:
        data = file.read()

    packets = parse_data(data)
    _, versions = parse_packet(packets)

    print(f"Part 1: {sum(versions)}")


if __name__ == "__main__":
    main()
