#!/usr/bin/python3
"""
This script, 101-nqueens, finds all possible solutions to the N queens puzzle, including translations and reflections.

It attempts virtual backtracking without recursion. In local tests, the process starts to visibly slow down for N > 8 and is successful up to N = 11. However, it may be killed if used for N > 11. Recursion could allow for a lighter-weight process, but it's not yet apparent to this student how to retain a record of which solutions are already derived with that method.

Attributes:
    N (int): Base number of queens and length of the board side in piece positions.
    candidates (list of lists of lists of int): List of all successful solutions for a given number of columns checked.
"""

from sys import argv

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)

def board_column_gen(board=[]):
    """
    Adds a column of zeroes to the right of any board about to be tested for queen arrangements in that column.

    Args:
        board (list of lists of int): 2D list of ints, only as wide as needed to test the rightmost column for queen conflicts.

    Returns:
        modified 2D list
    """
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board

def add_queen(board, row, col):
    """
    Sets "queen," or 1, to coordinates given in board.

    Args:
        board (list of lists of int): 2D list of ints, only as wide as needed to test the rightmost column for queen conflicts.
        row (int): First dimension index.
        col (int): Second dimension index.
    """
    board[row][col] = 1

def new_queen_safe(board, row, col):
    """
    For the given board, checks that for a new queen placed in the rightmost column, there are no other "queens," or 1 values, to the left and diagonally up-left and down-left.

    Args:
        board (list of lists of int): 2D list of ints, only as wide as needed to test the rightmost column for queen conflicts.
        row (int): First dimension index.
        col (int): Second dimension index.

    Returns:
        True if no left-side conflicts found for new queen, or False if a conflict is found.
    """
    x = row
    y = col

    for i in range(1, N):
        if (y - i) >= 0:
            # Check up-left diagonal
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            # Check left
            if board[x][y - i]:
                return False
            # Check down-left diagonal
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True

def coordinate_format(candidates):
    """
    Converts a board (matrix of 1 and 0) into a series of row/column indices of each queen/1.

    Args:
        candidates (list of lists of lists of int): List of all successful solutions for the amount of columns last checked.

    Returns:
        holberton, the list of coordinates.
    """
    holberton = []
    for x, attempt in enumerate(candidates):
        holberton.append([])
        for i, row in enumerate(attempt):
            holberton[x].append([])
            for j, col in enumerate(row):
                if col:
                    holberton[x][i].append(i)
                    holberton[x][i].append(j)
    return holberton

# Initialize candidates list with the first column of 0s
candidates = []
candidates.append(board_column_gen())

# Proceed column by column, testing the rightmost
for col in range(N):
    # Start a new generation of the candidate list for every round of testing
    new_candidates = []
    # Test each candidate from the previous round, at the current column
    for matrix in candidates:
        # For every row in that candidate's rightmost column
        for row in range(N):
            # Are there any conflicts in placing a queen at those coordinates?
            if new_queen_safe(matrix, row, col):
                # No? Then create a "child" (copy) of that candidate
                temp = [line[:] for line in matrix]
                # Place a queen in that position
                add_queen(temp, row, col)
                # And unless you're in the last round of testing,
                if col < N - 1:
                    # Add a new column of 0s on the right for the next round
                    board_column_gen(temp)
                # Add that new candidate to this round's list of successes
                new_candidates.append(temp)
    # When finished with the round, discard the "parent" candidates
    candidates = new_candidates

# Format results to match assignment output
for item in coordinate_format(candidates):
    print(item)

