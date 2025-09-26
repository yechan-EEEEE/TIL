def dfs(cnt, score, calorie):
    global result
    # 종료조건, 누적될 값들
    if calorie > limit_k:
        return

    if cnt == topping_cnt:
        result = max(result, score)
        return

    # 골랐을 때
    dfs(cnt + 1, score + toppings[cnt][0], calorie + toppings[cnt][1])

    dfs(cnt + 1, score, calorie)


T = int(input())
for test_case in range(1, T + 1):
    # 토핑 수와 제한 칼로리
    topping_cnt, limit_k = map(int, input().split())
    # [[점수, 칼로리], ... ]
    toppings = [list(map(int, input().split())) for _ in range(topping_cnt)]
    result = 0
    dfs(0, 0, 0)

    print(f"#{test_case} {result}")
