class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        dp=[0] * (n+1)

        if n==1:
            return nums[0]
        
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        
        for i in range(2,n):
            skip=dp[i-1]
            take=dp[i-2]+nums[i]

            dp[i]=max(skip,take)

        return dp[n-1]
