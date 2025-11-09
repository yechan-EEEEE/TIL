def dfs(node, visited, count):
    global max_len
    max_len = max(max_len, count)
    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, visited, count + 1)
            visited[nxt] = False  # 백트래킹 (다른 경로 탐색을 위해 복구)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    max_len = 0
    for start in range(1, N + 1):
        visited = [False] * (N + 1)
        visited[start] = True
        dfs(start, visited, 1)

    print(f"#{tc} {max_len}")
