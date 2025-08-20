import itertools

T = int(input())

for x in range(1, T + 1):
    N, K = map(int, input().split())
    N = list(map(int, input().split()))
    n = len(N)
    result = 0
    # for i in range(2, n+1):
    #     a = list(itertools.combinations(N, i))  # 이걸 2부터 N까지

    # a = list(itertools.combinations(N, 2))
    # b = list(itertools.combinations(N, 3))
    # c = list(itertools.combinations(N, 4))
    # d = list(itertools.combinations(N, 1))
    sum_num = 0
    for i in range(1, n+1):
        # a = []
        E = list(itertools.combinations(N, i))
        print(E)
    # b = list(itertools.permutations(N))
    # print(b)
    # result = 0
    # for i, j in a:
    #     print(i, j)
    #     if i + j == K:
    #         result += 1

print(f'#{x} {result}')
