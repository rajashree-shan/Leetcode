class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=1
        for i in range(2,n+1):
            curr=a+b
            b=a
            a=curr
        return a