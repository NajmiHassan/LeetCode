class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range (2):
            for n in nums:
                ans.append(n)
        return ans
        # nums.extend(nums)
        # return nums

        # return nums*2

        # nums+=nums
        # return nums 

        # return nums + nums
