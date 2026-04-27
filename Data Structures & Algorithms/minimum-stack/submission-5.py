class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []


    def push(self, val: int) -> None:
        if not self.min:
            self.min.append(val)
        elif val <= self.min[-1]  :
            self.min.append(val)

        

        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min[-1] == val:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
