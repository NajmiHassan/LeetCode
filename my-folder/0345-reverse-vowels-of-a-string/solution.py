class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']
        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in vowel:
                while s[right] not in vowel:
                    right -= 1
                s[left], s[right] = s[right], s[left]
                right -= 1

            left += 1
        return "".join(s)

