class MinStack:

    def __init__(self):
        self.stack = []
        self.extra_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.extra_stack.append(min(val,self.extra_stack[-1] if self.extra_stack else val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.extra_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.extra_stack[-1]
        
