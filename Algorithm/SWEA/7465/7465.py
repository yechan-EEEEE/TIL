# def find_set(x):
#     if x != p_list[x]:
#         p_list[x] = find_set(p_list[x])
#     return p_list[x]


# def union_set(x, y):
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


# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     p_list = list(range(N + 1))
#     rank = list(range(N + 1))

#     for i in range(M):
#         a, b = map(int, input().split())
#         union_set(a, b)

#     for j in range(1, N+1):
#         p_list[j] = find_set(j)

#     print(f'#{tc} {len(set(p_list))-1}')

# def find_set(x):
#     if x != p[x]:
#         p[x] = find_set(p[x])
#     return p[x]


# def union_set(x, y):
#     px = find_set(x)
#     py = find_set(y)

#     if px != py:
#         if rank[px] > rank[py]:
#             p[py] = px
#         elif rank[px] < rank[py]:
#             p[px] = py
#         else:
#             p[py] = px
#             rank[px] += 1

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     p = list(range(N + 1))
#     rank = [0] * (N + 1)
    
#     for i in range(M):
#         a, b = map(int, input().split())
#         union_set(a, b)
    
#     print(f'#{tc} {len(set(p)) - 1}')

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union_set(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px
            rank[px] += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    p = list(range(N + 1))
    rank = [0] * (N + 1)

    for i in range(M):
        a, b = map(int, input().split())
        union_set(a, b)
    
    for j in range(1, N + 1):
        p[j] = find_set(j)
    
    print(f'#{tc} {len(set(p)) - 1}')
