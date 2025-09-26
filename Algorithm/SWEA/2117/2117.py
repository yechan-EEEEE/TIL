T = int(input())
for x in range(1, T + 1):
    N, M = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(N)]


    def dfs(row, col, K):
        global max_houses
        # 영역 안에 있는 집 개수 세기
        house_count = 0
        for i in range(N):
            for j in range(N):
                if abs(i - row) + abs(j - col) < K:
                    if Map[i][j] == 1:
                        house_count += 1

        cost = K * K + (K - 1) * (K - 1)
        if house_count * M >= cost:
            max_houses = max(max_houses, house_count)
            # 다음 K로 확장
            dfs(row, col, K + 1)
        else:
            return  # 손해가 나면 더 이상 확장하지 않음

    max_houses = 0
    for r in range(N):
        for c in range(N):
            dfs(r, c, 1)  # K=1부터 시작

    print(f'#{x} {max_houses}')
