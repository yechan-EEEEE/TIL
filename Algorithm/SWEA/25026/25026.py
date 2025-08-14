
T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    score_num = list(map(int, input().split()))
    max_team = 0
    score_num.sort()
    score_num.reverse()
    # print(score_num)
    for i in range(N):
        cur_team = 1
        for j in range(1, N-i):
        # print(N)
        # print(i+1)
        # print(score_num[i], score_num[i+1])
            if i+j < N:
                a = score_num[i] - score_num[i+j]
                # print(i, a)
                if a <= K:
                    cur_team += 1
                    # print(cur_team)
        max_team = max(max_team, cur_team)
        # print(max_team)

    print(f'#{tc} {max_team}')