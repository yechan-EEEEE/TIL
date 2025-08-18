# dxy = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     grid = [list(map(int,input().split())) for _ in range(N)]
#     max_kill = 0
#     for i in range(N) :
#         for j in range(N):
#             cross_kill = grid[i][j]
#             for dx, dy in dxy[:4]:
#                 for power in range(1, M):
#                     cx = i + dx * power
#                     cy = j + dy * power
#                     if 0 <= cx < N and 0 <= cy < N:
#                         cross_kill += grid[cx][cy]
#             x_kill = grid[i][j]
#             for dx, dy in dxy[4:]:
#                 for power in range(1, M):
#                     cx = i + dx * power
#                     cy = j + dy * power
#                     if 0 <= cx < N and 0 <= cy < N:
#                         x_kill += grid[cx][cy]
#             max_kill = max(max_kill, cross_kill, x_kill)
#     print(f'#{tc} {max_kill}')

# T = int(input())
# dxy = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, -1], [-1, 1]]

# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     flies = [list(map(int, input().split())) for _ in range(N)]
#     max_kill = 0

#     for i in range(N):
#         for j in range(N):
#             cross_kill = flies[i][j]
#             for dx, dy in dxy[:4]:
#                 for power in range(1, M):
#                     cx = i + dx * power
#                     cy = j + dy * power
#                     if 0 <= cx < N and 0 <= cy < N:
#                         cross_kill += flies[cx][cy]
#             x_kill = flies[i][j]
#             for dx, dy in dxy[4:]:
#                 for power in range(1, M):
#                     cx = i + dx * power
#                     cy = j + dy * power
#                     if 0 <= cx < N and 0 <= cy < N:
#                         x_kill += flies[cx][cy]
#             max_kill = max(max_kill, cross_kill, x_kill)
#     print(f'#{tc} {max_kill}')

T = int(input())
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

for tc in range(1, T + 1):

    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N):
        for j in range(N):
            cross_kill = flies[i][j]
            for dx, dy in dxy[:4]:
                for power in range(1, M):
                    cx = i + dx * power
                    cy = j + dy * power
                    if 0 <= cx < N and 0 <= cy < N:
                        cross_kill += flies[cx][cy]
            x_kill = flies[i][j]
            for dx, dy in dxy[4:]:
                for power in range(1, M):
                    cx = i + dx * power
                    cy = j + dy * power
                    if 0 <= cx < N and 0 <= cy < N:
                        x_kill += flies[cx][cy]
            max_kill = max(max_kill, cross_kill, x_kill)
    print(f'#{tc} {max_kill}')