class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    count += (k - i)
        
        return count
        
        # n = len(arr)
        # count = 0
        # prefix = [0] * (n + 1)

        # for i in range(n):
        #     prefix[i + 1] = prefix[i] ^ arr[i]

        # for i in range(n):
        #     for k in range (i + 1, n):
        #         if prefix[i] == prefix[k + 1]:
        #             count =+ (k - 1)
        
        # return count


