class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Sliding Window Solution
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True
            
            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])

        return False

        

        
        # Hash Map Solution
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i

        return False
