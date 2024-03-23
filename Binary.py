class BinaryTreeNode:
    def __init__(self, obj):
        self.obj = obj
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, obj):
        if self.root is None:
            self.root = BinaryTreeNode(obj)
        else:
            self._insert(self.root,obj)

    def _insert(self, node, obj):
        if obj.name < node.obj.name:
            if node.left is None:
                node.left = BinaryTreeNode(obj)
            else:
                self._insert(node.left, obj)
        elif obj.name > node.obj.name:
            if node.right is None:
                node.right = BinaryTreeNode(obj)
            else:
                self._insert(node.right, obj)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or key == node.obj.name:
            return node.obj
        elif key < node.obj.name:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
