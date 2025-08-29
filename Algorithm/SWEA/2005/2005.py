# print(1)
# print(1, 1)
# print(1, 2, 1)
# print(1, 3, 3, 1)

# T = int(input())
# for i in range(1, T + 1):

#     N = int(input())
#     l1 = [1, 1]
#     for i in range(3, N + 1):
#         result = [0] * i
#         for j in range(i):
#             result[j+1] = l1[j] + l1[j+1]
t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]  # 2차원 리스트 하고 방마다 크기만큼 늘려놨네
    arr[0][0] =1  # 맨 앞은 무조건 1
 
    for i in range(1,n):  # 1부터 n까지 n까지인 이유는 맨 앞은 1로 정해져 있으니까
        for j in range(0,i+1):  # 
            if 0 <= i-1 < n and 0 <= j-1 < n:  # i-1이 자기보다 1 작았을 때 값이고 j-1이 자기 아래칸에 앞에 거고
                arr[i][j] += arr[i-1][j-1]  # 그 칸에 값이 존재하면 더해주기
            if 0 <= i-1 < n and 0 <= j < n :  # j는 자기 바로 위칸이구나
                arr[i][j] += arr[i-1][j]
     
    print(f'#{test_case}')
    for i in range(0,n):  # 4면 4번 출력
        for j in range(0,n):  # 자기 숫자만큼 원소 갯수 출력
            if arr[i][j] > 0:  # 0인 칸은 출력 안하기
                print(arr[i][j], end = " ")  # end로 띄어쓰기
        print()