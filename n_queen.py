def print_solution(board):
    for row in board:
        print(" ".join(row))
    print()
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False
    return True
def solve_n_queens_util(board, row, n):
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_n_queens_util(board, row + 1, n)
            board[row][col] = '.'  
def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve_n_queens_util(board, 0, n)
    
if __name__ == "__main__":
    try:
        n = int(input("Enter the number of queens (N): "))
        if n <= 0:
            raise ValueError("N must be a positive integer.")
        solve_n_queens(n)
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid positive integer for N.")
