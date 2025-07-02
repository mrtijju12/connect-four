ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = [[" " for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
    return board

def print_board(board):
    print("\n")
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("  " + "   ".join([str(i) for i in range(COLUMN_COUNT)]))
    print("\n")

def is_valid_location(board, col):
    return board[0][col] == " "

def get_next_open_row(board, col):
    for r in range(ROW_COUNT-1, -1, -1):
        if board[r][col] == " ":
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if (board[r][c] == piece and
                board[r][c+1] == piece and
                board[r][c+2] == piece and
                board[r][c+3] == piece):
                return True

    # Check vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if (board[r][c] == piece and
                board[r+1][c] == piece and
                board[r+2][c] == piece and
                board[r+3][c] == piece):
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if (board[r][c] == piece and
                board[r+1][c+1] == piece and
                board[r+2][c+2] == piece and
                board[r+3][c+3] == piece):
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if (board[r][c] == piece and
                board[r-1][c+1] == piece and
                board[r-2][c+2] == piece and
                board[r-3][c+3] == piece):
                return True

def is_board_full(board):
    for c in range(COLUMN_COUNT):
        if is_valid_location(board, c):
            return False
    return True

def main():
    board = create_board()
    game_over = False
    turn = 0

    print("Welcome to Connect Four!")
    print_board(board)

    while not game_over:
        # Ask for Player Input
        if turn == 0:
            piece = "X"
            col = input("Player 1 (X), choose a column (0-6): ")
        else:
            piece = "O"
            col = input("Player 2 (O), choose a column (0-6): ")

        # Validate input
        if not col.isdigit() or not (0 <= int(col) < COLUMN_COUNT):
            print("Invalid column. Please enter a number between 0 and 6.")
            continue

        col = int(col)

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, piece)

            print_board(board)

            if winning_move(board, piece):
                print(f"Player {turn + 1} ({piece}) WINS!")
                game_over = True
            elif is_board_full(board):
                print("It's a tie!")
                game_over = True
            else:
                turn = (turn + 1) % 2
        else:
            print("Column is full. Choose another one.")

if __name__ == "__main__":
    main()
