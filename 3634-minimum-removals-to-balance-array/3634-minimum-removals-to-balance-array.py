class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)

        left = 0 
        max_valid_window = 0 

        for right in range(n):

            while nums[right] > nums[left] *k:
                left += 1   
            current_window_size = right - left + 1
            if current_window_size > max_valid_window:
                max_valid_window = current_window_size
        
        return n - max_valid_window