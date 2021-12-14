from collections import Counter


def parse_data(data):
    polymer, _, *rules = data.splitlines()
    polymer_pairs = Counter(map(''.join, zip(polymer, polymer[1:])))
    elements = Counter(polymer)
    rules = dict(rule.split(" -> ") for rule in rules)
    return polymer_pairs, elements, rules


def step(polymer_pairs, elements, rules):
    polymer_pairs_out = polymer_pairs.copy()
    for pair, n in polymer_pairs.items():
        if pair in rules:
            polymer_pairs_out[pair] -= n
            polymer_pairs_out[pair[0] + rules[pair]] += n
            polymer_pairs_out[rules[pair] + pair[1]] += n
            elements[rules[pair]] += n

    return polymer_pairs_out, elements


def element_diff_max(elements):
    return max(elements.values()) - min(elements.values())


def main():
    with open("y2021/input/d14.txt") as file:
        data = file.read()

    polymer_pairs, elements, rules = parse_data(data)
    for i in range(40):
        polymer_pairs, elements = step(polymer_pairs, elements, rules)

        if i == 9:
            element_diff_10 = element_diff_max(elements)

    element_diff_40 = element_diff_max(elements)

    print(f"Part 1: {element_diff_10}")
    print(f"Part 2: {element_diff_40}")


if __name__ == "__main__":
    main()
