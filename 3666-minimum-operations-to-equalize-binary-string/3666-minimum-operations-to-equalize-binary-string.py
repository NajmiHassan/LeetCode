class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        c = s.count('0')

        if c == 0:
            return 0
        
        L = c 
        R = c
        steps = 0 
        visited = set()

        while (L, R) not in visited:
            if L <= 0 <= R and L % 2 == 0:
                return steps
            
            visited.add((L, R))

            if L <= k <= R:
                if (k - L) % 2 == 0:
                    next_L = 0
                else:
                    next_L = 1
            elif k < L:
                next_L = L - k
            else:
                next_L = k - R

            target = n - k
            if L <= target <= R:
                if (target - L) % 2 == 0:
                    next_R = n
                else:
                    next_R = n - 1
            elif target < L:
                next_R = n - (L - target)
            else:
                next_R = n - (target - R)

            L = next_L
            R = next_R
            steps += 1

        return -1
            

