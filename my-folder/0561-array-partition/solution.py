class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max = 0
        for i in range(0, len(nums), 2):
            max += (nums[i])
        return max
