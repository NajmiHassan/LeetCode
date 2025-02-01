class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter = {}
        # for num in nums:
        #     counter[num] = counter.get(num, 0) + 1
        
        # heap = []
        # for num, count in counter.items():
        #     heapq.heappush(heap, (count, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # result = []
        # while heap:
        #     result.append(heapq.heappop(heap)[1])

        # return result

        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums)+ 1)]
        for num, count in counter.items():
            bucket[count].append(num)
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):  # Iterate from highest frequency
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result  # Stop early when we get k elements
        
        return result
        
