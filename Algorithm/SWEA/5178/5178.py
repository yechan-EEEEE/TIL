T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    ans = 0

    tree = [0] + [0]*N
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    for i in range(N, 0, -1):
        if tree[i] == 0:
            if 2*i <= N:
                tree[i] += tree[2*i]
                if 2*i+1 <= N:
                    tree[i] += tree[2*i+1]
    ans = tree[L]
    print(f'#{tc} {ans}')
