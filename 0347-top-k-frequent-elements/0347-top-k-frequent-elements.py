from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        b = [[] for _ in range(n + 1)]
        
        for num, freq in counter.items():
            b[freq].append(num)
        
        ans = []
        for i in range(n, -1, -1):
            if b[i]:
                ans.extend(b[i])
            if len(ans) >= k:
                break
        
        return ans[:k]


        
        