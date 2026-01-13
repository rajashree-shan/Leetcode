class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        min=float('inf')
        for i in prices:
            if i<min:
                min=i
            else:
                maxp=max(maxp,i-min)
        return maxp