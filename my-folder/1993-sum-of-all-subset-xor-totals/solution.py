class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        subset_xor_sum = 0
        
        # Iterate over all possible subset sizes
        for i in range(n+1):
            # Generate all subsets of size i
            for subset in combinations(nums, i):
                # Compute the XOR of the current subset
                xor_total = 0
                for num in subset:
                    xor_total ^= num
                # Add the XOR total of this subset to the overall sum
                subset_xor_sum += xor_total
                
        return subset_xor_sum
