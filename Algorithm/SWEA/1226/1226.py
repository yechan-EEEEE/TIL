"""
각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
총 10개의 테스트케이스가 주어진다.
테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

[출력]
부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).

1
1111111111111111
1210000000100011
1010101110101111
1000100010100011
1111111010101011
1000000010101011
1011111110111011
1010000010001011
1010101111101011
1010100010001011
1010111010111011
1010001000100011
1011101111101011
1000100000001311
1111111111111111
1111111111111111

def get_road_move_time(road, n, m):
    queue = deque()
    queue.append((0, 0))
    distance = [[-1] * m for _ in range(n)]  # 방문처리를 위한 변수, -1이면 최단거리 갱신x(방문x), -1아니면 (방문o, don't touch)
    distance[0][0] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1 and road[nx][ny] == 1:
                queue.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1
                if nx == n-1 and ny == m-1:
                    return distance[nx][ny]


# 도로의 크기 n * m 입력 받기
n, m = map(int, input().split())
# 도로 정보 입력
road = [list(map(int, input().split())) for _ in range(n)]

# BFS 를 이용해서 이동시간 구하기
result = get_road_move_time(road, n, m)
print(result)
"""

from collections import deque
for test in range(10):
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    T = int(input())
    size = 16
    Map = [list(map(int, input().strip())) for _ in range(size)]


    def find_route(mini_map):
        queue = deque()
        queue.append((1, 1))
        visited = [[-1] * size for _ in range(size)]
        visited[1][1] = 0

        while queue:
            x, y = queue.popleft()
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size:
                    if mini_map[nx][ny] == 3:
                        return True
                    if mini_map[nx][ny] == 0 and visited[nx][ny] == -1:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
        return False
    if find_route(Map):
        print(f'#{T} 1')
    if not find_route(Map):
        print(f'#{T} 0')
