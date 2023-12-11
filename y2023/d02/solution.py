from dataclasses import dataclass, field


@dataclass
class Game:
    id: int
    sets: list[dict[str, int]]

    def is_possible(self, cubes) -> bool:
        for set in self.sets:
            for color, n_cubes in cubes.items():
                if color in set and not set[color] <= n_cubes:
                    return False

        return True


class Solver:
    CUBES = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    @staticmethod
    def read_input(path: str) -> list[Game]:
        with open(path, "r") as f:
            lines = f.read().splitlines()

        games = []
        for line in lines:
            id_string, sets_string = line.split(":")
            id = int(id_string.split()[-1])
            sets = []

            for set_string in sets_string.split(";"):
                set = dict()

                for cube_string in set_string.split(","):
                    n_cubes, color = cube_string.split()
                    set[color] = int(n_cubes)

                sets.append((set))

            game = Game(id, sets)
            games.append(game)

        return games

    def solve(self, path: str) -> None:
        games = self.read_input(path)
        games_possible = [game.id for game in games if game.is_possible(self.CUBES)]
        print(f"Part 1: {sum(games_possible)}")


if __name__ == "__main__":
    solver = Solver()
    solver.solve("y2023/d02/input.txt")
