class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hm={')':'(',']':'[','}':'{'}
        for i in s:
            if i not in hm:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    pop=stack.pop()
                    if pop!=hm[i]:
                        return False
        return not stack
