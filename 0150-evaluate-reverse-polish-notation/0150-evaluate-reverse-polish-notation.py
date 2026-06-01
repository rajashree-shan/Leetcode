class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:

            # If token is an operator
            if token in ["+", "-", "*", "/"]:

                # IMPORTANT:
                # second popped element is RIGHT operand
                b = stack.pop()

                # first popped element is LEFT operand
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                else:
                    # int() truncates toward zero
                    stack.append(int(a / b))

            else:
                # Convert string number into integer
                stack.append(int(token))

        return stack[0]