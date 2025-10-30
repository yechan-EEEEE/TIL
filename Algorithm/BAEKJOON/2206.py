"""
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다.
(1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

6 4
0100
1110
1000
0000
0111
0000
        15
4 4
0111
1111
1111
1110
        -1

bfs를 합니다
1. 길이 뚫려있을 때
2. (0, 1)을 뚫었을 때
3. (1, 0)을 뚫었을 때
뚫기는 한 번만 가능이니까 power 1로 두고 뚫으면 0
power가 1일 때만 뚫을 수 있게 해두기
1, 2, 3 비교해서 제일 작은 값
N, M이 visited가 됐을 때만 값 return
visited가 안 된 애들은 -1 return
"""
from collections import deque


def bfs(arr):
    return 0


N, M = map(int, input().split())
map_info1 = [list(map(int, input().strip())) for _ in range(N)]
map_info2 = [row[:] for row in map_info1]
map_info3 = [row[:] for row in map_info1]

result1 = bfs(map_info1)
result2 = bfs(map_info2)
result3 = bfs(map_info3)

ans = max(result1, result2, result3)
