T = int(input())
for tc in range(1,T+1):
    N = int(input())
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))
    change_cnt = 0
    Ci = Ai
    # print(Bi)
    # print(Ci)
    for x in range(N):
        if Ci[x] != Bi[x]:
            # print(x)
            for y in range(N-x):
                Ci[x+y] = (Ci[x+y] + 1 )% 2
                # print((Ci[x] + 1 )% 2)
                # print(Ci)
            change_cnt += 1
    print(f'#{tc} {change_cnt}')