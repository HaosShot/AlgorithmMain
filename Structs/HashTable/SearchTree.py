class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def find_minimum(self):
        return self._find_minimum(self.root)

    def _find_minimum(self, node):
        while node.left:
            node = node.left
        return node

    def find_maximum(self):
        return self._find_maximum(self.root)

    def _find_maximum(self, node):
        while node.right:
            node = node.right
        return node

    def find_predecessor(self, key):
        current = self.search(key)
        if current and current.left:
            return self._find_maximum(current.left)
        return None

    def find_successor(self, key):
        current = self.search(key)
        if current and current.right:
            return self._find_minimum(current.right)
        return None

    def in_order_traversal(self, node, result):
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.key)
            self.in_order_traversal(node.right, result)

    def sorted_order(self):
        result = []
        self.in_order_traversal(self.root, result)
        return result

    def select(self, i):
        if i > 0 and i <= len(self.sorted_order()):
            return self.sorted_order()[i-1]
        return None

    def _rank(self, node, key):
        if node is None:
            return 0
        if key < node.key:
            return self._rank(node.left, key)
        elif key > node.key:
            return 1 + self.size(node.left) + self._rank(node.right, key)
        else:
            return self.size(node.left) + 1
    
    def rank(self, key):
        return self._rank(self.root, key)

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_minimum(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node
    
    def delete(self, key):
        self.root = self._delete(self.root, key)

bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(9)

print("Поиск ключа 3:", bst.search(3).key if bst.search(3) else "Not found")

print("Минимальный ключ:", bst.find_minimum().key)
print("Максимальный ключ:", bst.find_maximum().key)

print("Предшественник 4:", bst.find_predecessor(4).key if bst.find_predecessor(4) else "None")
print("Преемник 4:", bst.find_successor(4).key if bst.find_successor(4) else "None")

print("Отсортированный порядок:", bst.sorted_order())

print("3-й элемент в отсортированном порядке:", bst.select(3))

print("Ранг для ключа 7:", bst.rank(7))

bst.delete(3)
print("Удаление ключа 3, отсортированный порядок теперь:", bst.sorted_order())
