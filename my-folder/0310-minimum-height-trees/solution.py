class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0] 

        
        graph = defaultdict(list)
        degrees = [0] * n  

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        
        leaves = deque([node for node in range(n) if degrees[node] == 1])

        while n > 2:
            
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1  
                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        leaves.append(neighbor)

        
        return list(leaves)
