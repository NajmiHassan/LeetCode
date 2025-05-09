class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = {}

        # Count characters in string s
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Subtract counts based on string t
        for char in t:
            if char not in char_count:
                return False
            else:
                char_count[char] -= 1
                if char_count[char] < 0:
                    return False

        # Ensure all counts are zero
        for count in char_count.values():
            if count != 0:
                return False

        return True
