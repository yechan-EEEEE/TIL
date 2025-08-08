'''
종이 꽃가루가 들어있는 풍선이 NxM 크기의 격자판에 붙어있는데, 어떤 풍선을 터뜨리면 상하좌우의 풍선이 추가로 터진다고 한다.

다음의 경우 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.

NxM개의 풍선에 들어있는 종이 꽃가루 개수 A가 주어지면, 한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최대값을 출력하는 프로그램을 만드시오.

(3 <= N, M <= 100)

입력

첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M, 이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.

출력

# 과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력한다.

입력                     출력
3
3 5
2 1 1 2 2
2 2 1 2 2
2 2 1 1 2               #1 8
5 5
3 4 1 2 3
3 4 1 3 2
2 3 2 4 1
1 4 4 1 3
2 2 3 4 4               #2 16
5 8
1 3 4 4 4 4 3 3
4 1 2 4 3 1 4 4
4 1 4 4 1 4 2 1
3 2 4 2 1 1 2 1
4 4 1 4 4 2 2 2         #3 17

'''

# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = list(map(int,input().split())) # 행, 열의 수를 입력 받아요
#     dust = [] #꽃가루 들어갈 빈 방
#     for x in range(N): # 행의 수만큼 반복해요
#         a = list(map(int,input().split())) # 입력한 숫자를 쭈루룩 받아놓고
#         dust.append(a) # 각 행에다 입력해줘요
#         # arr = [list(map(int,input().split())) for - in range(N)]
#     dx = [0,0,1,-1] # 오른쪽, 왼쪽, 아래, 위 값들
#     dy = [1,-1,0,0]
#     max_num = 0 # 다 더했을 때 최고 값 0으로 만들어두기
#     for i in range(0,N): # 행의 수만큼 반복
#         sum_num=0 # 여기다 이번에 터뜨렸을 때 총합을 넣을거에요
#         for j in range(0,M): # 열의 수만큼 반복
#             sum_num += dust[i][j]# 이제 더해줘야 하는데 여길 어떻게 쓸까요?
#             sum_num += dust[i+dx[i]][j+dy[j]]
#             sum_num += dust[]


'''
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int,input().split())) # 행, 열의 수를 입력 받아요
    dust = [] #꽃가루 들어갈 빈 방
    for x in range(0,N): # 행의 수만큼 반복해요
        a = list(map(int,input().split())) # 입력한 숫자를 쭈루룩 받아놓고
        dust.append(a) # 각 행에다 입력해줘요
    dx = [0,0,1,-1] # 오른쪽, 왼쪽, 아래, 위 값들
    dy = [1,-1,0,0]
    max_num = 0 # 다 더했을 때 최고 값 0으로 만들어두기
    for i in range(0,N): # 행의 수만큼 반복
        for j in range(0,M): # 열의 수만큼 반복
            sum_num=0 # 여기다 이번에 터뜨렸을 때 총합을 넣을거에요
            sum_num = dust[i][j]# 이제 더해줘야 하는데 여길 어떻게 쓸까요?
            sum_num += dust[i+dx[i]][j+dy[j]]
            sum_num += dust[]




    # 꽃가루의 합 중에서 최대값이 가장 큰 값을 저장할 변수
    max_value = 0

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

T = int(input())
for tc in range(1, T+1):
    # N = 행의 개수 , M = 열의 개수
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 꽃가루의 합 중에서 최대값이 가장 큰 값을 저장할 변수
    max_value = 0

    # 모든 풍선을 순회하고, 터트려본다..
    for i in range(N):  # 행
        for j in range(M):  # 열
            # i, j에서 풍선을 터트렸을 때, 발생하는 꽃가루를 저장할 누적 변수를만들어야 함
            temp_sum = arr[i][j]  # 본인 꽃가루도 포함하기 떄문에 바로 포함해서 초기화

            # 기준점 잡았으니 델타 탐색 시작하자.
            # for k in range(4):
            #     x = dx[k]
            #     y = dy[k]

            #        오른쪽   왼쪽     아래      위
            # dxy =[[0, 1], [0, -1], [1, 0], [-1, 0]]
            # 처음에 for 문 돌때 [0, 1] => [dx, dy]
            # dx : 0, dy: 1 => 오른쪽
            for dx, dy in dxy:
                # 각 방향으로 한 번만 탐색 X , 몇 번탐색 해야한다 ?? => 꽃가루 개수만큼(arr[i][j])
                for dist in range(1, arr[i][j] + 1):  # arr[i][j] => 1 일 경우에는, 그대로 dist 1밖에 실행 안된다.
                    # 델타탐색으로 다음에 이동할 좌표
                    ni = i + dx * dist
                    nj = j + dy * dist

                    # 범위를 벗어날 거에요..
                    # 꽃가루의 누적은 범위 안에 있는 애들한테만 해당한다. .
                    if 0 <= ni < N and 0 <= j < M:
                        temp_sum += arr[ni][nj]
                    else:  # 범위를 벗어난 경우
                        break

            max_value = max(max_value, temp_sum)

    print(f"#{tc} {max_value}")

            #        오른쪽   왼쪽     아래      위
            # dxy =[[0, 1], [0, -1], [1, 0], [-1, 0]]
            # 처음에 for 문 돌때 [0, 1] => [dx, dy]
            # dx : 0, dy: 1 => 오른쪽
            for dx, dy in dxy:
                # 각 방향으로 한 번만 탐색 X , 몇 번탐색 해야한다 ?? => 꽃가루 개수만큼(arr[i][j])
                for dist in range(1, arr[i][j] + 1):  # arr[i][j] => 1 일 경우에는, 그대로 dist 1밖에 실행 안된다.
                    # 델타탐색으로 다음에 이동할 좌표
                    ni = i + dx * dist
                    nj = j + dy * dist

                    # 범위를 벗어날 거에요..
                    # 꽃가루의 누적은 범위 안에 있는 애들한테만 해당한다. .
                    if 0 <= ni < N and 0 <= j < M:
                        temp_sum += arr[ni][nj]
                    else:  # 범위를 벗어난 경우
                        break

            max_value = max(max_value, temp_sum)

    print(f"#{tc} {max_value}")
'''
N, M = list(map(int, input().split()))
arr = [list(map(int,input().split())) for - in range(N)]