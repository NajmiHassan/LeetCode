class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            distinct_evens = set()
            distinct_odds = set()

            for j in range(i, n):
                num = nums[j]

                if num % 2 == 0:
                    distinct_evens.add(num)
                else:
                    distinct_odds.add(num)
                
                if len(distinct_evens) == len(distinct_odds):
                    current_len = j - i + 1
                    if current_len > max_len:
                        max_len = current_len

        return max_len

                