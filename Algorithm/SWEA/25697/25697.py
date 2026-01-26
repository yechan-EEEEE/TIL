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
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     N, X = map(int, input().split())
#     d_list = list(map(int, input().split()))
#     cnt = 0
#     cur_distance = 0
#     if len(d_list) == 1 and d_list[0] > abs(X):
#         cur_distance += d_list[0]
#         cnt += 1
#     while True:        
#         for i in d_list:
#             cur_distance += i
#             cnt += 1
#             if cur_distance >= abs(X):
#                 break
#         if cur_distance >= abs(X):
#             break
#     print(cnt)

import sys
input = sys.stdin.readline

def solve(x, lst):
    if x == 0:
        return 0
    x = abs(x)  # 도착 거리
 
    sl = sum(lst)  # 한 루프 돌았을 때 거리
    if x >= sl:  # 한 루프를 꽉 채우거나 그 이상일 때
        dd, m = divmod(x, sl)  # 몫, 나머지
        answer = dd * len(lst)  # 바퀴 수 * 한 바퀴당 점프 횟수
        if m <= 0:  # 딱 떨어지면 바퀴 수만큼만 뜀
            return answer
        for d in lst:  # 남은 거리를 빼가면서 도착하면 return
            m -= d
            answer += 1
            if m <= 0:
                return answer
    else:  # 한 루프를 다 돌기 전에 도착할 때
        maxd = lst[0]
        sumd = 0
        answer = 0
        for _ in range(2):
            for d in lst:
                sumd += d
                maxd = max(maxd, d)
                answer += 1
                if max(0, 2 * maxd - sumd) <= x <= sumd:
                    return answer
    return -1

t = int(input())
 
for _ in range(t):
    _, x = map(int, input().split())
    lst = list(map(int, input().split()))
    print(solve(x, lst)) 