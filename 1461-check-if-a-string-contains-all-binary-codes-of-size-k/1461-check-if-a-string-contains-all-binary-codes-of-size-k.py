class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen_code = set()

        target_count = 1 << k

        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            seen_code.add(substring)

            if len(seen_code) == target_count:
                return True

        return len(seen_code) == target_count