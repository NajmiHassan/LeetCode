class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0

        current_inc1 = -math.inf
        current_dec = -math.inf
        current_inc2 = -math.inf

        global_max = -math.inf

        for i in range(1,n):
            curr = nums[i]
            prev = nums[i-1]

            new_inc1 = -math.inf
            new_dec = -math.inf
            new_inc2 = -math.inf

            if curr > prev:
                new_inc1 = max(current_inc1 + curr, prev +curr)
            
                if current_dec != -math.inf:
                    new_inc2 = max(current_inc2 + curr, current_dec +curr)
                elif current_inc2 != -math.inf:
                    new_inc2 = current_inc2 + curr
            
            elif curr < prev:
                if current_inc1 != -math.inf:
                    new_dec = max(current_dec + curr, current_inc1 + curr)
                elif current_dec != -math.inf:
                    new_dec = current_dec +curr
            
            current_inc1 = new_inc1
            current_dec = new_dec
            current_inc2 = new_inc2

            if current_inc2 != -math.inf:
                global_max = max(global_max, current_inc2)
        
        return global_max

        