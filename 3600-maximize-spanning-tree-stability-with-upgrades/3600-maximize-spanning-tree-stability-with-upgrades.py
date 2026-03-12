class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        base_parent = list(range(n))
        base_rank = [1] * n
        
        # Helper for base DSU setup
        def base_find(i):
            root = i
            while root != base_parent[root]:
                root = base_parent[root]
            curr = i
            while curr != root:
                nxt = base_parent[curr]
                base_parent[curr] = root
                curr = nxt
            return root
            
        def base_union(i, j):
            ru = base_find(i)
            rv = base_find(j)
            if ru != rv:
                if base_rank[ru] < base_rank[rv]:
                    ru, rv = rv, ru
                base_parent[rv] = ru
                if base_rank[ru] == base_rank[rv]:
                    base_rank[ru] += 1
                return True
            return False

        must_count = 0
        min_must = float('inf')
        opt_edges = []
        
        # 1. Process all mandatory edges first
        for u, v, s, m in edges:
            if m == 1:
                if not base_union(u, v):
                    return -1  # A cycle within mandatory edges makes a valid MST impossible
                must_count += 1
                if s < min_must:
                    min_must = s
            else:
                opt_edges.append((u, v, s))
                
        # 2. Global connectivity check to see if a spanning tree is even possible 
        temp_p = list(base_parent)
        def temp_find(i):
            root = i
            while root != temp_p[root]:
                root = temp_p[root]
            curr = i
            while curr != root:
                nxt = temp_p[curr]
                temp_p[curr] = root
                curr = nxt
            return root
            
        temp_comps = n - must_count
        for u, v, s in opt_edges:
            ru = temp_find(u)
            rv = temp_find(v)
            if ru != rv:
                temp_p[rv] = ru
                temp_comps -= 1
        
        if temp_comps > 1:
            return -1  # Cannot connect all nodes even using all available edges

        # Sort optional edges descending to prioritize cost-0 (no upgrade) over cost-1 (upgrade) 
        opt_edges.sort(key=lambda x: x[2], reverse=True)
            
        # 3. Validation function for our binary search
        def check(x):
            if x > min_must:
                return False
            
            # Reset DSU arrays to base state
            p = list(base_parent)
            r = list(base_rank)
            
            def find(i):
                root = i
                while root != p[root]:
                    root = p[root]
                curr = i
                while curr != root:
                    nxt = p[curr]
                    p[curr] = root
                    curr = nxt
                return root
                
            comps = n - must_count
            if comps == 1:
                return True
                
            ups = 0
            
            # Single pass through the sorted optional edges
            for u, v, s in opt_edges:
                if s >= x:
                    # Cost 0: Edge is strong enough as is
                    ru = find(u)
                    rv = find(v)
                    if ru != rv:
                        if r[ru] < r[rv]:
                            ru, rv = rv, ru
                        p[rv] = ru
                        if r[ru] == r[rv]:
                            r[ru] += 1
                        comps -= 1
                        if comps == 1:
                            return True
                elif 2 * s >= x:
                    # Cost 1: Edge needs an upgrade to reach target strength
                    ru = find(u)
                    rv = find(v)
                    if ru != rv:
                        if r[ru] < r[rv]:
                            ru, rv = rv, ru
                        p[rv] = ru
                        if r[ru] == r[rv]:
                            r[ru] += 1
                        comps -= 1
                        ups += 1
                        if ups > k:
                            return False
                        if comps == 1:
                            return True
                else:
                    # Because array is sorted descending, all subsequent edges will also fall short.
                    break
                    
            return comps == 1 and ups <= k

        # 4. Binary search for the maximum stability
        left = 1
        right = min(min_must, 200000)
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1      # Look for a higher stability
            else:
                right = mid - 1     # Stability is too high, lower it
                
        return ans