T = int(input())

dxy = [[0, 1], [1, 0]]
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    wid_test, len_test, square_test = 0
    result = 0

    # 가로 검사
    for i in range(9):
        nx = i +