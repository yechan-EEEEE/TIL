from collections import deque
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
#
#
# T = 10
# for tc in range(1, T + 1):
#     p_list = list(range(101))
#     rank = list(range(101))
#     length, start = map(int, input().split())
#     data = list(map(int, input().split()))
#
#     for i in range(length):
#         x, y = i*2, i*2+1
#         union_set(p_list[x], p_list[y])
#
#     print(p_list)
T = 10
for tc in range(1, T + 1):
    length, start = map(int, input().split())
    data = list(map(int, input().split()))
    queue = deque()
    graph = [[] for _ in range(101)]
    for i in range(0, length, 2):
        graph[data[i]].append(data[i+1])

    
    visited = [0] * 101
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            # print(nxt)
            if not visited[nxt]:
                visited[nxt] = visited[cur] + 1
                queue.append(nxt)
    
    max_level = max(visited)
    ans = 0
    for i in range(101):
        if visited[i] == max_level:
            ans = max(ans, i)
    print(f"#{tc} {ans}")
