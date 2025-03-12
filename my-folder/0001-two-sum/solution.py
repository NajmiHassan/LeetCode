class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indexed_nums = [(nums[i], i) for i in range(len(nums))] 
        
        indexed_nums.sort()

        left = 0
        right = len(nums) - 1
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if current_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []


    #   prevMap = {} #val : index

    #     for i, n in enumerate(nums):
    #         diff = target - n
    #         if diff in prevMap:
    #             return [prevMap[diff], i]
    #         prevMap[n]= i
    #     return

    #       prevMap = {} #val : index

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n]= i
        # return


