def input_sudoku():
    print("Enter the Sudoku puzzle row by row, using space-separated numbers (0 for empty cells):")
    board = []
    for i in range(9):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != 9:
            print("Each row must have exactly 9 numbers.")
            return None
        board.append(row)
    return board

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False
    for x in range(9):
        if board[x][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    empty_cell = find_empty(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
        

def main():
    print("Input Manually")
    board = input_sudoku()
    if board is None:
        print("Failed to load Sudoku board.")
        return
    
    print("Unsolved Sudoku:")
    print_board(board)
    
    if solve_sudoku(board):
        print("Solved Sudoku:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
