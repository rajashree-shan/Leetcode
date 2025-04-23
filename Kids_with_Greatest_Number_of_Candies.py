class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxc=max(candies)
        return [candies[i]+extraCandies >= maxc for i in range(len(candies))]
