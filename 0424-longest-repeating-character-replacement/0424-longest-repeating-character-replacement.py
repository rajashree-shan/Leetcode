class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt={}
        left=0
        maxi=0
        ans=0

        for right,num in enumerate(s):
            cnt[num]=cnt.get(num,0)+1
            maxi=max(maxi,cnt[num])

            if right-left+1 -maxi > k:
                cnt[s[left]]-=1
                left+=1
        ans = max(ans, right - left + 1)

        return ans