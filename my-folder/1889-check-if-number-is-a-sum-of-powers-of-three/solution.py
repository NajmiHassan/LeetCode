class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:

            if n % 3 > 1:
                return False

            n //= 3
        return True

    #     while n > 0:
    #         largestPowerOfThree = self.findLargestPowerOfThree(n)

    #         if n >= largestPowerOfThree:
    #             n = n - largestPowerOfThree
    #         else:
    #             return False

    #     return True
    
    # def findLargestPowerOfThree(self, n:int) -> int:
    #     power = 1
    #     while (power*3) <= n:
    #         power = power * 3
    #     return power


# function checkPowersOfThree(n):
#     // While we haven't reduced the number to zero
#     WHILE n > 0:
#         // Find the largest power of three that doesn't exceed n
#         largestPowerOfThree = findLargestPowerOfThree(n)
        
#         // If we can subtract this power of three, do so
#         IF n >= largestPowerOfThree:
#             n = n - largestPowerOfThree
#         ELSE:
#             // If we can't subtract the current largest power, this means 
#             // we can't represent the number as sum of distinct powers of three
#             RETURN false
    
#     // If we've reduced n to zero, we've successfully represented it
#     RETURN true

# function findLargestPowerOfThree(n):
#     // Start with 3^0 = 1
#     power = 1
    
#     // Keep multiplying by 3 until we exceed n
#     WHILE (power * 3) <= n:
#         power = power * 3
    
#     RETURN power
