from itertools import product

FILEPATH = "y2024/input/input_d07.txt"


def calibrate(equations: list[int], operators: str) -> int:
    calibration_result = 0
    for result, *terms in equations:
        operator_combos = [list(p) for p in product(operators, repeat=len(terms) - 1)]
        if any(is_possible(result, terms, combo) for combo in operator_combos):
            calibration_result += result

    return calibration_result


def is_possible(result: int, terms: list[int], operators: list[str]) -> bool:
    value = terms[0]
    for operator, term in zip(operators, terms[1:]):
        value = eval(str(value) + operator + str(term))

    return value == result


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        equations = [
            map(int, equation.replace(":", " ").split())
            for equation in f.read().splitlines()
        ]

    calibration_result = calibrate(equations, "+*")
    print(f"Part 1: {calibration_result}")
