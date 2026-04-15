class MinStack:

    def __init__(self):
        self.arr = []
        self.mins = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        val = min(val, self.mins[-1] if self.mins else val)
        self.mins.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mins[-1]
