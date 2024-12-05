FILEPATH = "y2024/input/input_d02.txt"


def read_input(filepath: str) -> (list, list):
    reports = []

    with open(filepath, "r") as f:
        for line in f:
            reports.append([int(level) for level in line.split()])

    return reports


def is_safe_report(report: list[int]) -> bool:
    differences = [a - b for a, b in zip(report[:-1], report[1:])]

    if all(1 <= d <= 3 for d in differences) or all(-3 <= d <= -1 for d in differences):
        return True

    return False


def is_dampened_safe_report(report: list[int]) -> bool:
    for i in range(len(report)):
        if is_safe_report(report[:i] + report[i + 1 :]):
            return True

    return False


if __name__ == "__main__":
    reports = read_input(FILEPATH)

    n_safe_reports = sum([is_safe_report(r) for r in reports])
    print(f"Part 1: {n_safe_reports}")

    n_dampened_safe_reports = sum([is_dampened_safe_report(r) for r in reports])
    print(f"Part 2: {n_dampened_safe_reports}")
