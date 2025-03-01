class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range (n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        result = [0] * n
        position = 0

        for i in range (n):
            if nums[i] != 0:
                result[position] = nums[i]
                position = position + 1

        return result
