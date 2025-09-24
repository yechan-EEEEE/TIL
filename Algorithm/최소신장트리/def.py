class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)  # 부모 노드 배열 초기화
        self.rank = [0] * (len(v) + 1)  # 랭크 배열 초기화

    def make_set(self, x):
        self.p[x] = x  # 각 노드가 자기 자신을 부모로 가지도록 초기화
        self.rank[x] = 0  # 초기 랭크는 0

    def find_set(self, x):
        if x != self.p[x]:  # 노드 x가 자기 자신을 부모로 가지지 않는 경우
            self.p[x] = self.find_set(self.p[x])  # 부모 노드를 재귀적으로 찾고 경로 압축 수행
        return self.p[x]

    def union(self, x, y):
        px = self.find_set(x)  # 노드 x의 대표자(부모) 찾기
        py = self.find_set(y)  # 노드 y의 대표자(부모) 찾기

        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py  # x의 부모를 y의 부모로 설정
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px  # y의 부모를 x의 부모로 설정
            else:
                self.p[py] = px  # y의 부모를 x의 부모로 설정
                self.rank[px] += 1  # x의 랭크를 1 증가


def mst_kruskal(vertices, edges):
    mst = []  # 최소 신장 트리 저장
    n = len(vertices)

    ds = DisjointSet(vertices)

    # 초기화
    for i in range(n + 1):
        ds.make_set(i)

    # 가중치를 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    for edge in edges:
        s, e, w = edge  # 시작정점, 도착정점, 가중치
        '''
            이미 가중치를 기준으로 정렬했으므로
            최소 신장 트리를 구성하는 과정에서 가중치는 신경쓰지 않아도 된다.

            가중치가 높은 간선의 두 노드가 탐색 대상이 되더라도
            이전에 더 낮은 가중치의 간선으로 이어지도록 했으므로
            이미 MST에 포함되어 있음
        '''
        if ds.find_set(s) != ds.find_set(e):  # 시작정점과 도착정점이 다른 집합에 속한 경우
            ds.union(s, e)  # 두 집합을 합침
            mst.append(edge)  # 현재 간선을 MST에 추가

    return mst


 ###########################






import heapq

def prim(vertices, edges):
    mst = []  # 최소 신장 트리 저장

    adj_list = {v: [] for v in vertices}
    for start_v, end_v, w in edges:
        adj_list[start_v].append((end_v, w))
        adj_list[end_v].append((start_v, w))

    visited = set()  # 방문한 노드 집합
    init_vertex = vertices[0]  # 초기 정점

    # 초기 정점의 모든 간선을 힙에 추가
    # 가중치, 시작 정점, 도착 정점
    min_heap = [[w, init_vertex, e] for e, w in adj_list[init_vertex]]

    # 초기 정점의 간선들을 가중치 기준으로 최소 힙으로 변환
    heapq.heapify(min_heap)
    visited.add(init_vertex)  # 초기 정점 방문

    while min_heap:
        # 가중치가 가장 작은 간선 추출
        weight, start_v, end_v = heapq.heappop(min_heap)
        if end_v in visited: continue  # 이미 방문한 정점이면 건너뜀

        visited.add(end_v)  # 새로운 정점 방문
        mst.append((start_v, end_v, weight))  # 간선을 MST에 추가

        # 도착정점, 가중치
        for adj_v, adj_w in adj_list[end_v]:  # 새로 방문한 정점의 모든 인접 간선 처리
            if adj_v in visited: continue  # 이미 방문한 정점은 건너뜀
            heapq.heappush(min_heap, [adj_w, end_v, adj_v])  # 힙에 간선 추가

    return mst


# '''
#     가중치 그래프 형상
#          1
#       ¹ / \ ²
#        2---3
#          ³
# '''
# vertices = [1, 2, 3]
# edges = [[1, 2, 1], [2, 3, 3], [1, 3, 2]]
#
# # 인접 리스트 생성
#
#
# '''
#     MST 구성 결과
#          1
#       ¹ / \ ²
#        2   3
# '''
# mst = prim(vertices, edges)  # [(1, 2, 1), (1, 3, 2)]
# print(mst)
