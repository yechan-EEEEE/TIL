
T = int(input())

dxy = [[1, 0], [-1, 0], [0, -1], [0, 1]]
for tc in range(1, T + 1):
    N = int(input())
    map_height = [list(map(int, input().split())) for _ in range(N)]

    highest_height = 0
    for x in range(N):
        for y in range(N):
            if map_height[x][y] > highest_height:
                highest_height = map_height[x][y]
                
    max_mov = 0
    for i in range(N):
        for j in range(N):
            if map_height[i][j] == highest_height:
                x, y = i, j
                mov_cnt = 1
                while True:
                    min_height = map_height[x][y]
                    next_x, next_y = -1, -1
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy 
                        if 0 <= nx < N and 0 <= ny < N and map_height[nx][ny] < min_height:
                            min_height = map_height[nx][ny]
                            next_x, next_y = nx, ny
                    if next_x == -1:
                        break
                    x, y = next_x, next_y
                    mov_cnt += 1        
                max_mov = max(max_mov, mov_cnt)
    print(f'#{tc} {max_mov}')
