class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height)<= 2:
            return 0
        
        ans = 0
        
        #using two pointers i and j on indices 1 and n-1
        i = 1
        j = len(height) - 1
        
        #initialising leftmax to the leftmost bar and rightmax to the rightmost bar
        lmax = height[0]
        rmax = height[-1]
        
        while i <=j:
            # check lmax and rmax for current i, j positions
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[j]
            
            #fill water upto lmax level for index i and move i to the right
            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1
				
            #fill water upto rmax level for index j and move j to the left
            else:
                ans += rmax - height[j]
                j -= 1
                
        return ans

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0
    
#         n = len(height)
#         left_max = [0] * n
#         right_max = [0] * n
#         left_max[0] = height[0]
#         right_max[n - 1] = height[n - 1]
        
#         # Fill left_max array with the maximum height encountered so far from the left
#         for i in range(1, n):
#             left_max[i] = max(left_max[i - 1], height[i])
        
#         # Fill right_max array with the maximum height encountered so far from the right
#         for i in range(n - 2, -1, -1):
#             right_max[i] = max(right_max[i + 1], height[i])
        
#         # Calculate the trapped water for each position
#         water = 0
#         for i in range(n):
#             water += min(left_max[i], right_max[i]) - height[i]
        
#         return water
