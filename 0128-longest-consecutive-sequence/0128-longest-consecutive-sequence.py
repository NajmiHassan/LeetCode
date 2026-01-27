class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums is None:
            return 0

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                currentNum = num
                currentStreak = 1
                
                while (currentNum + 1) in numSet:
                    currentNum += 1
                    currentStreak += 1

                longest = max(longest, currentStreak)
        
        return longest

