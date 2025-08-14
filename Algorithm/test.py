# n = 3
# m = 4
# list_1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 행 우선 순회
# for i in range(n):
#     for j in range(m):
#         print(list_1[i][j], end=" ")
#     print()

# 열 우선 순회
# for j in range(m):
#     for i in range(n):
#         print(list_1[i][j], end=" ")
#     print()

# N = 5
# matrix = [list(map(int,input().split()))for _ in range(N)]
# total_sum=0
# main_sum=0
# for i in range(N):
#   for j in range(N):
#     if i==j:
#       main_sum += matrix[i][j]
# sub_sum=0
# for i in range(N):
#     for j in range(N):
#         if i == N-1-j:
#             sub_sum+=matrix[i][j]
            
# middle_value=matrix[N//2][N//2]
# total_sum = main_sum + sub_sum - middle_value
# print(total_sum)

# N=5
# matrix = [
#     [1,  2,  3,  4,  5],
#     [6,  7,  8,  9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# total_sum  = 0
# # 모든 요소를 순회
# for i in range(N):
#     for j in range(N):
#         num_sum = 0
#         # 델타 탐색
#         for k in range(4):
#             ni = i + dx[k]  # 다음에 이동할 i 좌표
#             nj = j + dy[k]  # 다음 j 좌표

#             # ni, nj 는 범위를 벗어나면 안된다. ..
#             if 0 <= ni < N and 0 <= nj < N:
#                 # 현재 좌표의 값과 이동한 좌표의 값의 차이의 절대값
#                 num_sum += abs(matrix[i][j] - matrix[ni][nj])
#         print("여기에 오면 델타 탐색을 끝내고 다 더한 값이 저장된다.")
#         total_sum += num_sum

# N = 5 
# matrix = [
#     [9, 20, 2, 18, 11],
#     [19, 1, 25, 3, 21],
#     [8, 24, 10, 17, 7],
#     [15, 4, 16, 5, 6],
#     [12, 13, 22, 23, 14]
# ]
# # 2차원 리스트를 1차원리스트로 바꾸고 ,정렬한다
# # [1,2,3,4,5, ..., 24, 25 ]
# sorted_list = []
# for row in matrix:  # row => 행을 의미
#     for num in row:  # col => 고정된 행의 열을 의미합니다.
#         sorted_list.append(num)

# sorted_list.sort()

# # 빈 5*5 행렬을 만들어야 한다.
# # [0, 0,0,0,0] 이거를 하나 만들고, 이걸 N 번반복해서 2차원 리스트를 만들겠다.
# result = [[0] * N for _ in range(N)]
# print(result)

# # 달팽이의 운동 방향 ( 오른쪽 -> 아래 -> 왼쪽 -> 위)
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# x, y = 0, 0
# direction = 0

# # 1, 2, ,3 ,4 , ...
# # 위의 값을 순회하면서 우리가 만든 result 값에다가 채워넣을거다.
# for value in sorted_list:
#     result[x][y] = value  # 값을 채웠다.
#     # 다음 좌표로 이동한다.
#     nx = x + dx[direction]
#     ny = y + dy[direction]

#     # 조건은 벽에 부딪친다(범위를 벗어났ㅇ거나)
#     # 이미 값이 채워져있는 경우에는 방향을 바꾼다.
#     # 범위 안에 없거나... 채워져있는 곳으로 가는 경우에는
#     # 방향을 바꿔야 한다.
#     if not( 0 <= nx < N and 0 <= ny < N and result[nx][ny] == 0):
#         direction = (direction + 1) % 4  # 다음의 방향으로 바꿀 수 있다.
#         nx, ny = x + dx[direction], y + dy[direction]

#     # 현재 좌표를 이동할 좌표로 갱신해준다. ( 갈 수 있는 좌표기 때문에 갱신해도 됨)
#     x, y = nx, ny
# print(result)

