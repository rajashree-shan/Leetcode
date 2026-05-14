class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        heap=[]

        for i,j in count.items():
            heapq.heappush(heap,(j,i))

            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq, num in heap]

