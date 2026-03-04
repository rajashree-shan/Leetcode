class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x%10==0 and x!=0:
            return False
        rev_half=0
        while x>rev_half :
            rev_half = rev_half * 10 + (x % 10)
            x //= 10
        return x==rev_half or x == rev_half // 10