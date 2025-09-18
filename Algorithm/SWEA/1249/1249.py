from collections import deque

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

C = int(input())
for Case in range(1, C+1):
    N = int(input())
    Map = [list(map(int, input().strip())) for _ in range(N)]

    visited = [[float('inf')] * N for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0
    result = 0

    def fastest_time(mini_map, map_size):
        while queue:
            x, y = queue.popleft()
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < map_size and 0 <= ny < map_size:
                    fix_time = visited[x][y] + mini_map[nx][ny]
                    if visited[nx][ny] > fix_time:
                        visited[nx][ny] = fix_time
                        queue.append((nx, ny))
        return visited[map_size-1][map_size-1]

    result = fastest_time(Map, N)
    print(f'#{Case} {result}')

"""
from collections import deque

dxy = [[-1,0],[1,0],[0,-1],[0,1]]

C = int(input())
for Case in range(1, C+1):
    N = int(input())
    Map = [list(map(int, list(input().strip()))) for _ in range(N)]

    visited = [[float('inf')] * N for _ in range(N)]
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if nx == N-1 and ny == N-1:
                    # 도착점은 0이므로 더하지 않고 바로 누적시간 비교
                    fix_time = visited[x][y]
                else:
                    fix_time = visited[x][y] + Map[nx][ny]
    
                if visited[nx][ny] > fix_time:
                    visited[nx][ny] = fix_time
                    queue.append((nx, ny))


    print(f'#{Case} {visited[N-1][N-1]}')


"""
"""
def fastest_time(Map, N):
    queue = deque()
    queue.append((0, 0))
    visited = [[-1 * N] for _ in range(N)]
    visited[0][0] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1:
                    queue.append((nx, ny))
                    Map[nx][ny] += Map[x][y]
                    if nx == N-1 and ny == N-1:
                        return Map[nx][ny]

result = fastest_time(Map, N)
print(f'#{Case} {result}')
"""