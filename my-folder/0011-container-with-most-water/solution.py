class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            area = (right - left) * min(height [left], height[right])
            res = max(res,area)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1 
            else:
                right -= 1

        return res

