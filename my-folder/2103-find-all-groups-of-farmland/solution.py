class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        def dfs(row, col):       
            land[row][col] = -1
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc             
                if 0 <= new_row < m and 0 <= new_col < n and land[new_row][new_col] == 1:
                    dfs(new_row, new_col)

        m, n = len(land), len(land[0])
        result = []

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    
                    top_left = [i, j]
                    bottom_right = [i, j]
                    
                    dfs(i, j)
                    
                    while bottom_right[0] + 1 < m and land[bottom_right[0] + 1][j] == -1:
                        bottom_right[0] += 1
                    while bottom_right[1] + 1 < n and land[i][bottom_right[1] + 1] == -1:
                        bottom_right[1] += 1
                    
                    result.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])

        return result

