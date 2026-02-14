class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * 102 for _ in range(102)]
        
        tower[0][0] = float(poured)
        
        for r in range(query_row + 1):
            for c in range(r + 1):
                
                if tower[r][c] > 1:
                    excess = (tower[r][c] - 1) / 2.0
                    tower[r + 1][c] += excess
                    tower[r + 1][c + 1] += excess
                    tower[r][c] = 1.0 
        
        return tower[query_row][query_glass]
        
        
        
        # tower = [[0.0 * 102 for _ in range(102)]]

        # tower[0][0] = float(poured)

        # for r in range(query_row + 1):
        #     for c in range(r+1):
        #         if tower[r][c] > 1:
        #             excess = (tower[r][c] - 1) / 2.0
        #             tower[r+1][c] += excess
        #             tower[r+1][c+1] += excess
        #             tower[r][c] = 1.0
        
        # return tower[query_row][query_glass]