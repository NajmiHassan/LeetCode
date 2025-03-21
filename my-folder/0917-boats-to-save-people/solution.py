class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
            boat, lo, hi = 0, 0, len(people) - 1
            people = sorted(people)
            while lo <= hi:
                if people[hi] + people[lo] <= limit:
                    lo += 1
                boat += 1
                hi -= 1
            return boat
