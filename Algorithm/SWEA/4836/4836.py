T = int(input())

for tc in range(1, T + 1):
    grid = [[0]*10 for _ in range(10)]
    N = int(input())
    purple_num = 0
    for color_num in range(N):
        Rr1, Rc1, Rr2, Rc2, color = list(map(int, input().split()))
        # print(f'Rr1={Rr1} Rc1={Rc1} Rr2={Rr2} Rc2={Rc2} color={color}')
        for i in range(Rr1, Rr2+1):
            for j in range(Rc1, Rc2+1):  # 입력된 왼쪽위 모서리부터 오른쪽 아래 모서리까지
                # print(i, j)
                grid[i][j] += color  # color를 더해준다
                # print(f'grid[i][j]={grid[i][j]}')
    for i in range(10):
        for j in range(10):
            if grid[i][j] >= 3:  # 보라색은 빨강 + 파랑 = 3이니까 3보다 크거나 같으면 카운트
                # print(f'grid[i][j]={grid[i][j]}')
                purple_num += 1
    print(f'#{tc} {purple_num}')
