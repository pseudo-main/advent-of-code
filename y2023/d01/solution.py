class Solver:
    @staticmethod
    def read_input(path: str) -> list[str]:
        with open(path, "r") as f:
            return f.read().splitlines()

    @staticmethod
    def filter_digits(string: str) -> list[int]:
        return [int(c) for c in string if c.isdigit()]

    @staticmethod
    def replace_spelled_digits(string: str) -> str:
        spelled_digits = {
            "one": "one1one",
            "two": "two2two",
            "three": "three3three",
            "four": "four4four",
            "five": "five5five",
            "six": "six6six",
            "seven": "seven7seven",
            "eight": "eight8eight",
            "nine": "nine9nine",
        }

        for spelling, digit in spelled_digits.items():
            string = string.replace(spelling, digit)

        return string

    def extract_calibration_value(self, string: str) -> int:
        digits = self.filter_digits(string)
        if digits:
            return int(str(digits[0]) + str(digits[-1]))
        else:
            return 0

    def solve(self, path: str) -> None:
        lines = self.read_input(path)
        calibration_values = [self.extract_calibration_value(line) for line in lines]
        print(f"Part 1: {sum(calibration_values)}")

        lines_digitized = [self.replace_spelled_digits(line) for line in lines]
        calibration_values_correct = [
            self.extract_calibration_value(line) for line in lines_digitized
        ]
        print(f"Part 2: {sum(calibration_values_correct)}")


if __name__ == "__main__":
    solver = Solver()
    solver.solve("y2023/d01/input.txt")
