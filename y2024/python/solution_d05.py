from collections import defaultdict
from functools import cmp_to_key

FILEPATH = "y2024/input/input_d05.txt"


def is_correct_order(pages: list[int], rules: dict[int : set[int]]) -> bool:
    return not any(rules[p].intersection(pages[:i]) for i, p in enumerate(pages))


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        part_a, part_b = f.read().strip().split("\n\n")

    rules = defaultdict(set)
    for rule in part_a.split():
        x, y = map(int, rule.split("|"))
        rules[x].add(y)

    updates = [list(map(int, update.split(","))) for update in part_b.split()]
    correct_updates = [pages for pages in updates if is_correct_order(pages, rules)]
    total = sum(update[(len(update) - 1) // 2] for update in correct_updates)
    print(f"Part 1: {total}")

    wrong_updates = [pages for pages in updates if not is_correct_order(pages, rules)]
    fixed_updates = [
        sorted(pages, key=cmp_to_key(lambda x, y: -1 + 2 * (y in rules[x])))
        for pages in wrong_updates
    ]
    total_fixed = sum(update[(len(update) - 1) // 2] for update in fixed_updates)
    print(f"Part 2: {total_fixed}")
