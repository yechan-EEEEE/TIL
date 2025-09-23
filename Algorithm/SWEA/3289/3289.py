# def find_set(x):
#     if x != p_list[x]:
#         p_list[x] = find_set(p_list[x])
#     return p_list[x]


# def union(x, y):
#     px = find_set(x)
#     py = find_set(y)

#     if px != py:
#         if rank[px] > rank[py]:
#             p_list[py] = px
#         elif rank[px] < rank[py]:
#             p_list[px] = py
#         else:
#             p_list[py] = px
#             rank[px] += 1


# def check(x, y):
#     px = find_set(x)
#     py = find_set(y)

#     if px != py:
#         return 0
#     else:
#         return 1


# T = int(input())
# for tc in range(1, T + 1):
#     n, m = map(int, input().split())
#     p_list = list(range(n + 1))
#     rank = list(range(n + 1))
#     ans = ''
#     for i in range(m):
#         function, a, b = map(int, input().split())
#         if function == 0:
#             union(a, b)
#         elif function == 1:
#             A = str(check(a, b))
#             ans += A

#     # print(f'#{tc} {"".join(ans)}')
#     print(f'#{tc} {ans}')
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union_set(x, y):
    px, py = find_set(x), find_set(y)

    if px != py:
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px
            rank[px] += 1


def check(x, y):
    px, py = find_set(x), find_set(y)

    if px != py:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    p = list(range(n + 1))
    rank = [0] * (n + 1)
    ans = ''

    for i in range(m):
        function, a, b = map(int, input().split())
        if function == 0:
            union_set(a, b)
        if function == 1:
            A = check(a, b)
            ans += str(A)
    
    print(f'#{tc} {ans}')
