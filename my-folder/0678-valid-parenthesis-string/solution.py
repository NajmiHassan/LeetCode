class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0
        for char in s:
            if char == "(":
                left_min, left_max = left_min + 1, left_max +1
            elif char == ")":
                left_min, left_max = left_min - 1, left_max -1
            else:
                left_min, left_max = left_min - 1, left_max + 1
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        return left_min == 0

        # left_balance = right_balance = 0
        # for i in range(len(s)):
        #     # If we encounter a left parenthesis or a '*', it could potentially be a left parenthesis
        #     left_balance += 1 if s[i] in "(*" else -1
        #     # If we encounter a right parenthesis or a '*', it could potentially be a right parenthesis
        #     right_balance += 1 if s[len(s) - 1 - i] in ")*" else -1
        #     # If at any point the balance goes negative, we have more right parentheses than left
        #     if left_balance < 0 or right_balance < 0:
        #         return False
        # # If we can complete the loop without the balance going negative, the string is valid
        # return True


        # return (f:=lambda s,b:min(accumulate(1-2*(c==b) for c in s)))(s,')')>=0<=f(s[::-1],'(')
