class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=int(a,2),int(b,2)
        
        while b:
            carry=(a&b) <<1
            w_carry=a^b
            a,b=w_carry,carry
        return bin(a)[2:]
