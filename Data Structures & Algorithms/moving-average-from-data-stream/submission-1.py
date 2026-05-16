class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.store = []
        

    def next(self, val: int) -> float:
        self.store.append(val)
        res = sum(self.store[-self.size:])/ len(self.store[-self.size:])
        return res


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
