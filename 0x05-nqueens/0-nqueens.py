#!/usr/bin/python3
""" Python script that solves the N queens puzzle challenge"""

import sys


def is_safe(board, row, col):
    """Check if there is a queen in the same column
    """
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen on the upper diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    # Check if there is a queen on the lower diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False

    return True


def nqueens_util(board, row, n, solutions):
    """method for iterating """
    if row == n:
        solutions.append([[i, col] for i, col in enumerate(board)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            nqueens_util(board, row + 1, n, solutions)
            board[row] = -1


def nqueens(n):
    """Method for determining number of iteration"""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    nqueens_util(board, 0, n, solutions)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
