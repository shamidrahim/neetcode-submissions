class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = [None] * self.cap
        self.size = 0

    def hash(self, key):
        index = key % self.cap
        return index        


    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key,value)
                self.size += 1
                if self.size >= self.cap // 2:
                    self.resize()
                return
            elif self.map[index].key == key:
                self.map[index].val = value
                return
            index += 1
            index = index % self.cap



    def get(self, key: int) -> int:
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key != key:
                index += 1
                index = index % self.cap
            elif self.map[index].key == key:
                return self.map[index].val
        return -1


    def remove(self, key: int) -> bool:
        if self.get(key) == -1:
            return False
        
        index = self.hash(key)    
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
            index += 1
            index = index % self.cap
        return True


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.cap


    def resize(self) -> None:
        self.cap = 2 * self.cap
        newMap = [None] * self.cap

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.insert(pair.key, pair.val)
