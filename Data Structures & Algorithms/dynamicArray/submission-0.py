class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.a = [0]*capacity

    def get(self, i: int) -> int:
        return self.a[i]

    def set(self, i: int, n: int) -> None:
        self.a[i] = n

    def pushback(self, n: int) -> None:
        if self.length < self.capacity:
            self.a[self.length] = n
            self.length += 1
        else:
            self.resize()
            self.pushback(n)


    def popback(self) -> int:
        self.length -= 1
        return self.a[self.length]

    def resize(self) -> None:
        k = [0] * (self.capacity * 2)
        for i in range(self.length):
            k[i] = self.a[i]
        self.a = k
        self.capacity *= 2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
