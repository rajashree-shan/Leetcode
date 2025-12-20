class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        current_string=""
        num=0
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch=="[":
                stack.append((current_string,num))
                current_string=""
                num=0
            elif ch=="]":
                prevs,prevn=stack.pop()
                current_string=prevs+current_string*prevn
            else:
                current_string+=ch
        return current_string


