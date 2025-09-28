from collections import deque
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]


def cnt_island(world_map, x, y):
    queue = deque()
    queue.append((x, y))
    world_map[x][y] = 0

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if world_map[nx][ny] == 0:
                continue

            queue.append((nx, ny))
            world_map[nx][ny] = 0


N, M = map(int, input().split())
islands = [list(map(int, input().strip())) for _ in range(M)]
cnt = 0

for i in range(N):
    for j in range(M):
        if islands[i][j] == 0:
            continue

        cnt_island(islands, i, j)
        cnt += 1

print(cnt)


# def find_island(island, x, y):
#     queue = deque()
#     queue.append((x, y))
#     island[x][y] = 0

#     while queue:
#         cx, cy = queue.popleft()
#         for dx, dy in dxy:
#             nx, ny = cx + dx, cy + dy

#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue

#             if island[nx][ny] == 0:
#                 continue

#             queue.append((nx, ny))
#             island[nx][ny] = 0


# n, m = map(int, input().split())  # 섬의 크기 입력
# arr = [list(map(int, input())) for _ in range(n)]  # 섬의 상태 입력 받기
# island_cnt = 0  # 섬의 개수

# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 0:
#             continue

#         find_island(arr, i, j)
#         island_cnt += 1

# print(island_cnt)  # 섬의 개수 출력
