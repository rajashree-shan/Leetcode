class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count={}

        for char in s:
            count[char]=count.get(char,0)+1
        left=[]
        middle=""

        for i in sorted(count):
            left.append(i*(count[i]//2))

            if count[i]%2==1:
                middle=i
        left="".join(left)

        return left+middle+left[::-1]
