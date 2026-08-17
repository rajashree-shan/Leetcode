class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}

        max_freq=0
        ans=0
        left=0
        for right ,char in enumerate(s):
            count[char]=count.get(char,0)+1

            max_freq=max(max_freq,count[char])

            while right-left+1 - max_freq > k:
                count[s[left]]-=1
                left+=1

            ans=max(ans,right-left+1)
        return ans

 
