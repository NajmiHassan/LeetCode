class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        prefix_length = len(prefix)

        for s in strs[1:]:
            while prefix != s[0:prefix_length]:
                prefix_length -= 1
                if prefix_length == 0:
                    return ""

                prefix = prefix[0:prefix_length]
        
        return prefix