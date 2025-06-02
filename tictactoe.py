def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("🎮 Welcome to Tic-Tac-Toe!")
    print("Players take turns to place X and O.")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        except ValueError:
            print("❌ Invalid input. Please enter numbers between 0 and 2.")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)

            if check_win(board, current_player):
                print(f"🏆 Player {current_player} wins!")
                break
            elif is_full(board):
                print("🤝 It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("❌ Invalid move. Try again.")

tic_tac_toe()
