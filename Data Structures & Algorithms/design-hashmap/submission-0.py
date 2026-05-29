class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [Node(0,0) for _ in range(1000)]    

    def hash_function(self, key: int):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = Node(key, value)

        

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)