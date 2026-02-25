class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_set_bits(n):
            count = 0
            while n > 0:
                n &= (n - 1)
                count += 1
            return count

        arr.sort(key = lambda x: (count_set_bits(x), x))

        return arr