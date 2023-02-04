from random import randint

import matplotlib.pyplot as plt

import numpy as np


class Solution:

    '''
    Given an mxn chessboard, if the position (x,y) of the knight is given, find the path which covers all the blocks of the chessboard without repeating.
    '''

    def knightTour(self, N):

        def isSafe(x, y):

            # Check cell (x, y) is not available and value is not visited already
            if 0 <= x < N and 0 <= y < N and board[x][y] == -1:
                return True
            return False

        def backtrack(cur_x, cur_y, moveCount):

            # Base case: If all moves are done
            if moveCount >= N*N:
                return True

            # Consider all possible moves
            for i in range(8):
                next_x = cur_x + move_x[i]
                next_y = cur_y + move_y[i]

                # Check if this move can be taken
                if isSafe(next_x, next_y):
                    # Take this move
                    board[next_x][next_y] = moveCount

                    # Check if this move leads to a solution
                    if backtrack(next_x, next_y, moveCount+1):
                        return True

                    # This move didn't work, then backtrack
                    board[next_x][next_y] = -1

            return False  # No move from all 8 possible worked, so backtrack previous move and retry

        # Initialize NxN chess board
        board = [[-1 for i in range(N)] for j in range(N)]

        # Possible moves of a knight on chess-board, X and Y coordinates
        move_x = [2, 1, -1, -2, -2, -1, 1, 2]
        move_y = [1, 2, 2, 1, -1, -2, -2, -1]

        # Start with the Knight is initially at the first block
        board[0][0] = 0
        backtrack(0, 0, 1)  # Step counter for knight's position
        return board

    def graph(self, solution):

        # Graph knight's tour given a solution
        N = len(solution[0])
        # Convert the board into a single list
        flat_solution = [item for sublist in solution for item in sublist]

        # Display the board
        board = np.zeros((N, N))
        board[1::2, 0::2] = 1
        board[0::2, 1::2] = 1
        plt.imshow(board, cmap='binary')

        positions = {}
        coordinates = []
        # Create all coordinates
        for i in range(0, N):
            for j in range(0, N):
                coordinates.append([j, i])

        # Store all coordinates in a single dictionary
        index = 0
        for coord in coordinates:
            positions[index] = coord
            index += 1

        # Display the solution indices
        for i in range(N*N):
            plt.text(positions[i][0], positions[i][1], flat_solution[i], fontsize=15, color="blue",
                     horizontalalignment='center', verticalalignment='center')

        plt.show()
