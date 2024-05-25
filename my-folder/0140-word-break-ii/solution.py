class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(index):
            if index in memo:
                return memo[index]
            if index == len(s):
                return['']
            
            sentences = []
            for end in range(index +1, len(s) + 1):
                word = s[index:end]
                if word in word_set:
                    following_sentences = backtrack(end)
                    for sentence in following_sentences:
                        if sentence:
                            sentences.append(word + ' ' + sentence)
                        else:
                            sentences.append(word)

            memo[index] = sentences
            return sentences

        return backtrack(0)
                        









