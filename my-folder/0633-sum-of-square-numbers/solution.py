class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))

        while left <= right:
            total = left*left + right*right
            if total > c:
                right -= 1
            elif total < c:
                left += 1
            else:
                return True
        return False
        
        
        # squareroot = set()

        # for i in range(int(sqrt(c)) + 1):
        #     squareroot.add(i * i)
        # a = 0

        # while a*a <= c:
        #     target = c - a*a
        #     if target in squareroot:
        #         return True
        #     a += 1
        # return False
