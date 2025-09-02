# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     grid = [list(map(int, input().strip())) for _ in range(N)]

#     total_sum = 0
#     center = N // 2

#     for i in range(N):
#         coord = abs(i - center)
#         for j in range(coord, N - coord):
#             total_sum += grid[i][j]

#     print(f'#{tc} {total_sum}')



# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     grid = [list(map(int, input().strip())) for _ in range(N)]

#     total_sum = 0
#     center = N // 2

#     for i in range(N):
#         coord = abs(i - center)
#         for j in range(coord, N - coord):
#             total_sum += grid[i][j]
    
#     print(f'#{tc} {total_sum}')


# T = int(input())

# for tc in range(1, T +1):
#     N = int(input())
#     grid = [list(map(int, input().strip())) for _ in range(N)]
#     total_sum = 0
#     center = N // 2

#     for i in range(N):
#         d = abs(i - center)
#         for j in range(d, N - d):
#             total_sum += grid[i][j]
# #     print(f'#{tc} {total_sum}')
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     grid = [list(map(int,input().strip())) for _ in range(N)]
#     total_sum = 0
#     center = N // 2
#
#     for i in range(N):
#         painted = abs(i-center)
#         for j in range(painted, N-painted):
#             total_sum += grid[i][j]
#     print(f'#{tc} {total_sum}')





T = int(input())

for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]
    center = N // 2  # 중간값
    sum_value = 0  # 농작물 가치 더한 값

    for i in range(N):
        start_point = abs(center - i)
        for j in range(start_point, N-start_point):
            sum_value += grid[i][j]
    print(f'#{t} {sum_value}')

# # 15:44

test = int(input())
for t in range(1, test+1):
    n = int(input())
    box = [list(map(int, input())) for _ in range(n)]
    num = 0
    l = n//2
    middle_sum = sum(box[l][0:])
    for i in range(l+1):
        num += sum(box[l-i][0+i:n-i])  # up
        num += sum(box[l+i][0+i:n-i])  # down
    num -= middle_sum
    print(f"#{t} {num}")

































