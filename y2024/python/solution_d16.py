import heapq

FILEPATH = "y2024/input/input_d16.txt"


def get_neighbours(
    maze: dict[tuple[int, int], str], node: tuple[int, int]
) -> set[tuple[int, int]]:
    x, y = node
    directions = {(0, -1), (1, 0), (0, 1), (-1, 0)}
    neighbours = {(x + dx, y + dy) for dx, dy in directions}
    return {n for n in neighbours if maze[n] != "#"}


if __name__ == "__main__":
    with open(FILEPATH, "r") as f:
        maze = {
            (x, y): c
            for y, row in enumerate(f.read().splitlines())
            for x, c in enumerate(row)
        }

    graph = {node: get_neighbours(maze, node) for node, c in maze.items() if c != "#"}
    n_start = list(maze.keys())[list(maze.values()).index("S")]
    n_target = list(maze.keys())[list(maze.values()).index("E")]

    visited = {n_start: 0}
    queue = [(0, n_start, (1, 0))]
    while queue:
        cost, (x, y), direction = heapq.heappop(queue)
        for x_n, y_n in graph[(x, y)]:
            dx, dy = x_n - x, y_n - y
            turn = direction != (dx, dy)
            option_cost = cost + 1 + turn * 1000

            if option_cost < visited.get((x_n, y_n), float("inf")):
                visited[(x_n, y_n)] = option_cost
                heapq.heappush(queue, (option_cost, (x_n, y_n), (dx, dy)))

    print(f"Part 1: {visited[n_target]}")
