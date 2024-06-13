class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #hashset
        #time complexity--->O(n)
        #space complexity--->O(n)
        hashset = set()

        for n in nums:            
            if n in hashset:
                return True
            hashset.add(n)
        return False


        #brute force
        #time complexity--->O(n^2)
        #space complexity--->O(1)
        #sorting
        #time complexity--->O(nlogn)
        #space complexity--->O(1)
        
