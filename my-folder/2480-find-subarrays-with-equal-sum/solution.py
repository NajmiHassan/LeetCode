class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        hash_set = set()
        for i in range(n - 1):
            total = nums[i] + nums[i + 1]
            if total in hash_set:
                return True
            hash_set.add(total)
        return False
