class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        def robLinear(houses):
            m = len(houses)

            if m == 1:
                return houses[0]

            dp = [0] * m

            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, m):
                skip = dp[i - 1]
                take = dp[i - 2] + houses[i]

                dp[i] = max(skip, take)

            return dp[m - 1]

        case1 = robLinear(nums[:-1])
        case2 = robLinear(nums[1:])

        return max(case1, case2)