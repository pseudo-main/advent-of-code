FILEPATH = "y2024/input/input_d02.txt"


def read_input(filepath: str) -> (list, list):
    reports = []

    with open(filepath, "r") as f:
        for line in f:
            reports.append([int(level) for level in line.split()])

    return reports


def is_safe_report(report: list[int]) -> bool:
    differences = [a - b for a, b in zip(report[:-1], report[1:])]
    
    if all(l > 0 for l in differences):
        if max(differences) > 3 or min(differences) < 1:
            return False

        return True

    elif all(l < 0 for l in differences):
        if max(differences) > -1 or min(differences) < -3:
            return False

        return True
    
    return False


if __name__ == "__main__":
    reports = read_input(FILEPATH)

    n_safe_reports = sum(1 for r in reports if is_safe_report(r))
    print(f"Part 1: {n_safe_reports}")

