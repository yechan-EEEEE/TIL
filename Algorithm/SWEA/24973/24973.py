"""
N x N 크기의 2차원 지도 정보가 주어집니다. 각 칸에는 해당 지역의 고유한 고도(높이)를 나타내는 숫자가 적혀 있습니다.

당신은 주어진 지도 정보에서 가장 높은 곳에서 출발하여 탐험을 시작합니다. 탐험은 상, 하, 좌, 우 네 방향으로만 이동할 수 있으며,
현재 있는 칸의 인접한 칸 중 가장 낮은 곳으로만 이동할 수 있습니다. 인접한 칸 중 가장 낮은 곳은 2군데 이상이 될 수 없음을 보장합니다.
시작 지점부터 규칙에 따라 더 이상 이동할 수 없을 때까지 움직였을 때, 당신이 방문한 총 칸의 개수를 구하는 프로그램을 작성하세요.
방문한 칸의 개수에는 시작 지점도 포함됩니다.

입력

첫 번째 줄에 지도의 크기 N이 주어집니다. (3 ≤ N ≤ 100)
두 번째 줄부터 N개의 줄에 걸쳐 각 칸의 고도 정보가 공백으로 구분되어 주어집니다. (1 ≤ 고도 ≤ 1,000)


출력

규칙에 따라 최대로 이동했을 때, 방문한 총 칸의 개수를 출력합니다.

입력                      출력
3
5
20 19 18 17 16
15 14 13 12 11
4  5  6  7  10
3  2  1  8  9
6  7  8  9  10
                          #1 6
4
50 49 48 30
10 12 13 29
11 15 16 28
50 45 46 27
                          #2 3
5
40 39 38 37 36
30 25 24 23 35
29 20 10 22 34
28 19 12 18 33
27 26 13 14 32
                          #3 5
"""
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    print(grid)
    high_num = 0  # 가장 높은 곳의 값
    start_x = 0  # 가장 높은 곳의 위치
    start_y = 0
    for x in range(N):  # 최고값 찾기
        for y in range(N):
            if grid[x][y] > high_num:
                high_num = grid[x][y]
                start_x = x
                start_y = y
    
    cur_num = high_num  # 현재 위치 값을 최고 위치로 설정
    max_mov = 0  # 최대 이동 값
    for i in range(N):  # 순회 시작
        for j in range(N):
            if grid[i][j] == high_num:  # 그 칸이 가장 높은 곳이면 이동시작
                for dx, dy in dxy:
                    # print(dx, dy)
                    mov_num = 0
                    # print(grid[i+dx][j+dy])
                    if 0 <= i+dx < N and 0 <= i+dy < N:  # 움직일 위치가 범위 밖으로 나가지 않으면 이동
                        # print(grid[i+dx][j+dy])
                        # print(cur_num)
                        for k in range(N):  # cur_num 이 주변 값들보다 제일 작을 때까지반복 을 못하겠네요
                            if [i+dx][j+dy] < cur_num:  # 움직일 곳의 값이 지금 위치값보다 작으면 이동
                                cur_num = grid[i+dx][j+dy]  # 이동 했으면 현재 위치를 그 값으로 바꿈
                                print(cur_num)
                                mov_num += 1  # 이동 했으니까 이동값에 1 더하기
                                max_mov = max(max_mov, mov_num)  # 2개 비교해서 더 큰 값 max 에 넣기(같은 값 2개면 비교해야 하니까)
                # print(max_mov)
    result = max_mov+1
    print(f'#{tc} {result}')
