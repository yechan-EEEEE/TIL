T = int(input())
dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for tc in range(1, T + 1):
    N = int(input())
    Hij = [list(map(int, input().split())) for _ in range(N)]
    max_mov = 0
    
    for i in range(N):
        for j in range(N):
            x, y = i, j
            mov_cnt = 1  # 첫 걸음도 이동으로 쳐서 1
            while True:
                min_H = Hij[x][y]  # 자기 위치를 가장 낮은곳이라고 치고
                next_x, next_y = -1, -1  # 다음 칸으로 움직이기 위한 변수
                for dx, dy in dxy:  # 4방향 델타탐색
                    nx, ny = x + dx, y + dy
                    # 범위 안이면서 4 방향중 가장 작은 값 min_H에 저장
                    if 0 <= nx < N and 0 <= ny < N and min_H > Hij[nx][ny]:
                        next_x, next_y = nx, ny  # 가장 작은 값의 x, y 좌표를 저장
                        min_H = Hij[nx][ny]
                if next_x == -1:  # 현재 위치가 가장 낮아서 좌표가 변하지 않았다면 종료
                    break
                mov_cnt += 1  # 다음 칸으로 움직이면서 카운트를 1 증가
                x, y = next_x, next_y
            max_mov = max(max_mov, mov_cnt)
    print(f'#{tc} {max_mov}')