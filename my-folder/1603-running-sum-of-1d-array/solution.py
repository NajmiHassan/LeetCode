class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        stack=[]
        s=0
        for i,j in enumerate(nums,1):
            s+=j
            stack.append(s)
        return stack
