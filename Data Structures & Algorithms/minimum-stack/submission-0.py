class MinStack:
    #Design a stack supports: push, pop, top, getMin operations
    # MinStack(): initializes stack object
    # push(): push value into the stack
    # int top(): get top element from the stack
    # int getMin(): retrieve the minimum element in the stack
    # each operation shouls run in O(1) time

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
