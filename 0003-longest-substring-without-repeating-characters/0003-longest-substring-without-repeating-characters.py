class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        maxi=0

        left=0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            maxi=max(maxi,right-left+1)
        return maxi