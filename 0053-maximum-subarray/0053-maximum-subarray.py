class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        n=len(nums)
        current=0
        for i in range(n):
            current+=nums[i]
            if current>maxi:
                maxi=current
            if current<0:
                current=0
        return maxi