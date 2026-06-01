class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:

        self.stack.append(val)

        # If minStack is empty,
        # current value becomes minimum
        if not self.minStack:
            self.minStack.append(val)

        else:
            # Store the minimum till now
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:

        # Remove from BOTH stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:

        # Top of minStack always contains minimum
        return self.minStack[-1]