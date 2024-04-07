class Solution:
    def checkValidString(self, s: str) -> bool:

        left_balance = right_balance = 0
        for i in range(len(s)):
            # If we encounter a left parenthesis or a '*', it could potentially be a left parenthesis
            left_balance += 1 if s[i] in "(*" else -1
            # If we encounter a right parenthesis or a '*', it could potentially be a right parenthesis
            right_balance += 1 if s[len(s) - 1 - i] in ")*" else -1
            # If at any point the balance goes negative, we have more right parentheses than left
            if left_balance < 0 or right_balance < 0:
                return False
        # If we can complete the loop without the balance going negative, the string is valid
        return True
