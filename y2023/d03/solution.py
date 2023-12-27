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


@dataclass
class SchematicNumber:
    coordinates: list[Coordinate]
    value: int

    def is_part_number(self, schematic_symbols: list[SchematicSymbol]) -> bool:
        for symbol in schematic_symbols:
            for adjacent_coordinate in symbol.coordinate.adjacent():
                if adjacent_coordinate in self.coordinates:
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


if __name__ == "__main__":
    solver = Solver()
    solver.solve("y2023/d03/input.txt")
