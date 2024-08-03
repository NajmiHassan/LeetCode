class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n]= i
        return
        
        # numMap = {}
        # n = len(nums)

        # for i in range(n):
        #     numMap[nums[i]] = i

        # for i in range(n):
        #     complement = target - nums[i]
        #     if complement in numMap and numMap[complement]!=i:
        #         return [i, numMap[complement]]
        
        # return []
