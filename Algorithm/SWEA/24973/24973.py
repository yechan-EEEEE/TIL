
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
            if map_height[i][j] == highest_height:  # 처음부터 쭉 돌다가 최고 높이면 시작
                x, y = i, j  # 아래 코드에서 i랑 j로 돌면 코드가 꼬여서 새로 지정
                mov_cnt = 1  # 현재 위치도 이동으로 치니까 1로 시작
                while True:
                    next_x, next_y = -1, -1  # 다음에 움직일 좌표를 저장할 변수, 종료 조건을 위해서 -1로 둠
                    min_height = map_height[x][y]  # 지금 위치를 가장 낮은 높이로 시작해서
                    for dx, dy in dxy:  # 4 방향을 전부 탐색
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and map_height[nx][ny] < min_height:  # 4 방향중 가장 낮은 곳을 찾는 곳
                            min_height = map_height[nx][ny]  # min_height를 가장 낮았던 높이로 갱신해주고
                            next_x, next_y = nx, ny  # 다음에 움직일 좌표를 지금 nx, ny로 갱신
                    if next_x == -1:  # 만약에 다음 움직일 좌표들이 내 자리보다 커서 좌표값이 변하지 않았다면 종료
                        break
                    x, y = next_x, next_y  # 좌표가 바뀌었으면 위치를 옮겨주고 카운트 +1
                    mov_cnt += 1        
                max_mov = max(max_mov, mov_cnt)  # while이 종료 됐을 때 최고높이인 곳이 또 있을 수 있으니 여기서 max
    print(f'#{tc} {max_mov}')
