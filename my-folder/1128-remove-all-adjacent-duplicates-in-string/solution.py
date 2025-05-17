class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []

        for c in s:
            if stk and stk[-1] == c:
                stk.pop()
                continue 
            stk.append(c)

        return "".join(stk)
