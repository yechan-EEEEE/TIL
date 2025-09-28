# def get_road_move_time(road, n, m):
#     queue = deque()
#     queue.append((0, 0))
#     distance = [[-1] * m for _ in range(n)]  # 방문처리를 위한 변수, -1이면 최단거리 갱신x(방문x), -1아니면 (방문o, don't touch)
#     distance[0][0] = 0

#     while queue:
#         x, y = queue.popleft()
#         for dx, dy in dxy:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1 and road[nx][ny] == 1:
#                 queue.append((nx, ny))
#                 distance[nx][ny] = distance[x][y] + 1
#                 if nx == n-1 and ny == m-1:
#                     return distance[nx][ny]


# # 도로의 크기 n * m 입력 받기
# n, m = map(int, input().split())
# # 도로 정보 입력
# road = [list(map(int, input().split())) for _ in range(n)]

# # BFS 를 이용해서 이동시간 구하기
# result = get_road_move_time(road, n, m)
# print(result)


from collections import deque
for test in range(10):
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    T = int(input())
    size = 16
    Map = [list(map(int, input().strip())) for _ in range(size)]


    def find_route(mini_map):
        queue = deque()
        queue.append((1, 1))
        visited = [[-1] * size for _ in range(size)]
        visited[1][1] = 0

        while queue:
            x, y = queue.popleft()
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size:
                    if mini_map[nx][ny] == 3:
                        return True
                    if mini_map[nx][ny] == 0 and visited[nx][ny] == -1:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
        return False
    if find_route(Map):
        print(f'#{T} 1')
    if not find_route(Map):
        print(f'#{T} 0')
