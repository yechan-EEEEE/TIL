T = int(input())
for tc in range(1, T + 1):
    memory_value = list(map(int, input().strip()))
    cur_num = 0
    cnt = 0

    for i in range(len(memory_value)):
        if memory_value[i] != cur_num:
            cur_num = memory_value[i]
            cnt += 1

    print(f'#{tc} {cnt}')
