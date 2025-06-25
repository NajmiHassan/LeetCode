class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(" ")

        # Check for unequal length
        if len(pattern) != len(words):
            return False

        char_to_words = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            if c in char_to_words:
                if char_to_words[c] != w:
                    return False
            else:
                char_to_words[c] = w  # ✅ Corrected assignment

            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c  # ✅ Corrected assignment

        return True

