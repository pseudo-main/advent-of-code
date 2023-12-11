class Solver:
    @staticmethod
    def read_input(path: str) -> list[str]:
        with open(path, "r") as f:
            return f.read().splitlines()

    @staticmethod
    def filter_digits(string: str) -> list[int]:
        return [int(c) for c in string if c.isdigit()]

    def extract_calibration_value(self, string: str) -> int:
        digits = self.filter_digits(string)
        return int(str(digits[0]) + str(digits[-1]))

    def solve(self, path: str) -> None:
        lines = self.read_input(path)
        calibration_values = [self.extract_calibration_value(line) for line in lines]
        print(f"Part 1: {sum(calibration_values)}")


if __name__ == "__main__":
    solver = Solver()
    solver.solve("y2023/d01/input.txt")
