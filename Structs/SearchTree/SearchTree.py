class TreeNode:
    def __init__(self, key, value=None):
        self.key = key  # Ключ
        self.value = value  # Значение (опционально)
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок

class SearchTree:
    def __init__(self):
        self.root = None  # Корень дерева

    # Вставка ключа и значения
    def insert(self, key, value=None):
        self.root = self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node, key, value):
        if node is None:
            return TreeNode(key, value)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, value)
        return node

    # Поиск по ключу
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    # Найти минимум (самый левый узел)
    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node

    # Найти максимум (самый правый узел)
    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, node):
        if node is None:
            return None
        while node.right:
            node = node.right
        return node

    # Удаление узла по ключу
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Случай: узел с одним или без потомков
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Случай: узел с двумя потомками
            min_larger_node = self._find_min(node.right)
            node.key = min_larger_node.key
            node.value = min_larger_node.value
            node.right = self._delete_recursive(node.right, min_larger_node.key)
        return node

    # Обход в отсортированном порядке (in-order traversal)
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append((node.key, node.value))
            self._inorder_recursive(node.right, result)

# Пример использования
if __name__ == "__main__":
    tree = SearchTree()
    
    # Вставка элементов
    tree.insert(50, "Value 50")
    tree.insert(30, "Value 30")
    tree.insert(70, "Value 70")
    tree.insert(20, "Value 20")
    tree.insert(40, "Value 40")
    tree.insert(60, "Value 60")
    tree.insert(80, "Value 80")
    
    # Поиск по ключу
    print("Поиск ключа 40:", tree.search(40))
    print("Поиск ключа 100:", tree.search(100))
    
    # Минимум и максимум
    print("Минимум:", tree.find_min().key)
    print("Максимум:", tree.find_max().key)
    
    # Удаление узла
    print("Удаляем ключ 30")
    tree.delete(30)
    
    # Вывод в отсортированном порядке
    print("Дерево в отсортированном порядке:", tree.inorder())
