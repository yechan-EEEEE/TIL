import heapq
import math


def dijkstra(graph, start):
    distances = {v: math.inf for v in graph}
    distances[start] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, start])

