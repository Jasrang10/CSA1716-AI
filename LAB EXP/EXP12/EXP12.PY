
board = [" "] * 9

def display():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-----")

def check():
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

player = "X"

while True:
    display()
    try:
        move = int(input("Player " + player + ", enter position (1-9): ")) - 1
    except ValueError:
        print("Enter a number from 1 to 9.")
        continue

    if move not in range(9) or board[move] != " ":
        print("Invalid move! Try again.")
        continue

    board[move] = player
    winner = check()

    if winner:
        display()
        print(winner, "wins!")
        break

    if " " not in board:
        display()
        print("It's a draw!")
        break

    player = "O" if player == "X" else "X"
