T = int(input())

for tc in range(1, T + 1):
    input_text = list(input().strip())
    stack = []
    result = 0
    for i in input_text:
        if not stack:
            stack.append(i)
        elif len(stack) >= 1 and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    result = len(stack)

    print(f'#{tc} {result}')
