class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        
class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.map = [None] * self.cap
        
    def hash_function(self, key: int):
        return key % self.cap

        

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        node = self.map[index]
        if not node:
            self.map[index] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while node:
                if node.key == key:
                    node.val = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1
        if self.size / self.cap >= 0.5:
            self.resize()
        

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.map[index]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1
        

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.map[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.map[index] = node.next
                self.size -= 1
                return True
            node, prev = node.next, node
        return False
            
        

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.cap
        

    def resize(self) -> None:
        newCap = self.cap * 2
        new_map = [None] * newCap
        for node in self.map:
            while node:
                index = node.key % newCap
                if new_map[index] is None:
                    new_map[index] = Node(node.key, node.val)
                else:
                    new_node = new_map[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.val)
                node = node.next
        self.cap = newCap
        self.map = new_map
        