class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)
        self.rank = [0] * (len(v) + 1)

    def make_set(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px
            else:
                self.p[py] = px
                self.rank[px] += 1


def mst_kruskal(vertices, edges):
    mst = []
    n = len(vertices)

    ds = DisjointSet(vertices)

    for i in range(n + 1):
        ds.make_set(i)

    edges.sort(key=lambda x: x[2])

    for edge in edges:
        s, e, w = edge
        if ds.find_set(s) != ds.find_set(e):
            ds.union(s, e)
            mst.append(edge)

    return mst


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = []
    vertices = list(range(V + 1))

    for i in range(E):
        s, e, w = map(int, input().split())
        edges.append([s, e, w])

    result = mst_kruskal(vertices, edges)

    sum_weight = 0
    for j in range(len(result)):
        sum_weight += result[j][2]
    print(f'#{tc} {sum_weight}')
