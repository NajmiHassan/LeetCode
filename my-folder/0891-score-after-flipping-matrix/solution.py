class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Toggle rows to ensure the leftmost digit is 1
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]

        # Toggle columns if necessary to maximize the score
        for j in range(1, n):
            count_ones = sum(grid[i][j] for i in range(m))
            if count_ones < m / 2:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]

        # Calculate the final score
        score = 0
        for i in range(m):
            score += int("".join(map(str, grid[i])), 2)
        return score
