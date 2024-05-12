class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = []

        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                # Extract the 3x3 submatrix
                submatrix = [grid[i + k][j:j + 3] for k in range(3)]
                # Find the maximum value in the submatrix
                max_value = max(max(row) for row in submatrix)
                row.append(max_value)
            result.append(row)

        return result  
