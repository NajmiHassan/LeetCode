class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        def can_reduce_in_time(T: int) -> bool:
            total_height_reduced = 0
            
            for w in workerTimes:
                # Using the quadratic formula to find max height 'x' this worker can clear in T seconds:
                # x = (sqrt(1 + 8T/w) - 1) / 2
                
                # math.isqrt computes the integer square root safely without floating point limits
                x = (math.isqrt(1 + 8 * T // w) - 1) // 2
                total_height_reduced += x
                
                # Early exit: if we already reduced enough, return True!
                if total_height_reduced >= mountainHeight:
                    return True
                    
            return False

        # Binary Search Bounds
        low = 1
        
        # Worst-case scenario upper bound: 
        # Assume only the fastest single worker does all the work.
        min_w = min(workerTimes)
        high = min_w * mountainHeight * (mountainHeight + 1) // 2
        
        ans = high
        
        # Execute binary search
        while low <= high:
            mid = (low + high) // 2
            
            if can_reduce_in_time(mid):
                ans = mid       # This time works, record it.
                high = mid - 1  # Let's see if we can do it in LESS time.
            else:
                low = mid + 1   # Time was too short, we need MORE time.
                
        return ans