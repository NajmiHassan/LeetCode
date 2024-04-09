class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        n = len(tickets)
        time = 0
        
        # Simulate the process until the person at position k buys all their tickets
        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    # Each person buys one ticket
                    tickets[i] -= 1
                    time += 1
                    # If the person at position k has bought all their tickets, return the time
                    if i == k and tickets[k] == 0:
                        return time
            # After each pass, move people who haven't bought all their tickets to the end of the queue
            tickets = [t + 1 if t < 0 else t for t in tickets]
        
        return time



