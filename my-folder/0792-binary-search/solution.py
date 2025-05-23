class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid  # Corrected indentation
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # Return -1 if target not found

