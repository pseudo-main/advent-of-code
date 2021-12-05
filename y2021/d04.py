def parse_data(data):
    draws = [int(n) for n in data[0].split(',')]
    boards_data = [b.split("\n") for b in data[1:]]

    boards = []
    for board_data in boards_data:
        board = [[int(n) for n in row.split()] for row in board_data]
        boards.append(board)

    return draws, boards


def is_winning_board(draws, board):
    win_r = any(all(n in draws for n in r) for r in board)
    win_c = any(all(r[i] in draws for r in board) for i in range(len(board)))
    return win_r or win_c


def main():
    with open("y2021/input/d04.txt") as file:
        data = file.read().strip().split("\n\n")

    draws, boards = parse_data(data)

    ns_drawn = set()
    score = 0
    winner = False
    for n in draws:
        ns_drawn.add(n)
        for board in boards:
            if is_winning_board(ns_drawn, board):
                ns_board = set(n for r in board for n in r)
                ns_not_drawn = ns_board - ns_drawn
                score = sum(ns_not_drawn) * n
                winner = True

        if winner:
            break

    print(f"Part 1: {score}")


if __name__ == "__main__":
    main()
