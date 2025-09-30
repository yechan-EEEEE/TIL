# from collections import deque
# dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
#
#
# def cnt_island(world_map, x, y):
#     queue = deque()
#     queue.append((x, y))
#     world_map[x][y] = 0
#
#     while queue:
#         cx, cy = queue.popleft()
#         for dx, dy in dxy:
#             nx, ny = cx + dx, cy + dy
#
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
#
#             if world_map[nx][ny] == 0:
#                 continue
#
#             queue.append((nx, ny))
#             world_map[nx][ny] = 0
#
#
# N, M = map(int, input().split())
# islands = [list(map(int, input().strip())) for _ in range(M)]
# cnt = 0
#
# for i in range(N):
#     for j in range(M):
#         if islands[i][j] == 0:
#             continue
#
#         cnt_island(islands, i, j)
#         cnt += 1
#
# print(cnt)
#
#
# # def find_island(island, x, y):
# #     queue = deque()
# #     queue.append((x, y))
# #     island[x][y] = 0
#
# #     while queue:
# #         cx, cy = queue.popleft()
# #         for dx, dy in dxy:
# #             nx, ny = cx + dx, cy + dy
#
# #             if nx < 0 or nx >= n or ny < 0 or ny >= m:
# #                 continue
#
# #             if island[nx][ny] == 0:
# #                 continue
#
# #             queue.append((nx, ny))
# #             island[nx][ny] = 0
#
#
# # n, m = map(int, input().split())  # 섬의 크기 입력
# # arr = [list(map(int, input())) for _ in range(n)]  # 섬의 상태 입력 받기
# # island_cnt = 0  # 섬의 개수
#
# # for i in range(n):
# #     for j in range(m):
# #         if arr[i][j] == 0:
# #             continue
#
# #         find_island(arr, i, j)
# #         island_cnt += 1
#
# # print(island_cnt)  # 섬의 개수 출력


# from collections import deque
# import math
# dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
#
#
# def find_island(Map, x, y):
#     global max_cnt, min_cnt, island_species, sum_island
#     queue = deque()
#     queue.append((x, y))
#     island_species.add(Map[x][y])
#     Map[x][y] = '0'
#
#     while queue:
#         cx, cy = queue.popleft()
#         sum_island += 1
#         for dx, dy in dxy:
#             nx, ny = cx + dx, cy + dy
#             if 0 <= nx < N and 0 <= ny < M:
#                 if Map[nx][ny] == '0':
#                     continue
#                 if Map[nx][ny] != '0':
#                     find_island(Map, nx, ny)
#         max_cnt = max(sum_island, max_cnt)
#         min_cnt = min(sum_island, min_cnt)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     map_info = [list(map(str, input().split())) for _ in range(M)]
#     max_cnt = 0
#     min_cnt = math.inf
#     sum_island = 0
#     island_species = set()
#
#     for i in range(N):
#         for j in range(M):
#             if map_info[i][j] == 0:
#                 continue
#             find_island(map_info, i, j)
#     print(max_cnt, min_cnt, len(island_species)-1)
from collections import deque
import math
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (1, -1), (-1, -1)]


def find_island(Map, x, y):
    queue = deque()
    queue.append((x, y))
    island_species.add(Map[x][y])
    Map[x][y] = '0'
    size = 1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] != '0':
                queue.append((nx, ny))
                Map[nx][ny] = '0'
                size += 1
    return size


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    map_info = [input().split() for _ in range(N)]
    max_cnt = 0
    min_cnt = math.inf
    island_species = set()

    for i in range(N):
        for j in range(M):
            if map_info[i][j] == '0':
                continue
            size = find_island(map_info, i, j)
            max_cnt = max(max_cnt, size)
            min_cnt = min(min_cnt, size)

    print(max_cnt - min_cnt, len(island_species))
