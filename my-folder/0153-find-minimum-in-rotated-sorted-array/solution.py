class Solution(object):
    def findMin(self, nums):
        l,r=0,len(nums)-1
        while  l<r:
            mid=l+(r-l)//2
            if mid<r and nums[mid]>nums[mid+1]:
                return nums[mid+1]
            elif nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]>nums[l]:
                l=mid+1
            elif nums[mid]<nums[r]:
                r=mid-1
        return nums[0]
