class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split() # make list

        for i in range(len(words)):
            word = words[i]
            reversed_word = word[::-1] 
            words[i] = reversed_word

        # convert to string
        ans = " ".join(words)

        return ans
