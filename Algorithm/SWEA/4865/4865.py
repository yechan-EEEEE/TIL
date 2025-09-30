T = int(input())
for tc in range(1, T + 1):
    str1 = str(input().strip())
    str2 = str(input().strip())
    max_cnt = 0

    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        max_cnt = max(cnt, max_cnt)
    print(f'#{tc} {max_cnt}')
