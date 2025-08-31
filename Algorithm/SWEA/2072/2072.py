T = int(input())

for tc in range(1, T + 1):
    num_list = list(map(int, input().split()))
    result = 0

    for i in num_list:
        if i % 2 == 1:
            result += i
    
    print(f'#{tc} {result}')