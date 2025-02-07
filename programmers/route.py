def solution(N, a, b):
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [1] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)
            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1

    intervals = list(zip(a, b))
    uf = UnionFind(N)
    result = []

    for i in range(N):
        for j in range(i):
            a1, b1 = intervals[i]
            a2, b2 = intervals[j]
            if not (b1 < a2 or b2 < a1):
                uf.union(i, j)


        group_count = len(set(uf.find(k) for k in range(i + 1)))
        result.append(group_count)

    return result
