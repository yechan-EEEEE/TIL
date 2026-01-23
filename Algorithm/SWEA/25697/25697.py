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

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    d_list = list(map(int, input().split()))
    X = abs(X)

    cnt = 0
    cur_distance = 0
    max_jump = 0
    found = False

    while cnt <= 10**7:
        for i in d_list:
            cur_distance += i
            max_jump = max(max_jump, i)
            cnt += 1

            if cnt == 1:
                if cur_distance == X:
                    found = True
            elif cnt == 2:
                d0 = d_list[0]
                if len(d_list) > 1:
                    d1 = d_list[1]
                else:
                    d1 = d_list[0]
                if abs(d0 - d1) <= X <= cur_distance:
                    found = True
            else:
                if (2 * max_jump - cur_distance) <= X <= cur_distance:
                    found = True

            if found:
                print(cnt)
                break

        if found:
            break
    else:
        print(-1)