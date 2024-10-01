class CustomStack:

    def __init__(self, maxSize: int):
        self.lengthMax = maxSize
        self.length = 0
        self.obj = []

    def push(self, x: int) -> None:
        if self.length == self.lengthMax:
            return None
        self.length += 1
        self.obj.append(x)
        return None

    def pop(self) -> int:
        if self.length == 0:
            return -1
        self.length -=  1
        x = self.obj.pop()
        return x

    def increment(self, k: int, val: int) -> None:
        k = min(self.length, k)
        self.obj[:k] = [i+val for i in self.obj[:k]]

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)