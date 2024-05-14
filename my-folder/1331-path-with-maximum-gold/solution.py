class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def backtrack(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            gold = grid[i][j]
            grid[i][j] = 0  # Mark as visited
            max_gold = 0

            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                max_gold = max(max_gold, backtrack(new_i, new_j))

            grid[i][j] = gold  # Backtrack
            return max_gold + gold

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_gold = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, backtrack(i, j))

        return max_gold
