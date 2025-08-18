'''
4
5
1 2 3 4 5
                   # 5
5
4 5 1 2 3
                   # 3
5
5 4 3 2 1
                   # 1
8
1 2 1 2 3 1 2 1
                   # 3
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    car_num = list(map(int, input().split()))
    max_num = 1
    cur_num = 1
    for i in range(N-1):
            if car_num[i] < car_num[i+1]:
                cur_num += 1
                max_num = max(max_num,cur_num)
            else:
                cur_num = 1
    print(f'#{tc} {max_num}')