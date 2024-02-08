#!/usr/bin/python3
"""Module with solution for the N-Queens challenge with backtracking"""
import sys


def chessboard(pos, n):
    """Function to print chessboard with appropriate positions of queens"""

    board = []

    for RANK in range(n):
        for FILE in range(n):
            if FILE == pos[RANK]:
                board.append([RANK, FILE])

    print(board)


def safe_pos(pos, RANK, FILE, n):
    """Function to determine safe a square to place a queen"""

    if (pos[RANK] == FILE) or (pos[RANK] == FILE - RANK + n) or \
            (pos[RANK] == RANK - n + FILE):
        return True
    return False


def get_safe_pos(board, rank, n):
    """Function to get all safe positions to place queens with recursion"""

    if rank == n:
        chessboard(board, n)
    else:
        for FILE in range(n):
            safe = True

            for RANK in range(rank):
                if safe_pos(board, RANK, FILE, rank):
                    safe = False

            if safe:
                board[rank] = FILE
                get_safe_pos(board, rank + 1, n)


def create_board(n):
    """Function to generate chessboard of n-size"""

    return [0 * n for i in range(n)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)


board = create_board(int(n))
rank = 0
get_safe_pos(board, rank, int(n))
#!/usr/bin/python3
""" A program that solves the N queens problem """

from sys import argv


def check_row(board, row, n):
    """ Check if there is a queen in the row """
    for col in range(n):
        if board[row][col]:
            return False
    return True


def check_diagonals(board, row, col, n):
    """ Check if there is a queen in the diagonals """
    for i in range(n):
        if (board[i][col] or
                board[row][i] or
                (0 <= row + i < n and 0 <= col + i < n and board[row + i][col + i]) or
                (0 <= row - i < n and 0 <= col + i < n and board[row - i][col + i])):
            return False
    return True


def solve_n_queens(n):
    """ Solve the N Queens problem """
    if n < 4:
        print("N must be at least 4")
        return []

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([col for col, val in enumerate(board[row - 1]) if val])
            return

        for col in range(n):
            if check_row(board, row, n) and check_diagonals(board, row, col, n):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)
    return solutions


def main():
    """ The Main Function """
    argc = len(argv)
    if argc != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
