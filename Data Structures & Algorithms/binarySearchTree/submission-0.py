class Treenode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.right = None
        self.left = None
class TreeMap:
    
    def __init__(self,):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        newNode = Treenode(key, val)
        if self.root == None:
            self.root = newNode
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
        cur = self.root
        while cur != None:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        cur = self.findmin(self.root)
        return cur.val if cur else -1

    def findmin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node


    def getMax(self) -> int:
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val if cur else -1


    def remove(self, key: int) -> None:
        self.root = self.removehelper(self.root, key)
        

    def removehelper(self, cur: TreeNode, key: int) -> TreeNode:
        if cur == None:
            return None

        if key > cur.key:
            cur.right = self.removehelper(cur.right, key)
        elif key < cur.key:
            cur.left = self.removehelper(cur.left, key)
        else:
            if cur.left == None:
                return cur.right
            elif cur.right == None:
                return cur.left
            else:
                minNode = self.findmin(cur.right)
                cur.key = minNode.key
                cur.val = minNode.val
                cur.right = self.removehelper(cur.right, minNode.key)
        return cur

    def getInorderKeys(self) -> List[int]:
        res = []
        self.inordertraversal(self.root, res)
        return res
    def inordertraversal(self, root: TreeNode, res: List[int]) -> None:
        if root != None:
            self.inordertraversal(root.left, res)
            res.append(root.key)
            self.inordertraversal(root.right, res)




