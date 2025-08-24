dxy = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]

    # 초기 배치
    mid = N // 2
    board[mid-1][mid-1] = 2  # 백 왼쪽위
    board[mid][mid] = 2      # 백 오른쪽 아래
    board[mid-1][mid] = 1    # 흑 오른쪽 위
    board[mid][mid-1] = 1    # 흑 왼쪽 아래

    # M번 돌 놓기
    for _ in range(M):
        x, y, color = map(int, input().split())
        x -= 1  # 입력받는 숫자는 1부터 N까지의 좌표라서 -1씩 해줘야함
        y -= 1
        board[x][y] = color  # 입력 받으면 그 자리에 돌을 둔다

        # 8방향 탐색
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            flip_list = []  # 색을 바꿔야할 돌 리스트
            # 범위가 보드 안이고, 돌이 놓여있고, 내가 지금 놓는 돌이랑 색이 다르다면 실행
            while 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 0 and board[nx][ny] != color:
                flip_list.append((nx, ny))  # 방금 그 좌표를 넣어주고 그 방향으로 한번 더 이동
                nx += dx
                ny += dy
            # while 문 끝나고 나와서 그 방향으로 한칸 더 갔을 때 같은 색 돌이 있으면 리스트에 저장된 돌들 색 바꾸기
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == color:
                for fx, fy in flip_list:
                    board[fx][fy] = color

    # 흑/백 돌 개수 세기
    black = sum(stone.count(1) for stone in board)  # 
    white = sum(stone.count(2) for stone in board)

    print(f"#{tc} {black} {white}")
