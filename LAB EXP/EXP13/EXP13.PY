
def minimax(board, is_max):
    if "X" in board and board.count("X") == 3:
        return 1
    if "O" in board and board.count("O") == 3:
        return -1
    if " " not in board:
        return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = "X" if is_max else "O"
            scores.append(minimax(board, not is_max))
            board[i] = " "

    return max(scores) if is_max else min(scores)

board = [" "] * 9
print("Minimax score:", minimax(board, True))
