class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen_zero = False

        for ch in s:
            if ch == '0':
                seen_zero = True
            elif ch == '1' and seen_zero:
                return False

        return True