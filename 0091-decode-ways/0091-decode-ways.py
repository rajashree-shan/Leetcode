class Solution:
    def numDecodings(self, s: str) -> int:
        # Step 1: Handle edge case for empty string
        if not s or s[0] == '0':
            return 0
        
        # Step 2: Initialize the DP array
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: one way to decode an empty string
        dp[1] = 1  # Base case: one way to decode if the first character is valid
        
        # Step 3: Fill the DP array
        for i in range(2, n + 1):
            # Check single digit (s[i-1])
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            # Check two digits (s[i-2:i])
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        # Step 4: Return the total number of ways to decode
        return dp[n]