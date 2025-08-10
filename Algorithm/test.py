# def bubble_sort(arr):
#     n = len(arr)  # 리스트의 길이
#
#     # range(5) => (0, 1, 2, 3, 4) => 순회할 거에요 ,
#     # 이 for문이 진행될 때마다 최대값이 비교되면서 뒤로 가짐
#     for i in range(n):  # 리스트의 길이만큼 인덱스를 반복할 수 있다.
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# arr = [55, 7, 78, 12, 42]  # [7, 12, 42, 55, 78]
# bubble_sort(arr)
# print(arr)
# def selection_sort(arr):
#     n = len(arr) # 배열의 길이
#
#     # 첫번째 원소부터 최소값을 찾자
#     for i in range(n-1): # 최소값을 찾는 행위를 반복한다.
#         min_idx = i # 최소값의 인덱스 겸 최소값을 탐색하는 시작지점
#         for j in range(i+1,n):
#             # 현재까지의 최소값보다 작은 값이 발견되면
#             # 최소값 인덱스를 갱신한다.
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         # for문이 끝났다 = 끝까지 돌아서 최소값을 찾았다
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
# arr = [64, 25, 10, 22, 11]
# selection_sort(arr)
# print(arr)
#
# def insertion_sort(arr):
#     n = len(arr)
#     # 첫번째 요소는 이미 정렬됐다고 가정
#     # 두번째 요소부터 미정렬이라고 가정
#     # 미정렬에 있는 요소들을 정렬된 요소의 적합한 장소에 넣기
#     for idx in range(1,n):
#         # 현재 idx 요소로부터 왼쪽으로 이동하면서 비교를 시작한다.
#         for jdx in range(idx,0,-1):
#             if arr[jdx -1] > arr[jdx]: # 왼쪽 요소가 현재 요소보다 크면 위치를 바꾼다
#                 arr[jdx-1], arr[jdx] = arr[jdx], arr[jdx-1] # 서로 위치를 교환하면서 이동한다
#             else: # 왼쪽 요소가 현재 요소보다 작거나 같은 경우, 위치를 바꿨다면 그만
#                 break
# arr = [9, 5, 7, 1, 4]
# insertion_sort(arr)
# print(arr)  # [1, 4, 5, 7, 9]
#
# def counting_sort(arr, max_value):
#     n = len(arr)
#
#     # 1. 최댓값 찾기 (max_value를 파라미터로 제공하고 있음)
#     # 2. 최댓값으로 배열 초기화하기 (최댓값만큼 공간을 확보해야 한다. index error 안나려고)
#     count_arr = [0] * (max_value + 1) # 0은 개수, 초기에는 일단 0으로 초기화
#
#     # 3. 각 요소가 몇 번 나왔는지 확인하기
#     # 주어진 arr를 순회하면서, 개수를 센다. 해당 값을 인덱스로 활용해서 바로 값을 추가한다.
#     for num in arr:
#         # 해당 값을 인덱스로 활용하고, 이미 0으로 초기화 돼있기 때문에 +1
#         count_arr += 1
#     # 4.안정성을 지키기 위해 누적합 배열을 만든다. (누적합 배열: 해당 값이 들어갈 수 있는 범위)
#     for i in range(1, len(count_arr)):
#         # 이전 값을 누적해서 스스로를 갱신한다.
#         # 이전 값은 이미 이전 값들을 누적한 상태이므로 가능한 로직
#         count_arr[i] += count_arr[i - 1]
#     # 결과를 저장하기 위한 결과 배열
#     result = [0] * n
#
#     # 주어진 배열을 거꾸로 순회하면서, 누적
#     # 합 배열의 값을 이용해 값을 넣는다.
#     for i in range(n-1, -1, -1): # 역으로 순회
#         val = arr[i] # arr[i] 너무 길어서 val에다가 넣어놓고 시작
#
#         # count_arr[val] = 값을 인덱스로 활용해서 들어가야 할 위치를 찾는다
#         # count_arr[val] - 1 = 찾은 위치에서 1을 빼준다
#         # 이 값을 다시 index로 활용해서 result에 val 값을 넣어준다.
#         result[count_arr[val] - 1] = val
#
#         count_arr[val] -= 1 # 이제 한 칸을 차지해서 1을 빼준다
#     return  result
# arr = [0, 4, 1, 3, 1, 2, 4, 1]
# result = counting_sort(arr,4)
# print(result)

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
