class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort()
        result = [0] * len(deck)
        indexes = list(range(len(deck)))

        for card in deck:
            result[indexes.pop(0)] = card
            if indexes:
                indexes.append(indexes.pop(0))
                
        return result




