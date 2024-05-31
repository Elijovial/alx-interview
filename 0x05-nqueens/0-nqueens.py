#!/usr/bin/python3
"""
The N queens puzzle
"""
import sys


def print_solutions(solutions, n):
    """Prints out the solutions in the required format."""
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


def is_safe(board, row, col, n):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens(board, row, n, solutions):
    """Uses backtracking to find all solutions."""
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(board, row + 1, n, solutions)
            board[row] = -1


def nqueens(n):
    """Main function to solve the N Queens problem."""
    board = [-1] * n
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    print_solutions(solutions, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(n)
