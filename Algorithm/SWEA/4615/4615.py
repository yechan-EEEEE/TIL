dxy = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]

    # 초기 배치
    mid = N // 2
    board[mid-1][mid-1] = 2  # 백
    board[mid][mid] = 2      # 백
    board[mid-1][mid] = 1    # 흑
    board[mid][mid-1] = 1    # 흑

    # M번 돌 놓기
    for _ in range(M):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        board[x][y] = color

        # 8방향 탐색
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            flip_list = []
            while 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 0 and board[nx][ny] != color:
                flip_list.append((nx, ny))
                nx += dx
                ny += dy
            # 뒤집기
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == color:
                for fx, fy in flip_list:
                    board[fx][fy] = color

    # 흑/백 돌 개수 세기
    black = sum(stone.count(1) for stone in board)
    white = sum(stone.count(2) for stone in board)

    print(f"#{tc} {black} {white}")
