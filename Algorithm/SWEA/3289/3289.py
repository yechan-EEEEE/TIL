def find_set(x):

    if x != p_list[x]:
        p_list[x] = find_set(p_list[x])
    return p_list[x]


def union(x, y):
    # 최적화 전
    # px = find_set(x)
    # py = find_set(y)

    # if px < py:
    #     p[y] = px
    # else:
    #     p[x] = py

    # 최적화
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if rank[px] > rank[py]:
            p_list[py] = px
        elif rank[px] < rank[py]:
            p_list[px] = py
        else:
            p_list[py] = px
            rank[px] += 1


def check(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    p_list = list(range(n + 1))
    rank = list(range(n + 1))
    ans = ''
    for i in range(m):
        function, a, b = map(int, input().split())
        if function == 0:
            union(a, b)
        elif function == 1:
            A = str(check(a, b))
            ans += A

    # print(f'#{tc} {"".join(ans)}')
    print(f'#{tc} {ans}')
