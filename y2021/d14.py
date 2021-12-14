from collections import Counter


def parse_data(data):
    polymer = data[0]
    rules = dict()
    for line in data[1].splitlines():
        pair, insert = line.split(" -> ")
        rules[pair] = insert + pair[1]

    return polymer, rules


def apply_rules(pair, rules):
    if pair in rules:
        return rules[pair]
    return pair[1]


def main():
    with open("y2021/input/d14.txt") as file:
        data = file.read().split("\n\n")

    polymer, rules = parse_data(data)
    for _ in range(10):
        pairs = [polymer[i:i+2] for i in range(len(polymer) - 1)]
        polymer = polymer[0] + ''.join(apply_rules(p, rules) for p in pairs)

    element_counts = Counter(polymer).values()
    element_diff = max(element_counts) - min(element_counts)
    print(f"Part 1: {element_diff}")


if __name__ == "__main__":
    main()
