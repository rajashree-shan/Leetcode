class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        # Helper function to solve linear rob problem
        def rob_linear(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[-1]
        
        # Case 1: Exclude last house
        case1 = rob_linear(nums[:-1])
        # Case 2: Exclude first house
        case2 = rob_linear(nums[1:])
        
        return max(case1, case2)
