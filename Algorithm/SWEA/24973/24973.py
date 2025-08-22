
T = int(input())

dxy = [[1, 0], [-1, 0], [0, -1], [0, 1]]
for tc in range(1, T + 1):
    N = int(input())
    map_height = [list(map(int, input().split())) for _ in range(N)]
    highest_height = 0
    max_mov = 0
    for x in range(N):
        for y in range(N):
            if map_height[x][y] > highest_height:
                highest_height = map_height[x][y]
    print(f'high={highest_height}')
    for i in range(N):
        mov_cnt = 1
        for j in range(N):
            if map_height[i][j] == highest_height:
                lowest_test = 1
                while lowest_test == 1:
                    min_height = map_height[i][j]
                    for dx, dy in dxy:
                        nx = i + dx
                        ny = j + dy
                        print(f'min={min_height}')
                        if 0 <= nx < N and 0 <= ny < N and map_height[nx][ny] < min_height:
                            min_height = map_height[nx][ny]
                            # print(f'min={min_height}')
                    if min_height == map_height[i][j]:
                        lowest_test -= 1
                    mov_cnt += 1
                    i, j = nx, ny

        max_mov = max(max_mov, mov_cnt)
    print(f'#{tc} {max_mov}')




