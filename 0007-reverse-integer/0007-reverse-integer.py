class Solution:
    def reverse(self, x: int) -> int:
        y = str(abs(x))
        y = y.strip()
        y = y[::-1]
        res = int(y)
        if res >= 2** 31 -1 or res <= -2** 31:
            return 0
        elif x < 0:
            return -1 * res
        else:
             return res
        
        