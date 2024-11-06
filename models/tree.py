# tree.py
class Node:
    def __init__(self, key, trade):
        self.key = key
        self.trade = trade
        self.left = None
        self.right = None
        self.height = 1

class Tree:
    def insert(self, root, key, trade):
        if not root:
            return Node(key, trade)
        if key < root.key:
            root.left = self.insert(root.left, key, trade)
        else:
            root.right = self.insert(root.right, key, trade)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        
        # Balance adjustments
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root.trade if root else None
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
