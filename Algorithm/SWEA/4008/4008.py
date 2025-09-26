def dfs(cnt, score, operations):
    global max_result, min_result

    if cnt == N - 1:
        max_result = max(max_result, score)
        min_result = min(min_result, score)
        return

    if operations[0] > 0:
        operations[0] -= 1
        dfs(cnt + 1, score + num_list[cnt + 1], operations)
        operations[0] += 1

    if operations[1] > 0:
        operations[1] -= 1
        dfs(cnt + 1, score - num_list[cnt + 1], operations)
        operations[1] += 1

    if operations[2] > 0:
        operations[2] -= 1
        dfs(cnt + 1, score * num_list[cnt + 1], operations)
        operations[2] += 1

    if operations[3] > 0:
        operations[3] -= 1
        dfs(cnt + 1, int(score / num_list[cnt + 1]), operations)
        operations[3] += 1


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    operations = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    max_result = -100000001
    min_result = 100000001
    dfs(0, num_list[0], operations)
    result = max_result - min_result
    print(f'#{t} {result}')
