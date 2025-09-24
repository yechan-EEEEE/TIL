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


T = int(input())
for C in range(1, T + 1):
    N = int(input())
    vertices = list(range(N))
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())

    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            dx = x_list[i] - x_list[j]
            dy = y_list[i] - y_list[j]
            L2 = dx * dx + dy * dy
            cost = E * L2
            edges.append((i, j, cost))

    mst = prim(vertices, edges)
    total_cost = 0
    for edge in mst:
        s, e, w = edge
        total_cost += w
    print(f'#{C} {round(total_cost)}')
