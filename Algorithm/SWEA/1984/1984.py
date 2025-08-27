T = int(input())

for tc in range(1, T + 1):
    number = list(map(int, input().split()))
    max_num = 0
    min_num = 100000
    result = 0
    sum_num = 0

    for i in number:
        if i > max_num:
            max_num = i
        elif i < min_num:
            min_num = i

    for i in number:
        if i == min_num or i == max_num:
            continue
        else:
            sum_num += i
    average = sum_num / 8
    result = round(average)
    print(f'#{tc} {result}')
