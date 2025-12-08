class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []

        # One pass: identify invalid parenthesis
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()  # we have a match
                else:
                    s[i] = ''  # mark invalid ')'

        # Remove any unmatched '(' left in stack
        while stack:
            s[stack.pop()] = ''

        return "".join(s)
  