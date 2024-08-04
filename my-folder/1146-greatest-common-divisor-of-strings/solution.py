class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # # Check if concatenated strings are equal or not, if not return ""
        # if str1 + str2 != str2 + str1:
        #     return ""
        # # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        # from math import gcd
        # return str1[:gcd(len(str1), len(str2))]
        
        def canConstructFromRepeated(str, part):
            if len(str) % len(part) != 0:
                return False
            repeated = part * (len(str) // len(part))
            return repeated == str

        gcd_length = math.gcd(len(str1), len(str2))

        candidate = str1[:gcd_length]

        if canConstructFromRepeated(str1, candidate) and canConstructFromRepeated(str2, candidate):
            return candidate
        else:
            return ""

