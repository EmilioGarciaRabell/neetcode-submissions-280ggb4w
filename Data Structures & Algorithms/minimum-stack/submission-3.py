class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        self.max = []


    def push(self, val: int) -> None:
        if not self.min:
            self.min.append(val)
        elif val <= self.min[-1]  :
            self.min.append(val)

        if not self.max:
            self.max.append(val)
        elif val >= self.max[-1]:
            self.max.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.max[-1] == val:
            self.max.pop()
        if self.min[-1] == val:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
