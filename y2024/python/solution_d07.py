from itertools import product

FILEPATH = "y2024/input/input_d07.txt"


def is_possible(result: int, terms: list[int], operators: list[str]) -> bool:
    value = terms[0]
    for operator, term in zip(operators, terms[1:]):
        value = eval(str(value) + operator + term)

    return value == result


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        equations = {
            int(equation.split(":")[0]): equation.split(":")[1].split()
            for equation in f.read().splitlines()
        }

    calibration_result = 0
    for result, terms in equations.items():
        operator_combos = [list(p) for p in product("+*", repeat=len(terms) - 1)]
        if any(is_possible(result, terms, operators) for operators in operator_combos):
            calibration_result += result

    print(f"Part 1: {calibration_result}")
