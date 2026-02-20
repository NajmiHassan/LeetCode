class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ""

        substrings = []
        count = 0 
        start = 0

        for i, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1

            if count == 0:
                inner_string = s[start + 1 : i]
                processed_inner = self.makeLargestSpecial(inner_string)

                substrings.append("1" + processed_inner + "0")

                start = i + 1

        substrings.sort(reverse=True)

        return "".join(substrings)

                


