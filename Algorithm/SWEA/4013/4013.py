from collections import deque


def rotate_gear(gear, direct):  # 번호, 방향
    if direct == 1:  # 시계 방향
        x = gear.pop()
        gear.appendleft(x)

    elif direct == -1:  # 반시계 방향
        x = gear.popleft()
        gear.append(x)
        

T = int(input())
for tc in range(1, T + 1):
    K = int(input())  # 회전 횟수
    gears = [()]  # 1번부터 쓰려고 빈 칸 하나 넣음
    magnet_num = 4  # 자석 개수
    for _ in range(magnet_num):
        gears.append(deque(map(int, input().split())))

    for _ in range(K):
        num, direction = map(int, input().split())
        dirs = [0] * (magnet_num + 1)  # 회전 방향 저장
        dirs[num] = direction

        # 왼쪽 확인
        for i in range(num, 1, -1):  # 지금 자석부터 1번 자석까지
            if gears[i][6] != gears[i-1][2]:
                dirs[i-1] = -dirs[i]
            else:
                break

        # 오른쪽 확인
        for i in range(num, magnet_num):  # 마지막 자석은 오른쪽이 없으니까 마지막 전까지
            if gears[i][2] != gears[i+1][6]:
                dirs[i+1] = -dirs[i]
            else:
                break

        # 실제 회전
        for i in range(1, magnet_num + 1):
            if dirs[i] != 0:
                rotate_gear(gears[i], dirs[i])

    # 점수 계산
    score = [1, 2, 4, 8]
    score_sum = 0
    for i in range(1, magnet_num + 1):
        if gears[i][0] == 1:
            score_sum += score[i - 1]

    print(f"#{tc} {score_sum}")
