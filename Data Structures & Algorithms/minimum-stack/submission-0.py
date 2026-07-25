class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minimum = float("inf")
        
    def push(self, val: int) -> None:
        if(self.minimum >= val):
            self.minimum = val
            self.minStack.append(val)

        self.stack.append(val)
        
        print(self.stack)

    
    def pop(self) -> None:
        poppedValue = self.stack.pop()
        if(poppedValue == self.minimum):
            self.minStack.pop()

            if self.minStack:
                self.minimum = self.minStack[-1]
            else:
                self.minimum = float("inf")

        return poppedValue
    
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minimum
        
