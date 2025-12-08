class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        last_op="+"
        num=0
        for i,ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in'+-*/' or i==len(s)-1:
                if last_op == '+':
                    stack.append(num)
                elif last_op == '-':
                    stack.append(-num)
                elif last_op == '*':
                    stack[-1] = stack[-1] * num
                elif last_op == '/':
                    stack[-1] = int(stack[-1] / num)

                num = 0
                last_op = ch

        return sum(stack)
