"""
5

4 10
1 2 3 4
            4
4 11
1 2 3 4
            5
1 3
5
            2
6 6
1 3 5 2 4 6
            3
6 10000000
1 3 5 2 4 6
            2857144
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
buckets = [list(map(int, input().split())) for _ in range(N)]
moves = [tuple(map(int, input().split())) for _ in range(M)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
print(buckets[1][2])