# import sys
# sys.stdin = open("input.txt","r")
# T = int(input()) # 테스트케이스 입력
# for tc in range(1,T+1): # 입력 수 만큼 반복
#     N, M = list(map(int,input().split())) # 전역 크기와 파리채의 크기
#     net=[] # 전체 빈칸, 여기에 선언해야 초기화 안됌
#     for _ in range(N): # 5칸이니까 5번 반복 입력
#       fly = list(map(int,input().split())) # 파리들 칸마다 수 입력 받고
#       net.append(fly) # net에다 입력, extend는 나눠서 하나씩 넣는거라 append로 한번에 넣어야함
#       # print(net)
#     max_kill = 0 # 최대 킬 수
#     for i in range(N-M+1): # 파리채가 범위 밖으로 나가면 안되니까 반복횟수 설정
#        for j in range(N-M+1): # 위와 같음
#           sum_kill = 0
#           for m in range(M): # 행
#              for n in range(M): #열
#                 sum_kill+=net[i+m][i+n] # 순서대로 자기자리,우,하,하우 4자리 더하기
#           max_kill=max(sum_kill,max_kill) # 때리기가 끝날 때마다 최대킬이랑 방금 때린 값 비교해서 큰 값 저장
#     print(f'#{tc} {max_kill}')


# import sys
# sys.stdin = open("input.txt","r")
# T = int(input())
# for tc in range(1,T+1):
#     N, M = list(map(int,input().split()))
#     net = [list(map(int,input().split())) for _ in range(N)]
#     # net = []
#     # for _ in range(N):
#     #     fly = list(map(int,input().split()))
#     #     net.append(fly)
#     max_kill=0
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             sum_kill=0
#             for n in range(M):
#                 for m in range(M):
#                     sum_kill+=net[i+n][j+m]
#             max_kill=max(sum_kill,max_kill)
#     print(f'#{tc} {max_kill}')

'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
v 1 2 3 4 5

이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
답은 12와 6의 차인 6을 출력한다.

입력
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

출력
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력                                                                                                      출력
3                       T
10 3                    N이 정수의 개수 M이 이웃한 값들 몇개를 더할 건가
1 2 3 4 5 6 7 8 9 10                                                                                    #1 21
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821                                                        #2 11088
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176     #3 1090


'''

# T = int(input())
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     ai = list(map(int, input().split()))
#     first_num = 0
#     for k in range(M):
#         first_num += ai[k]
#     max_num = first_num
#     min_num = first_num
#     # max_num = 0
#     # min_num = 10000 * M
#     for i in range(N-M+1):
#         sum_num = 0
#         for j in range(M):
#             sum_num += ai[i+j]
#         max_num = max(sum_num, max_num)
#         min_num = min(sum_num, min_num)
#     result = max_num - min_num
#     print(f'#{tc} {result}')
#
# dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
# N = [[2, 1, 1, 2, 2], [2, 2, 1, 2, 2], [2, 2, 1, 1, 2]]
# # print(dxy[0])
# # print(dxy[0][0])
# # for dx, dy in dxy:
# #     print(dx, end=' ')
# #     print(dy)
# print(dxy[3])
# print(N[0][4])
# N=3
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,10]
# ]

# result = []

# # 각 행의 합을 result에 더할건데
# # 조건: 홀수 행만 넣으세요 ( [1,2,3], [7,8,10] ) 행의 합을 넣으세요
# # result => [6, 25 ]
# for i in range(N):
#     if i % 2 == 1:
#         continue
#     line_sum = 0
#     for j in range(N):
#         if i == 1:
#             break
#         line_sum += matrix[i][j]
#     result.append(line_sum)
# print(result)
# dxy = [(-1,0), (1,0), (0,-1), (0,1)]  # 상, 하, 좌, 우
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     grid = [list(map(int, input().split())) for _ in range(N)]
#     high_num = max(map(max, grid))
#     max_path_len = 0
#
#     for i in range(N):
#         for j in range(N):
#             if grid[i][j] == high_num:
#                 x, y = i, j
#                 path_len = 1
#
#                 # 최대 N*N번 반복, 이동 불가 시 break
#                 for _ in range(N*N):
#                     cur_height = grid[x][y]
#                     next_x, next_y = -1, -1
#                     next_height = cur_height
#
#                     for dx, dy in dxy:
#                         nx, ny = x + dx, y + dy
#                         if 0 <= nx < N and 0 <= ny < N:
#                             if grid[nx][ny] < next_height:
#                                 next_height = grid[nx][ny]
#                                 next_x, next_y = nx, ny
#                                 break  # 이동할 곳은 유일
#
#                     if next_x == -1:  # 이동할 곳 없으면 종료
#                         break
#
#                     x, y = next_x, next_y
#                     path_len += 1
#
#                 max_path_len = max(max_path_len, path_len)
#
#     print(f"#{tc} {max_path_len}")
