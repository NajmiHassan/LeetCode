class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        
        tree_min = [0] * (4 * n)
        tree_max = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
     
        def push(node):
            if lazy[node] != 0:
                add = lazy[node]
                left = 2 * node
                right = 2 * node + 1
                
              
                lazy[left] += add
                tree_min[left] += add
                tree_max[left] += add
                
             
                lazy[right] += add
                tree_min[right] += add
                tree_max[right] += add
                
               
                lazy[node] = 0

       
        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return
            
            if l <= start and end <= r:
                tree_min[node] += val
                tree_max[node] += val
                lazy[node] += val
                return
            
            push(node)
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)
            
            tree_min[node] = min(tree_min[2 * node], tree_min[2 * node + 1])
            tree_max[node] = max(tree_max[2 * node], tree_max[2 * node + 1])

       
        def query_first_zero(node, start, end, l, r):
            
            if l > end or r < start:
                return -1
            
            if tree_min[node] > 0 or tree_max[node] < 0:
                return -1
            
            
            if start == end:
                return start if tree_min[node] == 0 else -1
            
            push(node)
            mid = (start + end) // 2
            
            
            res = query_first_zero(2 * node, start, mid, l, r)
            if res != -1:
                return res
            
           
            return query_first_zero(2 * node + 1, mid + 1, end, l, r)

        last_pos = {}
        max_len = 0
        
        for i, x in enumerate(nums):
            
            val = 1 if x % 2 == 0 else -1
            
            prev = last_pos.get(x, -1)
            
            
            update(1, 0, n - 1, prev + 1, i, val)
            
            last_pos[x] = i
            
            
            idx = query_first_zero(1, 0, n - 1, 0, i)
            
            if idx != -1:
                current_len = i - idx + 1
                if current_len > max_len:
                    max_len = current_len
                    
        return max_len