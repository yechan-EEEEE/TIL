import itertools

T = int(input())

for x in range(1, T + 1):
    N, K = map(int, input().split())
    M = list(map(int, input().split()))
    result = 0

    for i in range(1, N+1):
        E = list(itertools.combinations(M, i))
        sum_num = 0
        # print(E)
        for j in E:
            sum_num = sum(j)
            # print(sum_num)
            if sum_num == K:
                result += 1

    print(f'#{x} {result}')
