T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    result = 0

    if N > M:
        N, M = M, N
        Ai, Bj = Bj, Ai

    for i in range(M - N + 1):
        cur_sum = 0
        for j in range(N):
            cur_sum += Ai[j] * Bj[i+j]
        result = max(result, cur_sum)
    
    print(f'#{tc} {result}')
