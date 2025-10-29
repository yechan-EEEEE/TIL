import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T + 1):
    length = int(input())
    table = [list(map(int, input().split())) for _ in range(length)]
    cnt = 0

    for i in range(length):
        for j in range(length):
            if table[i][j] == 1:  # 전체 확인하다가 1이 나오면
                x, y = i, j  # 현재 좌표를 x, y로 놓고
                for k in range(1, length):  # 아래 확인 끝까지 반복
                    nx = x + k
                    if nx < length:  # 범위 안에 있을 때만
                        if table[nx][y] == 2:  # 2 만나면 결속상태 하나 추가하고 결속하면 멈추니까 break
                            cnt += 1
                            break
                        elif table[nx][y] == 1:  # 1 만나면 같은 색에 막혔으니까 break
                            break
                        # 0만 있으면 아래로 빠져나가는 거라 무시해도 됌
    print(f'#{tc} {cnt}')
