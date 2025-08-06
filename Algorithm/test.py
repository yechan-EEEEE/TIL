# def bubble_sort(arr):
#     # 패스를 확인을 했어야 했다.
#
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
#
# # print(arr)  # [7, 12, 42, 55, 78]
#
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
n = 3
m = 4
list_1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
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

'''
total_sum=0
main_sum=0
for i in range(N)
  for j in range(N)
    if i==j:
      main_sum += matrix[i][j]
sub_sum=0
for i in range(N):
    for j in range(N):
        if i == N-1-j:
            sub_sum+=matrix[i][j]
            
middle_value=matrix[N//2][N//2}
'''