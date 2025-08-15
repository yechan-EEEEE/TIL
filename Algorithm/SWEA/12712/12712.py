'''
입력                    출력
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
                        #1 64
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29
                        #2 157
'''
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]
    max_kill = 0
    for i in range(N) :
        for j in range(N):
            cross_kill = grid[i][j]
            for dx, dy in dxy[:4]:
                for power in range(1, M):
                    cx = i + dx * power
                    cy = j + dy * power
                    if 0 <= cx < N and 0 <= cy < N:
                        cross_kill += grid[cx][cy]
            x_kill = grid[i][j]
            for dx, dy in dxy[4:]:
                for power in range(1, M):
                    cx = i + dx * power
                    cy = j + dy * power
                    if 0 <= cx < N and 0 <= cy < N:
                        x_kill += grid[cx][cy]
            max_kill = max(max_kill, cross_kill, x_kill)
    print(f'#{tc} {max_kill}')