class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        ans=len(words[-1])
        return ans
