#!/usr/bin/python3
"""program that solves the N queens problem."""

import sys


def print_usage_and_exit():
    """Print usage message and exit with status 1"""
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(message):
    """Print error message and exit with status 1"""
    print(message)
    sys.exit(1)


def is_valid_position(board, row, col):
    """Check if a queen can be placed at board[row][col]"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """Solve the N queens puzzle and print all solutions"""
    def solve(row):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid_position(board, row, col):
                board[row] = col
                solve(row + 1)

    solutions = []
    board = [-1] * N
    solve(0)

    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(N)]
        print(formatted_solution)


def main():
    """function handles command-line arguments"""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")

    if N < 4:
        print_error_and_exit("N must be at least 4")

    solve_nqueens(N)


if __name__ == "__main__":
    main()
