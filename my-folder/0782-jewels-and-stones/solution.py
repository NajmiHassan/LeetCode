class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        noOfJewels = 0
        for stone in stones:
            if stone in jewels:
                noOfJewels += 1
        return noOfJewels
