class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countLessEqual(x):
            count, n = 0, len(matrix)
            row, col = n-1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    count += row +1
                    col += 1
                else:
                    row -= 1
            return count

        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]

        while left < right:
            mid = (left + right) // 2
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
