class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        hm=set(nums)
        for i in range(n+1):
            if i not in hm:
                return i