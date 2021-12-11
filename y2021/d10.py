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


def is_corrupted(line):
    chars_illegal = [')', ']', '}', '>']
    search = [re.escape(c) for c in chars_illegal]
    pattern = re.compile('|'.join(search))
    return pattern.search(line)


def score_error(line):
    score_error_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    search = [re.escape(c) for c in score_error_map.keys()]
    pattern = re.compile('|'.join(search))
    return score_error_map[pattern.search(line).group(0)]


def score_incomp(line):
    score_incomp_map = {'(': 1, '[': 2, '{': 3, '<': 4}
    findall = [re.escape(c) for c in score_incomp_map.keys()]
    pattern = re.compile('|'.join(findall))

    score_incomp = 0
    for match in pattern.findall(line)[::-1]:
        score_incomp = score_incomp * 5 + score_incomp_map[match]

    return score_incomp


def main():
    with open("y2021/input/d10.txt") as file:
        data = file.read().splitlines()

    lines_trim = [trim_line(line) for line in data]
    lines_corrupt = [line for line in lines_trim if is_corrupted(line)]
    score_error_tot = sum(score_error(line) for line in lines_corrupt)

    lines_incomp = [line for line in lines_trim if not is_corrupted(line)]
    scores_incomp = [score_incomp(line) for line in lines_incomp]
    score_incomp_mid = sorted(scores_incomp)[round(len(scores_incomp) / 2)]

    print(f"Part 1: {score_error_tot}")
    print(f"Part 2: {score_incomp_mid}")


if __name__ == "__main__":
    main()
