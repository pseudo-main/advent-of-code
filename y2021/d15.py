from collections import defaultdict
import heapq


def parse_data(data):
    lines = data.splitlines()
    return {
        (x, y): int(n) for x, l in enumerate(lines) for y, n in enumerate(l)}


def neighbours(risk_levels, c):
    cs_adj = [(c[0]-1, c[1]), (c[0]+1, c[1]), (c[0], c[1]-1), (c[0], c[1]+1)]
    return [c for c in cs_adj if c in risk_levels]


def dijkstra(risk_levels):
    coordinates = risk_levels.keys()
    source = min(coordinates)
    target = max(coordinates)

    queue = [(0, source)]
    path_safest = defaultdict(lambda: float('inf'), {source: 0})
    path = set()

    while queue:
        risk, current = heapq.heappop(queue)

        if current == target:
            return risk

        path.add(current)

        for neighbour in neighbours(risk_levels, current):
            risk_new = risk + risk_levels[neighbour]
            if risk_new < path_safest[neighbour]:
                path_safest[neighbour] = risk_new
                heapq.heappush(queue, (risk_new, neighbour))


def main():
    with open("y2021/input/d15.txt") as file:
        data = file.read()

    risk_levels = parse_data(data)
    risk_min = dijkstra(risk_levels)

    print(f"Part 1: {risk_min}")


if __name__ == "__main__":
    main()
