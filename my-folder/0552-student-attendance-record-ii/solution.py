class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        def checkRecord(n: int) -> int:
            if n == 1:
                return 3  # "P", "L", "A"
        
        # dp[length][num_A][consecutive_L]
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
        
        # Initializing base cases
        dp[1][0][0] = 1  # "P"
        dp[1][0][1] = 1  # "L"
        dp[1][1][0] = 1  # "A"
        
        for i in range(2, n+1):
            # Ending with P
            for j in range(2):
                for k in range(3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD
            
            # Ending with L
            for j in range(2):
                dp[i][j][1] = dp[i-1][j][0] % MOD
                dp[i][j][2] = dp[i-1][j][1] % MOD
            
            # Ending with A
            for k in range(3):
                dp[i][1][0] = (dp[i][1][0] + dp[i-1][0][k]) % MOD
        
        # Summing all valid sequences of length n
        total = 0
        for j in range(2):
            for k in range(3):
                total = (total + dp[n][j][k]) % MOD
        
        return total
        
        
        
        # MOD = 10**9 + 7
        # if n == 1:
        #     return 3
        # dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1) ]
        
        # dp[1][0][0] = 1
        # dp[1][0][1] = 1 
        # dp[1][1][0] = 0

        # for _ in range(2, n+1):
        #     P_new = (P + L + LL) % MOD
        #     L_new = P
        #     LL_new = L
        #     P, L, LL = P_new, L_new, LL_new

        # without_A = (P + L + LL) % MOD

        # total = without_A
        # for i in range(n):
        #     total = (total + (without_A * (P +L+LL)%MOD))% MOD

        # return total

