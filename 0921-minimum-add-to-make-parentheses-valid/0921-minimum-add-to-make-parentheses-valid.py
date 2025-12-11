class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance=0
        addition=0
        for ch in s:
            if ch=="(":
                balance+=1
            else :
                if balance>0:
                    balance-=1
                else:
                    addition+=1
        return addition+balance