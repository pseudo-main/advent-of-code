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

    risk_levels_full = risk_levels.copy()
    w, h = max(risk_levels)

    for (x, y), risk in risk_levels_full.copy().items():
        risk_new = risk
        for i in range(1, 5):
            c_new = (x + i * (w+1), y)
            risk_new = max((risk_new + 1) % 10, 1)
            risk_levels_full[c_new] = risk_new

    for (x, y), risk in risk_levels_full.copy().items():
        risk_new = risk
        for j in range(1, 5):
            c_new = (x, y + j * (h+1))
            risk_new = max((risk_new + 1) % 10, 1)
            risk_levels_full[c_new] = risk_new

    risk_min_full = dijkstra(risk_levels_full)

    print(f"Part 1: {risk_min}")
    print(f"Part 2: {risk_min_full}")


if __name__ == "__main__":
    main()
