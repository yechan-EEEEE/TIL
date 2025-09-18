# from collections import deque
#
#
# def bfs_tree(tree, root_node):
#     queue = deque([root_node])
#     result = []
#
#     while queue:
#         node = queue.popleft()
#         result.append(node)
#         if node not in tree: continue
#         for child in tree[node]:
#             queue.append(child)
#
#     return result
#
#
# tree = {'A': ['B', 'C', 'D'],
#         'B': ['E', 'F'],
#         'D': ['G', 'H', 'I'],
#         }
#
# root_node = 'A'
# result = bfs_tree(tree, root_node)
#
# print(' '.join(result))

# from collections import deque
#
#
# def bfs(graph, start):
#
#     return result  # 최종 탐색 경로 반환
#
#
# # 그래프 인접 리스트
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A'],
#     'D': ['B', 'F'],
#     'E': ['B', 'F'],
#     'F': ['D', 'E', 'G'],
#     'G': ['F']
# }
#
# start_node = 'A'
# result = []  # 탐색 경로를 저장할 리스트
# visited = set()  # 중복 X
# queue = deque()
# queue.append(start_node)
# visited.add(start_node)  # 큐에 넣을 때 방문처리
#
# while queue:
#     vertex = queue.popleft()
#     result.append(vertex)
#
#     for neighbor in graph[vertex]:
#         if neighbor in visited:
#             continue
#         queue.append(neighbor)
#         visited.add(neighbor)
#
# print("그래프 탐색 경로:", result)  # 탐색 경로 출력

## 지도 통째로 복사하기
# from collections import deque
# import pprint
#
# dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#
#
# def get_road_move_time(road, n, m):
#     queue = deque()
#     queue.append((0, 0))
#     distance = [[-1] * m for _ in range(n)]  # 방문처리를 위한 변수, -1이면 최단거리 갱신x(방문x), -1아니면 (방문o, don't touch)
#     distance[0][0] = 0
#
#     while queue:
#         x, y = queue.popleft()
#         for dx, dy in dxy:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1 and road[nx][ny] == 1:
#                 queue.append((nx, ny))
#                 distance[nx][ny] = distance[x][y] + 1
#                 if nx == n-1 and ny == m-1:
#                     return distance[nx][ny]
#
#
# # 도로의 크기 n * m 입력 받기
# n, m = map(int, input().split())
# # 도로 정보 입력
# road = [list(map(int, input().split())) for _ in range(n)]
#
# # BFS 를 이용해서 이동시간 구하기
# result = get_road_move_time(road, n, m)
# print(result)

# from collections import deque
#
# dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#
#
# def get_road_move_time(road, n, m):
#     queue = deque()
#     queue.append((0, 0, 0))
#     road[0][0] = 0
#
#     while queue:
#         x, y, dist = queue.popleft()
#         for dx, dy in dxy:
#             nx, ny = x + dx, y + dy
#             next_dist = dist + 1
#             if 0 <= nx < n and 0 <= ny < m and road[nx][ny] == 1:
#                 queue.append((nx, ny, next_dist))
#                 road[nx][ny] = 0
#                 if nx == n-1 and ny == m-1:
#                     return next_dist
#
#
# # 도로의 크기 n * m 입력 받기
# n, m = map(int, input().split())
# # 도로 정보 입력
# road = [list(map(int, input().split())) for _ in range(n)]
#
# # BFS 를 이용해서 이동시간 구하기
# result = get_road_move_time(road, n, m)
# print(result)

from collections import deque

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(x, y, count):
    global min_count

    if x == N-1 and y == M-1:
        min_count = min(count, min_count)
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny]:
            continue
        if not road[nx][ny]:
            continue

        visited[nx][ny] = True
        dfs(nx, ny, count+1)
        visited[nx][ny] = False


# 입력 받기
N, M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
min_count = float('inf')
visited[0][0] = True

dfs(0, 0, 0)

# 도로의 크기 n * m 입력 받기
# n, m = map(int, input().split())
# # 도로 정보 입력
# road = [list(map(int, input().split())) for _ in range(n)]


# BFS 를 이용해서 이동시간 구하기
# result = dfs(N, M, road)
print(min_count)