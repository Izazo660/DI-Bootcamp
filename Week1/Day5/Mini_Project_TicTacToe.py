def display_board(board):
    """Step 2: Display the current state of the game board."""
    print("\nTIC TAC TOE")
    print("*************")
    for i in range(3):
        print(f"* {board[i][0]} | {board[i][1]} | {board[i][2]}  *")
        if i < 2:
            print("* ---|---|--- *")
    print("*************")


def player_input(player, board):
    """Step 3: Get player input, validate it, and update the board."""
    print(f"\nPlayer {player}'s turn...")
    
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid input! Rows and columns must be between 1 and 3.")
                continue
            if board[row][col] != " ":
                print("That square is already taken! Choose another one.")
                continue
            board[row][col] = player
            break            
        except ValueError:
            print("Invalid input! Please enter valid numeric integers.")


def check_win(board, player):
    """Step 4: Check all possible winning combinations (rows, cols, diagonals)."""
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def check_tie(board):
    """Step 5: Check if the board is completely full without any winner."""
    for row in board:
        if " " in row:
            return False
    return True


def play():
    """Step 6: The Main Game Loop to coordinate execution flow."""
    print("Welcome to TIC TAC TOE!")
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    current_player = "X"
    while True:
        display_board(board)
        player_input(current_player, board)
        if check_win(board, current_player):
            display_board(board)
            print(f"\n Congratulations ! Player {current_player} wins ! ")
            break
        if check_tie(board):
            display_board(board)
            print("\n It's a tie game ! Good match !")
            break
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play()