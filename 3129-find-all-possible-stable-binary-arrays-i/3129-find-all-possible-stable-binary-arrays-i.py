class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        z, o, l = zero, one, limit
        
        MOD = 10**9 + 7

        dp = [[[0,0] for _ in range(o + 1)] for _ in range(z + 1)]

        for i in range(1, min(z, l) + 1):
            dp[i][0][0] = 1

        for j in range(1, min(o, l) + 1):
            dp[0][j][1] = 1
        
        for i in range(1, z + 1):
            for j in range(1, o + 1):
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD

                if i > l:
                    dp[i][j][0] = (dp[i][j][0] - dp[i  - 1 - l][j][1]) % MOD
                
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD

                if j > l:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - 1 - l][0]) % MOD
    
        return (dp[z][o][0] + dp[z][o][1]) % MOD