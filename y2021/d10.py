import re


def trim_line(line):
    pairs = ['()', '[]', '{}', '<>']
    replace = [re.escape(p) for p in pairs]
    pattern = re.compile('|'.join(replace))

    while line:
        line_r = pattern.sub('', line)
        if line == line_r:
            break

        line = line_r

    return line


def error_score(line):
    error_score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    search = [re.escape(c) for c in error_score_map.keys()]
    pattern = re.compile('|'.join(search))

    error_indices = pattern.search(line)

    if error_indices:
        return error_score_map[error_indices.group(0)]
    else:
        return 0


def main():
    with open("y2021/input/d10.txt") as file:
        data = file.read().splitlines()

    lines_trimmed = [trim_line(line) for line in data]
    error_score_tot = sum(error_score(line) for line in lines_trimmed)

    print(f"Part 1: {error_score_tot}")


if __name__ == "__main__":
    main()
