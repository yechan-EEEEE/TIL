import sys
sys.stdin = open("input.txt", "r")

# dxy = [[0, -1], [0, 1], [-1, 0]]
# for _ in range(1, 11):
#     tc = int(input())
#     N = 100
#     ladder = [list(map(int, input().split())) for _ in range(N)]
#     start_point = 0
#     for i in range(N):
#         if ladder[N-1][i] == 2:
#             start_point = i
#     i, j = N - 1, start_point
#     while i > 0:
#         for dx, dy in dxy:
#             nx = i + dx
#             ny = j + dy
#             if 0 <= nx < N and 0 <= ny < N and ladder[nx][ny] == 1:
#                 ladder[nx][ny] = 0
#                 i, j = nx, ny
#                 break
#     print(f'#{tc} {j}')

dxy = [[0, -1], [0, 1], [-1, 0]]
for _ in range(10):
    tc = int(input())
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]
    start_point = 0
    for i in range(N):
        if ladder[N-1][i] == 2:
            start_point = i
    i, j = N - 1, start_point
    while i > 0:
        for dx, dy in dxy:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < N and 0 <= ny < N and ladder[nx][ny] == 1:
                ladder[nx][ny] = 0
                i, j = nx, ny
                break
    print(f'#{tc} {j}')
