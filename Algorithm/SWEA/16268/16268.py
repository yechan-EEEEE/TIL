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
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    dust = [list(map(int, input().split())) for _ in range(N)]  # 꽃가루 들어간 풍선들
    max_num = 0  # 터뜨렸을 때 최대값
    # 행 우선 순회
    for i in range(N):
        for j in range(M):
            sum_num = dust[i][j]  # 자기 자리 더해야하니까 여기다 해주고
            # print(sum_num)
            for dx, dy in dxy:  # 이렇게 하면 반복문에 -1,0 / 1,0 / 0,-1 / 0,1 이 들어가요
                # print(dx, dy)
                if 0 <= i+dx < N and 0 <= j+dy < M:  # 범위 밖이면 더하지 말아야 하니까 범위 정해주고
                    # print(sum_num)
                    # print(dust[i+dx][j+dy])
                    sum_num += dust[i+dx][j+dy]  # 상하좌우 움직이는 값을 sum_num 에 더해주고
                    # print(sum_num)
                    max_num = max(max_num, sum_num)  # 최대값이랑 sum_num 이랑 비교해서 최대값 갱신해요
                    # print(max_num)
    print(f'#{test_case} {max_num}')




