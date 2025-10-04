

# def bino(n, k):
#     B = [[0 for _ in range(k + 1)] for _ in range(n + 1)] 

#     for i in range(n + 1):
#         for j in range(min(i, k) + 1):
#             if j == 0 or j == i:
#                 B[i][j] = 1
#             else:
#                 B[i][j] = B[i - 1][j - 1] + B[i - 1][j]  

#     return B[n][k]


# T = int(input())
# for tc in range(1, T + 1):
#     n, a, b = map(int, input().split())

#     result = bino(n, a)
#     print(f'#{tc} {result}')


def brute_force(text, pattern):
    M, N = len(text), len(pattern)

    i, j = 0, 0

    while i < M and j < N:
        if text[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == N:
        return 1
    else:
        return 0
    
T = int(input())
for tc in range(1, T + 1):
    str1 = str(input())
    str2 = str(input())
    result = brute_force(str2, str1)

    print(f'#{tc} {result}')
