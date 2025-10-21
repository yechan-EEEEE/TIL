"""
빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다. 빙산 이외의 바다에 해당되는 칸에는 0이 저장된다.
배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다. 바닷물은 호수처럼 빙산에 둘러싸여 있을 수도 있다.
2차원 배열에서 동서남북 방향으로 붙어있는 칸들은 서로 연결되어 있다고 말한다.
빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램
만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.

첫 줄에는 이차원 배열의 행의 개수와 열의 개수를 나타내는 두 정수 N과 M이 한 개의 빈칸을 사이에 두고 주어진다.
N과 M은 3 이상 300 이하이다.
그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다.
각 칸에 들어가는 값은 0 이상 10 이하이다.
배열에서 빙산이 차지하는 칸의 개수, 즉, 1 이상의 정수가 들어가는 칸의 개수는 10,000 개 이하이다.
배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.

5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
                2

i나 j가 0이 아닌 곳에서만
주변의 0 개수만큼 빼는데 visited를 확인하고 처음인 부분만 세서 빼기
한 바퀴 다 돌고 덩어리 개수 세서 두 덩어리 이상이면 cnt출력
아직 한덩어리면 visited 초기화하고 다시
전부 0이 돼버리면 0 출력
"""
from collections import deque
import copy
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def cnt_ice(arr):
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and not visited[i][j]:
                cnt += 1
                queue = deque([(i, j)])
                visited[i][j] = True
                
                while queue:
                    cx, cy = queue.popleft()
                    for dx, dy in dxy:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] > 0 and not visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
    return cnt


def melt_ice(arr):
    new_arr = copy.deepcopy(arr)
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                zero_cnt = 0
                for dx, dy in dxy:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                        zero_cnt += 1
                new_arr[i][j] = max(0, arr[i][j] - zero_cnt)
    
    return new_arr

N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]

year = 0

while True:
    num_of_ice = cnt_ice(ice)
    
    # 빙산이 두 덩어리 이상이면 종료
    if num_of_ice >= 2:
        print(year)
        break
    
    # 빙산이 모두 녹았으면 0 출력
    if num_of_ice == 0:
        print(0)
        break
    
    # 빙산 녹이기
    ice = melt_ice(ice)
    year += 1