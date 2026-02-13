class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0 

        if n > 0:
            current_run = 0
            for i in range(n):
                if i > 0 and s[i] == s[i-1]:
                    current_run += 1
                else:
                    current_run =  1
                max_len = max(max_len, current_run)

        pairs = [('a', 'b', 'c'), ('b', 'c', 'a'), ('a', 'c', 'b')]

        for char1, char2, forbidden in pairs:
            diff_map = {0: -1}
            balance = 0

            for i, char in enumerate(s):
                if char == forbidden:
                    balance = 0
                    diff_map = {0: i}
                else:
                    if char == char1:
                        balance += 1
                    elif char == char2:
                        balance -= 1
                    
                    if balance in diff_map:
                        current_len = i - diff_map[balance]
                        max_len = max(max_len, current_len)
                    else:
                        diff_map[balance] = i
        
        state_map = {(0,0): -1}
        ca = cb = cc = 0

        for i, char in enumerate(s):
            if char == 'a': ca += 1
            elif char == 'b': cb += 1
            elif char == 'c': cc += 1

            state = (ca - cb, cb - cc)

            if state in state_map:
                current_len = i - state_map[state]
                max_len = max(max_len, current_len)
            else:
                state_map[state] = i
    
        return max_len
        
