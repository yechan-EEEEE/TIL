import heapq
import math
from collections import defaultdict


def dijkstra(graph, start, Node):
    distances = {v: math.inf for v in range(Node)}  # 모든 정점의 거리를 무한대로 초기화
    # 시작정점을 0으로 초기화
    distances[start] = 0
    # 우선순위 큐
    min_heap = []
    # 시작 정점을 우선순위 큐에 넣고 시작
    # [거리, 정점]
    heapq.heappush(min_heap, [0, start])

    while min_heap:
        # 현재 정점, 현재 정점에 도달하는 거리
        current_distance, current_vertex = heapq.heappop(min_heap)

        # 정점까지의 기존 거리보다 갱신된 거리가 크다면 그냥 넘어감
        if distances[current_vertex] < current_distance:
            continue

        # 인접한 노드에 대해서 거리를 확인
        for adjacent, weight in graph[current_vertex].items():
            # 해당 정점까지의 거리
            # 현재 정점까지의 거리 + A -> b 로 가는 거리
            distance = current_distance + weight
            if distance < distances[adjacent]:  # 기존에 저장된 거리보다 작으면 갱신
                distances[adjacent] = distance
                heapq.heappush(min_heap, [distance, adjacent])

    return distances


t = int(input())
for tc in range(1, t + 1):
    N, T = map(int, input().split())
    Map = defaultdict(dict)
    for _ in range(T):
        a, b, w = map(int, input().split())
        Map[a][b] = w
    start_point = 0
    result_dict = dijkstra(Map, start_point, N)
    result = result_dict[N-1]
    if result == math.inf:
        result = "impossible"
    print(f'#{tc} {result}')
