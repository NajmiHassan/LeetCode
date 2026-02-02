import heapq
from collections import defaultdict

class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        K = k - 2
        
        left_heap = []
        right_heap = []
        
        left_sum = 0
        left_count = 0
        
        to_remove = defaultdict(int)
        
        def push_right(val):
            heapq.heappush(right_heap, val)
            
        def push_left(val):
            nonlocal left_sum, left_count
            heapq.heappush(left_heap, -val)
            left_sum += val
            left_count += 1
            
        def pop_left():
            nonlocal left_sum, left_count
            val = -heapq.heappop(left_heap)
            left_sum -= val
            left_count -= 1
            return val

        def pop_right():
            return heapq.heappop(right_heap)

        def clean_heaps():
            while left_heap and to_remove[-left_heap[0]] > 0:
                to_remove[-left_heap[0]] -= 1
                heapq.heappop(left_heap)
            while right_heap and to_remove[right_heap[0]] > 0:
                to_remove[right_heap[0]] -= 1
                heapq.heappop(right_heap)

        def balance():
            clean_heaps()
            
            while left_count > K:
                val = pop_left()
                push_right(val)
                clean_heaps()
            
            while left_count < K and right_heap:
                clean_heaps()
                if right_heap:
                    val = pop_right()
                    push_left(val)
            
            clean_heaps()

        def add_num(val):
            if not left_heap or val < -left_heap[0]:
                push_left(val)
            else:
                push_right(val)
            balance()

        def remove_num(val):
            nonlocal left_sum, left_count
            
            clean_heaps()
            
            if left_heap and val <= -left_heap[0]:
                push_left_val = -left_heap[0]
                left_sum -= val
                left_count -= 1
                to_remove[val] += 1
            else:
                to_remove[val] += 1
            
            balance()

        n = len(nums)
        
        for idx in range(2, min(2 + dist, n)):
            add_num(nums[idx])
            
        min_cost = nums[0] + nums[1] + left_sum
        
        for i in range(1, n - k + 1):
            remove_num(nums[i+1])
            
            new_idx = i + 1 + dist
            if new_idx < n:
                add_num(nums[new_idx])
            
            current_cost = nums[0] + nums[i+1] + left_sum
            if current_cost < min_cost:
                min_cost = current_cost
                
        return min_cost