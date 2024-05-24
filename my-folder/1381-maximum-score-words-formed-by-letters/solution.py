class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        letter_count = Counter(letters)

        def word_score(word):
            return sum(score[ord(char) - ord('a')] for char in word)
        def can_form_word(word, available_letters):
            word_count = Counter(word)
            for char in word_count:
                if word_count[char] > available_letters[char]:
                    return False
            return True

        def backtrack(index, available_letters):
            if index == len(words):
                return 0 
            
            max_score = backtrack(index +1, available_letters)

            current_word = words[index]
            if can_form_word(current_word, available_letters):
                update_letters = available_letters - Counter(current_word)
                max_score = max(max_score, word_score(current_word) + backtrack(index+ 1, update_letters))
            return max_score

        return backtrack(0, letter_count)






