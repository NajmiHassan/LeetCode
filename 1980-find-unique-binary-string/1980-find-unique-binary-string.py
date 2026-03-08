class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []

        for i in range(len(nums)):
            current_ch = nums[i][i]

            if current_ch == "0":
                result.append("1")
            else: 
                result.append("0")
        
        return "".join(result)