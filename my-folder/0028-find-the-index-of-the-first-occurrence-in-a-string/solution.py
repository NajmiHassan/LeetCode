class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        H, N = len(haystack), len(needle)
        for i in range(H):
            if haystack[i:i+N] == needle:
                return i
        return -1
