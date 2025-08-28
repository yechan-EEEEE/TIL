import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    cur_max_num = 0
    # item_cnt = 0
    # sum_num = 0
    result = 0

    for i in range(N):
        # print(f'arr[i]={arr[i]}')
        if arr[i] >= cur_max_num:
            # print(f'cur_max_num={cur_max_num}')
            # result += (item_cnt * cur_max_num) - sum_num
            # print(result, item_cnt, cur_max_num, sum_num)
            # cur_max_num = arr[i]
            # print(f'cur_max_num={cur_max_num}')
            # item_cnt = 0
            cur_max_num = arr[i]
        elif arr[i] < cur_max_num:
            # item_cnt += 1
            # print(arr[i], item_cnt, cur_max_num)
            # sum_num += arr[i]
            # print(sum_num)
            result += cur_max_num - arr[i]

    print(f'#{tc} {result}')
