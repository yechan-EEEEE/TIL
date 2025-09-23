p = [0] * (N+1)
rank = [0] * (N+1)

# def make_set(x):
#     p[x] = x
#
#
# def find_set(x):
#     # 최적화 전
#     # if x == p[x]:
#     #     return x
#     # return find_set(p[x])
#
#     # 최적화
#     if x != p[x]:
#         p[x] = find_set(p[x])
#     return p[x]
#
#
# def union(x, y):
#     # 최적화 전
#     # px = find_set(x)
#     # py = find_set(y)
#
#     # if px < py:
#     #     p[y] = px
#     # else:
#     #     p[x] = py
#
#     # 최적화
#     px = find_set(x)
#     py = find_set(y)
#
#     if px != py:
#         if rank[px] > rank[py]:
#             p[py] = px
#         elif rank[px] < rank[py]:
#             p[px] = py
#         else:
#             p[py] = px
#             rank[px] += 1

p = [0] * (N+1)
rank = [0] * (N+1)


def make_set(x):
    p[x] = x


def find_set(x):

    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):

    px = find_set(x)
    py = find_set(y)

    # if px > py:
    #     p[x] = py
    # elif px < py:
    #     p[y] = px
    if px != py:
        if rank[px] < rank[py]:
            p[px] = py
        elif rank[px] > rank[py]:
            p[py] = px
        else:
            p[y] = px
            rank[px] += 1































