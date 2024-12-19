class HashTable:
    def __init__(self, size=50):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def lookup(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        if bucket is None:
            return f"Объект с ключом {key} не найден."
        
        for pair in bucket:
            if pair[0] == key:
                return pair[1] 

        return f"Объект с ключом {key} не найден."

    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = []

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  
                return

        self.table[index].append([key, value])

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        if bucket is None:
            return f"Объект с ключом {key} не найден."

        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                if len(bucket) == 0:
                    self.table[index] = None
                return f"Объект с ключом {key} удалён."
            
        return f"Объект с ключом {key} не найден."


hash_table = HashTable(size=10)

hash_table.insert("Яблоко", 1)
hash_table.insert("Овца", 2)
hash_table.insert("Баран", 3)

print(hash_table.lookup("Яблоко"))  
print(hash_table.lookup("Баран"))  

print(hash_table.lookup("Овца"))  
print(hash_table.delete("Овца")) 
print(hash_table.lookup("Овца")) 
