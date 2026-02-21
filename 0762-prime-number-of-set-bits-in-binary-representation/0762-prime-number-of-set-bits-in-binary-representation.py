class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # with custom helper function
        prime = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0

        def count_set_bits(n):
            count = 0
            while n > 0:
                count += n & 1
                n >>= 1
            return count

        for num in range(left, right + 1):
            set_bits = count_set_bits(num)

            if set_bits in prime:
                ans += 1

        return ans

# without helper fuction
    primes = {2, 3, 5, 7, 11 , 13, 17, 19}
        ans = 0

        for num in range(left, right + 1):
            set_bits = num.bit_count()

            if set_bits in primes:
                ans += 1
        
        return ans
