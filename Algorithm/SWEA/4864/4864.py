

def bruteforce_match(p, t):
    M = len(p)
    N = len(t)

    i = j = 0

    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == M:
        return 1
    else:
        return 0


T = int(input())

for tc in range(1, T + 1):

    str1 = str(input().strip())
    str2 = str(input().strip())
    result = bruteforce_match(str1, str2)
    print(result)


    # N = len(str1)
    # M = len(str2)
    # max_sum = 0
    #
    # for i in range(M-N+1):
    #     cur_sum = 0
    #     for j in range(N):
    #         if str1[j] == str2[i+j]:
    #             cur_sum += 1
    #             if cur_sum == N:
    #                 max_sum += 1
    # print(f'#{tc} {max_sum}')
