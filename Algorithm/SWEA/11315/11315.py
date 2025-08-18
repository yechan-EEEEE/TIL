T = int(input())
dxy = [[0, 1], [1, 0], [1, 1], [-1, 1]]

for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(str, input().strip())) for _ in range(N)]
    found = 0  # 5개 이상 있는지 확인하는 변수
    result = []  # 결과 출력할 리스트

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'o':  # o면 탐색 시작
                for dx, dy in dxy:
                    cnt = 1  # 시작했으니 카운트 1
                    for repeat in range(1, N):  # 탐색 반복
                        cur_x = i + dx * repeat
                        cur_y = j + dy * repeat
                        if 0 <= cur_x < N and 0 <= cur_y < N and grid[cur_x][cur_y] == 'o':  # 범위 안에 있고 o면
                            cnt += 1  # 카운트 +1
                            if cnt == 5:  # 5가 되면 YES 출력하면 되니까 break
                                found = 1
                                break
                        else:  # 아니면 연속된 o가 아니니까 break하고 다음 칸 찾기
                            break
                    if found == 1:
                        break
                if found == 1:
                    break
        if found == 1:
            break

    if found == 0:
        result = 'NO'
    elif found == 1:
        result = 'YES'
    
    print(f'#{tc} {result}')