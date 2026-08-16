class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n1=len(s1)
        n2=len(s2)
        count1=[0]*26
        count2=[0]*26
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')]+=1
            count2[ord(s2[i])-ord('a')]+=1

        if count1==count2:
            return True
        for i in range(n1,n2):
            count2[ord(s2[i])-97]+=1
            count2[ord(s2[i-n1]) - 97]-=1
            if count1==count2:
                return True

        return False
        

