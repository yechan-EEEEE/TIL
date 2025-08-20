T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    rotated_grid = []

    for k in range(3):  # 90도 돌리기 3번
        new_grid = [[0]*N for _ in range(N)]  # 칸 수 똑같은 새로운 그리드
        for i in range(N):
            for j in range(N):
                new_grid[j][N-i-1] = grid[i][j]  # 이동 규칙대로 이동
        rotated_grid.append(new_grid)  # 전부 출력해야해서 돌렸을 때 값을 저장해둠
        grid = new_grid  # 다시 돌려야하니 grid에 돌아간 값을 저장
    # print(rotated_grid)
    print(f'#{tc}')
    for i in range(N):
        result = []
        for j in rotated_grid:
            result.append(''.join(map(str, j[i])))  # result에 저장해둔 돌아간 값들 첫번째 줄부터 띄어쓰기를 빼고 넣어줌
            # print(result)
        print(' '.join(result))  # result에 들어간 값들을 서로 띄어쓰기를 해서 출력

"""
t = int(input())
 
for testcase in range(0, t):
    print(f"#{testcase+1}")
    n = int(input())
    board = []
 
    for i in range(n):
        board.append(list(map(int, input().split())))
 
    for i in range(n):
        for j in range(n-1, -1, -1):
            print(board[j][i], end="")
 
        print(end = " ")
 
        for j in range(n-1, -1, -1):
            print(board[n-i-1][j], end="")
 
        print(end=" ")
 
        for j in range(n):
            print(board[j][n-i-1], end="")
 
        print()
"""