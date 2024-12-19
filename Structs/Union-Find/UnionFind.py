class UnionFind:
    def __init__(self, X):
        self.parent = {x: x for x in X}  
        self.rank = {x: 0 for x in X}    

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False


X = [1, 2, 3, 4, 5]

un = UnionFind(X)

print(un.union(1, 2))  
print(un.union(3, 4))  
print(un.union(2, 3))  

print(un.find(1))  
print(un.find(4))  
print(un.find(5))  

print(un.union(1, 4))  
