class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest = ""

        for i in range(len(s)):
            # odd length
            odd = expand(i, i)
            # even length
            even = expand(i, i+1)
            
            # pick the longest among current centers
            longest = max(longest, odd, even, key=len)

        return longest