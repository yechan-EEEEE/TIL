'''

종이 꽃가루가 들어있는 풍선이 M개씩 N개의 줄에 붙어있고,
어떤 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임이 있다.
예를 들어 풍선에 든 꽃가루가 1개씩일 때, 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.
NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면,
한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력하는 프로그램을 만드시오.

(3<=N, M<=100)

입력
첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M, 이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.

출력
#과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력한다.

입력                    출력

3
3 5
2 1 1 2 2 
2 2 1 2 2 
2 2 1 1 2               #1 10
5 5
3 4 1 2 3 
3 4 1 3 2 
2 3 2 4 1 
1 4 4 1 3 
2 2 3 4 4               #2 26
5 8
1 3 4 4 4 4 3 3 
4 1 2 4 3 1 4 4 
4 1 4 4 1 4 2 1 
3 2 4 2 1 1 2 1 
4 4 1 4 4 2 2 2         #3 40

'''

# dxy = [[1, 0], [-1, 0], [0, -1], [0, 1]]
# T = int(input())
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     dust = [list(map(int, input().split())) for _ in range(N)]
#     max_num = 0
#     for i in range(N):
#         for j in range(M):
#             sum_num = dust[i][j]

# dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_value = 0
#     for i in range(N):  # 행
#         for j in range(M):  # 열
#             temp_sum = arr[i][j]  # 본인 꽃가루도 포함하기 떄문에 바로 포함해서 초기화
#             for dx, dy in dxy:
#                 # 각 방향으로 한 번만 탐색 X , 몇 번탐색 해야한다 ?? => 꽃가루 개수만큼(arr[i][j])
#                 for dist in range(1, arr[i][j] + 1):  # arr[i][j] => 1 일 경우에는, 그대로 dist 1밖에 실행 안된다.
#                     # 델타탐색으로 다음에 이동할 좌표
#                     ni = i + dx * dist
#                     nj = j + dy * dist
#
#                     # 범위를 벗어날 거에요..
#                     # 꽃가루의 누적은 범위 안에 있는 애들한테만 해당한다. .
#                     if 0 <= ni < N and 0 <= nj < M:
#                         temp_sum += arr[ni][nj]
#                     else:  # 범위를 벗어난 경우
#                         break
#
#             max_value = max(max_value, temp_sum)
#
#     print(f"#{tc} {max_value}")


# dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# T = int(input())
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     grid = [list(map(int, input().split())) for _ in range(N)]
#     max_sum = 0  # 터뜨린 최대 값
#     for i in range(N):  # 행
#         for j in range(M):  # 열
#             cur_sum = grid[i][j]  # 현재 더한 값=자기 위치 값도 더해줘야 하니까 이렇게 해두고
#             for dx, dy in dxy:  # 델타탐색을 시작합니다
#                 for dist in range(1, grid[i][j]+1):  # 탐색을 반복합니다, 현재 위치 값만큼
#                     cx = i+dx * dist
#                     cy = j+dy * dist
#                     if 0 <= cx < N and 0 <= cy < M:
#                         cur_sum += grid[cx][cy]
#                     else:
#                         break
#             max_sum = max(max_sum, cur_sum)
#     print(f'#{tc} {max_sum}')


































