def bellman_ford(graph, start):
    v_count = len(graph)  # 그래프의 정점 수
    # 시작 정점에서 모든 정점까지의 거리를 무한대로 초기화
    distances = {v: float('inf') for v in graph}
    distances[start] = 0  # 시작 정점의 거리를 0으로 설정

    # 모든 정점에 대해서 반복 ( 정점 개수 - 1 )
    # => 최악의 경우, 최단거리를 구하는데 엣지의 개수가 V -1 개 일수 있으니까
    for i in range(v_count - 1):
        updated = False  # 거리를 업데이트한 적 있는 지 확인하는 변수
        # 업데이트한 적이 없으면, 순회를 더 이상 진행하지 않죠

        # 모든 정점에 대해서 연결된 정점을 확인한다.
        for u in graph:
            for v, weight in graph[u].items():

                # [ 시작 정점(u) 에 도달하는 최소 거리 + 가중치 ] 가 [ 도착 정점(v)의 최소 거리]
                # 보다 작은 경우에는 갱신을 한다.
                # (시작 정점(u)는 무한대면 안된다 => 아직 도달할 수 없는 정점이니까 )
                # 결국 처음 순회할 때는 시작 정점이 0이기 때문에, 갱신이 가능합니다.
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    updated = True

        # 거리 업데이트가 된 적이 없다?? 그러면 순회를 더이상 하지 않음
        # 왜냐? 이미 최단거리가 만들어졌다는 소리니까
        if not updated:
            break

    # 음수 사이클 검출
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                # 여기에 들어왔다는건, 값이 갱신되었다는 소리
                print("음수 사이클이 발생했어요!")
                return

    return distances


# 예시 그래프
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 3, 'D': 2, 'E': 3},
    'C': {'B': 1, 'D': 4, 'E': 5},
    'D': {'E': -3},
    'E': {'F': 2},
    'F': {}
}

# 시작 정점 설정
start_vertex = 'A'

# 벨만-포드 알고리즘 실행
result = bellman_ford(graph, start_vertex)

print(f"'{start_vertex}': {result}")
