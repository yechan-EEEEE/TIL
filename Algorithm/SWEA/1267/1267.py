# # import sys
# # sys.stdin = open('sample_input (1).txt')
# from collections import defaultdict

# # 후위순회로 구현하면 됩니다.
# def dfs(v):
#     # 현재 정점을 방문했다고 표시
#     visited[v] = True

#     # 인접한 정점들을 다시 dfs 호출
#     for neighbor in graph[v]:
#         # 방문한 적이 없는 인접 정점들만 DFS 시행
#         if not visited[neighbor]:
#             # 실행되면서 제일 안쪽으로 파고든다.
#             dfs(neighbor)

#     # 더 이상 파고들 때가 없는 경우에, 현재 정점을 결과에 추가한다.
#     result.append(v)


# T = 4
# for tc in range(1, T + 1):
#     v_cnt, e_cnt = map(int, input().split())
#     edges = list(map(int, input().split()))

#     # DAG 그래프 구성
#     # 인접리스트 형태로 만들거다.
#     graph = defaultdict(list)
#     # 시작점과 끝정점을 서로 연결해준다.
#     for i in range(e_cnt):
#         graph[edges[2*i]].append(edges[2*i+1])

#     # 방문여부를 체크해야 한다.
#     visited = [False] * (v_cnt + 1)
#     result = []

#     """
#     모든 정점에 대해서 DFS를 실행한다. 
#     - 연결되지 않은 그래프가 주어졌을 때도, 모두 방문할 수 있도록 
#     (각 연결된 부분끼리의 순서만 올바르게 유지되면 아무 문제가 없다 )
#     => 그렇기 때문에 결과가 유일성 보장이 안된다는 겁니다. 
#     """
#     for v in range(1, v_cnt + 1):
#         if not visited[v]:  # 방문하지 않은 정점에서만 DFS를 돌린다.
#             dfs(v)

#     print(f"#{tc}", *result[::-1])
from collections import defaultdict, deque


T = 10
for tc in range(1, T + 1):
    v_cnt, e_cnt = map(int, input().split())
    graph = defaultdict(list)

    # 그래프 구성
    edges = list(map(int, input().split()))
    for i in range(e_cnt):
        graph[edges[2 * i]].append(edges[2 * i + 1])

    # 모든 노드들의 진입차수를 구해야한다.
    # 진입차수를 저장할 변수를 만들자.
    in_degree = [0] * (v_cnt + 1)

    """
    graph = {"시작정점" : 도착 정점 리스트, ..., }
    시작 정점을 기준으로 인접한 정점을 for문을 돌면서, 시작 정점을 인덱스로한 공간에 +1 씩 해준다. 
    """
    # node는 시작 정점
    for node in graph:
        # node(시작 정점)의 인접한 노드를 순회하면서, 진입 차수를 +1씩 해준다.
        for neighbor in graph[node]:
            in_degree[node] += 1

    # 진입 차수가 0인 노드들을 큐에 추가한다.
    # 진입 차수가 0 => 의존성이 없다.. 즉 먼저 실행되어야 할 노드들이다.
    # DAG 그래프는 반드시 진입 차수가 0인 노드가 존재한다.
    queue = deque()
    for i in range(1, v_cnt + 1):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    # 큐가 빌 때까지 아래 과정을 실행
    # 1. 큐에 있는 값을 꺼낸다.
    # 2. 큐와 연결된 노드들의 진입차수를 1씩 빼준다.
    # 3. 뺀 진입차수가 0이 된 노드들은 다시 큐에 집어넣는다.
    while queue:
        node = queue.popleft()
        result.append(node)

        # 인접한 노드를 순회하면서, 인접한 노드들의 진입차수를 1씩 빼준다.
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 싸이클 탐지 코드를 추가해야 한다.
    """
    1번 케이스) 아예 시작부터 진입차수가 0인 애들이 없어서, 시작조차 못하는 케이스 
    """
    if len(result) != v_cnt:
        print("싸이클 찾았습니다!")
    else:
        print(f"#{tc} ", *result)
