import numpy as np
import matplotlib.pyplot as plt


class Solution:
    """
    Given an NxN chessboard, this algorithm finds a knight's tour starting from (0,0).
    It prioritizes squares with the least onward moves (Warnsdorff's Rule).
    """

    def knightTour(self, N):
        def isSafe(x, y):
            return 0 <= x < N and 0 <= y < N and board[x, y] == -1

        def get_degree(x, y):
            """Count the number of valid moves from (x, y)."""
            count = 0
            for i in range(8):
                nx, ny = x + move_x[i], y + move_y[i]
                if isSafe(nx, ny):
                    count += 1
            return count

        def backtrack(x, y, moveCount):
            if moveCount == N * N:
                return True  # Success!

            # Sort moves based on Warnsdorff's heuristic
            moves = sorted(
                [
                    (x + move_x[i], y + move_y[i])
                    for i in range(8)
                    if isSafe(x + move_x[i], y + move_y[i])
                ],
                key=lambda pos: get_degree(pos[0], pos[1]),
            )

            for nx, ny in moves:
                board[nx, ny] = moveCount  # Move knight
                if backtrack(nx, ny, moveCount + 1):  # Recursive call
                    return True
                board[nx, ny] = -1  # Backtrack

            return False  # No valid moves

        # Initialize board using NumPy
        board = np.full((N, N), -1, dtype=int)

        # Possible knight moves
        move_x = [2, 1, -1, -2, -2, -1, 1, 2]
        move_y = [1, 2, 2, 1, -1, -2, -2, -1]

        # Start from (0,0)
        board[0, 0] = 0
        if backtrack(0, 0, 1):
            return board
        else:
            return None  # No solution found

    def graph(self, solution):
        """Visualize the knight’s tour"""
        if solution is None:
            print("No solution found.")
            return

        N = solution.shape[0]
        plt.figure(figsize=(6, 6))
        plt.imshow(np.zeros((N, N)), cmap="gray_r", alpha=0.5)

        # Get (x, y) positions for plotting
        pos = {solution[i, j]: (j, N - 1 - i) for i in range(N) for j in range(N)}
        x_vals, y_vals = zip(*[pos[i] for i in range(N * N)])

        # Draw path
        plt.plot(x_vals, y_vals, "ro-", markersize=8, linewidth=2)

        # Number each step
        for step, (x, y) in pos.items():
            plt.text(
                x, y, str(step), fontsize=10, ha="center", va="center", color="white"
            )

        plt.xticks(range(N))
        plt.yticks(range(N))
        plt.grid(True)
        plt.show()


# Example Usage
N = 8
solver = Solution()
solution = solver.knightTour(N)
solver.graph(solution)
