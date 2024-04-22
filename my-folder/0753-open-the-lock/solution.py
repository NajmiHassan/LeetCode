class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        
        
        if target in deadends:
            return -1
        
        
        queue = deque([("0000", 0)])         
        
        while queue:
            state, steps = queue.popleft()
            
           
            for i in range(4):
                for delta in [-1, 1]:
                    next_state = state[:i] + str((int(state[i]) + delta) % 10) + state[i+1:]
                    
                    
                    if next_state not in deadends:
                        deadends.add(next_state)  
                        queue.append((next_state, steps + 1))
                        
                       
                        if next_state == target:
                            return steps + 1
        
        return -1
