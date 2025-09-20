from collections import deque

def rotate_gear(gear, direction):
    if direction == 1:  # 시계 방향
        x = gear.pop()
        gear.appendleft(x)
    elif direction == -1:  # 반시계 방향
        x = gear.popleft()
        gear.append(x)

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    gears = [deque()]  # 1번부터 쓰려고 dummy 하나 넣음
    for _ in range(4):
        gears.append(deque(map(int, input().split())))

    for _ in range(K):
        num, direction = map(int, input().split())
        dirs = [0] * 5  # 회전 방향 저장
        dirs[num] = direction

        # 왼쪽 전파
        for i in range(num, 1, -1):
            if gears[i][6] != gears[i-1][2]:
                dirs[i-1] = -dirs[i]
            else:
                break

        # 오른쪽 전파
        for i in range(num, 4):
            if gears[i][2] != gears[i+1][6]:
                dirs[i+1] = -dirs[i]
            else:
                break

        # 실제 회전
        for i in range(1, 5):
            if dirs[i] != 0:
                rotate_gear(gears[i], dirs[i])

    # 점수 계산
    score = 0
    if gears[1][0] == 1:
        score += 1
    if gears[2][0] == 1:
        score += 2
    if gears[3][0] == 1:
        score += 4
    if gears[4][0] == 1:
        score += 8

    print(f"#{tc} {score}")
