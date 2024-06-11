class Solution:
    def minimumChairs(self, s: str) -> int:
        cur_count = 0
        max_count = 0

        for char in s:
            if char == "E":
                cur_count += 1
                max_count = max(max_count, cur_count)
            else:
                cur_count -= 1
        
        return max_count

#time complexity --> O(n) where n = the number of characters in s
#space comlexity --> O(1)

