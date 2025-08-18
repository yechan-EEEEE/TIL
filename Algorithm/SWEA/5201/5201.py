T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    wi.sort()
    wi.reverse()
    ti.sort()
    ti.reverse()
    # print(f'wi{wi}')
    # print(f'ti{ti}')
    max_w = 0
    prev_con = 0

    for i in range(M):
        if prev_con >= N:
            break
        if wi[prev_con] <= ti[i]:
            max_w += wi[prev_con]
            prev_con += 1
        else:
            prev_con += 1
            if prev_con < N and wi[prev_con] <= ti[i]:
                max_w += wi[prev_con]
                prev_con += 1
                
    print(f'#{tc} {max_w}')