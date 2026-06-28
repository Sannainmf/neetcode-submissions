class MinStack:

    def __init__(self):
        self.arr = []
        self.minArr = []

    def push(self, val: int) -> None:

        self.arr.append(val)

        if not self.minArr:
            self.minArr.append(val)
        else:
            if val < self.minArr[-1]:
                self.minArr.append(val)
            else:
                self.minArr.append(self.minArr[-1])        

    def pop(self) -> None:

        self.arr.pop()
        self.minArr.pop()
        

    def top(self) -> int:
        
        return self.arr[-1]

    def getMin(self) -> int:

        return self.minArr[-1]
        
