from collections import defaultdict

FILEPATH = "y2024/input/input_d05.txt"


def is_in_correct_order(pages: list[int], rules: dict[int : set[int]]) -> bool:
    return not any(rules[p].intersection(pages[:i]) for i, p in enumerate(pages))


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        part_a, part_b = (part.split("\n") for part in f.read().strip().split("\n\n"))

    rules = defaultdict(set)
    for rule in part_a:
        x, y = map(int, rule.split("|"))
        rules[x].add(y)

    updates = [list(map(int, update.split(","))) for update in part_b]
    correct_updates = [pages for pages in updates if is_in_correct_order(pages, rules)]
    total = sum(update[(len(update) - 1) // 2] for update in correct_updates)
    print(f"Part 1: {total}")
