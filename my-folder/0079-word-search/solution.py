class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # def backtrack(r,c,i):
        #     if i==ln: return True
        #     for dr,dc in ((r+1,c),(r,c+1),(r-1,c),(r,c-1)):
        #         tmp,board[r][c] = board[r][c],"#"
        #         if 0<=dr<m and 0<=dc<n and board[dr][dc]==word[i]:
        #             if backtrack(dr,dc,i+1): return True
        #         board[r][c] = tmp
            
        # m,n,ln = len(board),len(board[0]),len(word)
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j]==word[0]:
        #             if backtrack(i,j,1): return True
        # return False

        def dfs(i, j, k):
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

