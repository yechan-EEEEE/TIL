from collections import deque

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    num = list(map(int, input().split()))
    num_list = deque()
    for i in num:
        num_list.append(i)

    while True:
        for j in range(1, 6):
            num_list[0] -= j
            a = num_list.popleft()
            if a < 0:
                a = 0
            num_list.append(a)
            if a == 0:
                break
        if num_list[7] == 0:
            break

    result = ""
    for ans in num_list:
        result += str(ans)
        result += " "

    print(f'#{tc} {result}')
