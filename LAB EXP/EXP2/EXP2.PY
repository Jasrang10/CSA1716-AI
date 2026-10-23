
def solve(board, row):
    if row == 8:
        for r in board:
            print(" ".join("Q" if x else "." for x in r))
        return True

    for col in range(8):
        safe = True

        for r in range(row):
            if (board[r][col] or
                (row - r == abs(col - board[r].index(1))
                 if 1 in board[r] else False)):
                safe = False
                break

        if safe:
            board[row][col] = 1
            if solve(board, row + 1):
                return True
            board[row][col] = 0

    return False

board = [[0] * 8 for _ in range(8)]
solve(board, 0)
