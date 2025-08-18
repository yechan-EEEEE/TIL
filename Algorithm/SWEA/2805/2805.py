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


T = int(input())

for tc in range(1, T +1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]
    total_sum = 0
    center = N // 2

    for i in range(N):
        d = abs(i - center)
        for j in range(d, N - d):
            total_sum += grid[i][j]
    print(f'#{tc} {total_sum}')