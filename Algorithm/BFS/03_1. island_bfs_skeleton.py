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


from collections import deque
import math
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (1, -1), (-1, -1)]


def find_island(Map, x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    island_species.add(Map[x][y])  # 종류 세려고 set에 입력
    Map[x][y] = '0'  # 확인한 곳은 0으로 바꿔서 pass
    cnt += 1  # 함수를 실행하면 그 곳부터 섬의 크기니까 +1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] != '0':  # 지도 안이고 0이 아니면 섬이다
                queue.append((nx, ny))
                Map[nx][ny] = '0'  # 방문했으니 0으로 처리
                cnt += 1  # 크기 +1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    map_info = [input().split() for _ in range(N)]  # map 정보
    cnt = 0  # 섬 크기 저장할 변수
    max_cnt = 0  # 제일 큰 섬 크기 저장할 변수
    min_cnt = math.inf  # 제일 작은 섬 크기 저장할 변수
    island_species = set()  # 섬 종류 저장할 변수

    for i in range(N):
        for j in range(M):
            cnt = 0  # 새로운 칸에서 시작할 때마다 크기 초기화
            if map_info[i][j] == '0':  # 0이면 섬 아니니까 pass
                continue
            find_island(map_info, i, j)  # 0이 아니면 섬이니까 함수 실행
            max_cnt = max(max_cnt, cnt)  # 함수 끝나고 max와 min 갱신
            min_cnt = min(min_cnt, cnt)

    print(f'#{tc} {max_cnt - min_cnt} {len(island_species)}')
