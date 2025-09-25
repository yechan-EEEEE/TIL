def floyd_warshall(graph):
    V = len(graph)

    for k in range(V):  # 모든 정점을 경유 정점으로 고려
        for i in range(V):  # 시작 정점을 고정
            for j in range(V):  # 도착 정점을 고정
                # (시작 정점 -> k 정점) 거리 + ( k 정점 -> 도착 정점) 거리
                # (시작 정점 -> 도착 정점) 거리
                # 경유해서 가는 게 더 가깝다면 갱신
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    # 음수 사이클 확인
    for i in range(V):
        if graph[i][i] < 0:
            print("음수 사이클이 존재합니다.")
            break
    return graph  # 최단 경로가 포함된 거리 행렬을 반환


INF = float('inf')  # 무한대

# 예시 그래프의 인접 행렬
adj_matrix = [
    [0, 4, 2, 5, INF],
    [INF, 0, 1, INF, 4],
    [1, 3, 0, 1, 2],
    [-2, INF, INF, 0, 2],
    [INF, -3, 3, 1, 0]
]

# 음수 사이클 확인
# adj_matrix = [
#     [0, -4, 2, 5, INF],
#     [INF, 0, 1, INF, 4],
#     [1, 3, 0, 1, 2],
#     [-2, INF, INF, 0, 2],
#     [INF, -3, 3, 1, 0]
# ]

result = floyd_warshall(adj_matrix)

# 최단 거리 행렬 출력
for row in result:
    print(row)
