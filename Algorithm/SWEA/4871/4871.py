T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]

    for i in range(E):
        a, b = map(int, input(). split())
        graph[a].append(b)

    print(graph)

    S, G = map(int, input().split())

    visited = [0] * (V + 1)
    ans = 0

    def dfs(node):
        if node == G:
            return True
        visited[node] = 1
        for n_node in graph[node]:
            if not visited[n_node]:
                if dfs(n_node):
                    return True
        return False

    if dfs(S):
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')
