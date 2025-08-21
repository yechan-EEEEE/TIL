T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    sum_num = [0]*5000
    # print(sum_num)
    bus_stop = []
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A-1, B):
            sum_num[i] += 1
            # print(sum_num)
        # sum_num[A-1:B] += 1
    P = int(input())
    for i in range(P):
        C = int(input())
        bus_stop.append(sum_num[C-1])
        # print(result, sum_num[C-1])
    result = (" ".join(map(str, bus_stop)))
    print(f'#{tc} {result}')
