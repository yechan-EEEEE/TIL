import heapq
import math


# def dijkstra(height, N):
#     dist = [[math.inf] * N for _ in range(N)]  # 거리 저장할 변수
#     dist[0][0] = 0  # 시작 지점은 0
#     heap = [(0, 0, 0)]  # (비용, x, y)
#     dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#     while heap:
#         cost, x, y = heapq.heappop(heap)

#         if cost > dist[x][y]:  # 이동 비용이 저장된 비용보다 크면 pass
#             continue

#         for dx, dy in dxy:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < N:
#                 next_cost = 1  # 다음 칸 기본 이동 비용 1
#                 if height[nx][ny] > height[x][y]:  # 다음칸 높이가 더 높으면
#                     next_cost += (height[nx][ny] - height[x][y])  # 이동 비용에다 높이 차이만큼 +
#                 new_dist = cost + next_cost  # 새로운 이동 비용 = 현재까지의 비용 + 이동 비용

#                 if new_dist < dist[nx][ny]:  # 새로운 이동 비용이 기록된 최소 비용보다 적으면 갱신
#                     dist[nx][ny] = new_dist
#                     heapq.heappush(heap, (new_dist, nx, ny))

#         if (x, y) == (N - 1, N - 1):  # 도착하면 반환
#             return cost


def dijkstra(height, N):
    dist = [[math.inf] * N for _ in range(N)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        cost, x, y = heapq.heappop(heap)

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                next_cost = 1
                if height[nx][ny] > height[x][y]:
                    next_cost += (height[nx][ny] - height[x][y])
                new_dist = cost + next_cost

                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heapq.heappush(heap, (new_dist, nx, ny))
        
        if (x, y) == (N - 1, N - 1):
            return cost


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]
    
    result = dijkstra(height, N)
    print(f'#{tc} {result}')
