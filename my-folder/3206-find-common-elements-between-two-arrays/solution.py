class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a=set(nums1)
        b=set(nums2)
        ans=[0,0]
        for i in nums1:
            if i in b:
                ans[0]=ans[0]+1
        for i in nums2:
            if i in a:
                ans[1]=ans[1]+1
        return ans
        
