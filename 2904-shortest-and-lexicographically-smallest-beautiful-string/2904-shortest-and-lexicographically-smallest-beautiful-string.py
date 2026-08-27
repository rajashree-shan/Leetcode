class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans=""
        left=0
        ones=0
        current=0
        for right in range(len(s)):
            if s[right]=='1':
                ones+=1

            while ones>k:
                if s[left]=='1':
                    ones-=1
                left+=1


            while ones==k and s[left]=='0':
                    left+=1

            if ones==k:
                current=s[left:right+1]

                if ans=="":
                    ans=current

                elif len(current)<len(ans):
                    ans=current

                elif len(current) == len(ans) and current < ans:
                        ans = current
        return ans