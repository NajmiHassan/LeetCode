class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp = n ^ (n >> 1)

        return (temp & (temp + 1)) == 0

