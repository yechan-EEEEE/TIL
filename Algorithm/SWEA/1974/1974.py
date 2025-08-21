T = int(input())

for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    # 가로 검사
    for i in range(9):
        num_test = set()
        for j in range(9):
            num_test.add(sudoku[i][j])
        if len(num_test) != 9:
            result = 0
            break
    # 세로 검사
    for i in range(9):
        num_test = set()
        for j in range(9):
            num_test.add(sudoku[j][i])
        if len(num_test) != 9:
            result = 0
            break
    
    # 네모칸 검사
    for i in range(3):       # 블록 x좌표 index
        for j in range(3):   # 블록 y좌표 index
            start_x = i * 3
            start_y = j * 3
            num_test = set()
            for dx in range(3):
                for dy in range(3):
                    nx = start_x + dx
                    ny = start_y + dy
                    num_test.add(sudoku[nx][ny])
            if len(num_test) != 9:
                result = 0
                break
        if result == 0:
            break

    print(f'#{tc} {result}')