T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    idx = list(map(int, input().split()))
    m = max(idx)
    tree = [[] for _ in range(m+1)]
    nod_cnt = 1

    for i in range(0, len(idx), 2):
        tree[idx[i]].append(idx[i+1])

    stack = [N]
    nod_cnt = 0

    while stack:
        node = stack.pop()
        nod_cnt += 1
        stack.extend(tree[node])

    print(f'#{tc} {nod_cnt}')
