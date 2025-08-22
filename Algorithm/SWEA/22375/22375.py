T = int(input())
for tc in range(1,T+1):
    N = int(input())
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))
    change_cnt = 0
    # print(Bi)
    for x in range(N):
        if Ai[x] != Bi[x]:
            # print(x)
            for y in range(N-x):
                Ai[x+y] = (Ai[x+y] + 1 )% 2
            change_cnt += 1
    print(f'#{tc} {change_cnt}')