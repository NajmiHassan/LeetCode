class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            anagram_map[key].append(string)

        return list(anagram_map.values())
