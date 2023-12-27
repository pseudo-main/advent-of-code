from string import digits
from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int

    def adjacent(self) -> list["Coordinate"]:
        return [
            Coordinate(i, j)
            for i in range(self.x - 1, self.x + 2)
            for j in range(self.y - 1, self.y + 2)
            if (i, j) != (self.x, self.y)
        ]


@dataclass
class SchematicSymbol:
    coordinate: Coordinate
    value: str

    def gear_ratio(self, schematic_part_numbers: list["SchematicNumber"]) -> int:
        if self.value != "*":
            return 0

        gear_part_numbers = []
        for part_number in schematic_part_numbers:
            if any(
                coordinate in self.coordinate.adjacent()
                for coordinate in part_number.coordinates
            ):
                gear_part_numbers.append(part_number)

        if len(gear_part_numbers) == 2:
            return gear_part_numbers[0].value * gear_part_numbers[1].value
        else:
            return 0


@dataclass
class SchematicNumber:
    coordinates: list[Coordinate]
    value: int

    def is_part_number(self, schematic_symbols: list["SchematicSymbol"]) -> bool:
        for symbol in schematic_symbols:
            if any(
                coordinate in self.coordinates
                for coordinate in symbol.coordinate.adjacent()
            ):
                return True

        return False


class Solver:
    @staticmethod
    def read_input(
        path: str,
    ) -> tuple[list[SchematicNumber], list[SchematicSymbol]]:
        with open(path, "r") as f:
            lines = f.read().splitlines()

        numbers = []
        symbols = []
        for i, line in enumerate(lines):
            value_string = ""
            coordinates = []

            for j, character in enumerate(line):
                if character in digits:
                    value_string += character
                    coordinates.append(Coordinate(i, j))
                else:
                    if character != ".":
                        symbols.append(SchematicSymbol(Coordinate(i, j), character))

                    if value_string != "":
                        numbers.append(SchematicNumber(coordinates, int(value_string)))
                        value_string = ""
                        coordinates = []

                if j == len(line) - 1 and value_string != "":
                    numbers.append(SchematicNumber(coordinates, int(value_string)))

        return numbers, symbols

    def solve(self, path: str) -> None:
        numbers, symbols = self.read_input(path)
        part_numbers = [number for number in numbers if number.is_part_number(symbols)]
        print(f"Part 1: {sum(part_number.value for part_number in part_numbers)}")

        gear_ratios = [symbol.gear_ratio(part_numbers) for symbol in symbols]
        print(f"Part 2: {sum(gear_ratios)}")


if __name__ == "__main__":
    solver = Solver()
    solver.solve("y2023/d03/input.txt")
