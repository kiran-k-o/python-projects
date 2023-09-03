def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_idx = 0

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        player = players[player_idx]
        move = input(f"Player {player}, enter your move (row[1-3] and column[1-3] separated by space): ")

        try:
            row, col = map(int, move.split())
            if row < 1 or row > 3 or col < 1 or col > 3:
                raise ValueError()

            if board[row - 1][col - 1] != " ":
                print("That cell is already occupied. Try again.")
                continue

            board[row - 1][col - 1] = player

            if check_winner(board, player):
                print_board(board)
                print(f"Congratulations! Player {player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw! The game is over.")
                break

            player_idx = 1 - player_idx  # Switch to the other player for the next turn

        except ValueError:
            print("Invalid input. Please enter row and column numbers (1-3) separated by space.")

if __name__ == "__main__":
    tic_tac_toe()
