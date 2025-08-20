#
# wid_d = [[0, 1], [0, -1]]  # 가로로 움직일 값
# len_d = [[1, 0], [-1, 0]]  # 세로로 움직일 값
# T = int(input())
# for tc in range(1, T+1):
#     N, K = list(map(int, input().split()))
#     word_puz = [list(map(int, input().split()))for _ in range(N)]
#     max_val = 0  # 길이가 맞는 칸의 개수
#     for i in range(N):
#         for j in range(N):
#             cur_room = 0  # 현재 칸의 크기
#             for wid_x, wid_y in wid_d:  # 이렇게 하면 0, 1 / 0, -1 이 순서대로 들어간다, 오른쪽 왼쪽으로 움직이는 반복문
#                 # print(wid_x, wid_y)
#                 cur_room_w = 0  # 양쪽 움직인 값을 더한 값
#                 for dist1 in range(1, N):  # 반복을 할건데 어디서 하든 어차피 N보다 작으니까 N만큼 반복해보죠
#                     nx1 = i + wid_x * dist1  # 다음에 움직일 x위치
#                     ny1 = j + wid_y * dist1  # 다음에 움직일 y위치
#                     print(nx1, ny1)
#                     if 0 <= nx1 < N and 0 <= ny1 < N:  # 다음에 움직일 위치가 퍼즐 안에 있으면
#                         if word_puz[nx1][ny1] == 1:
#                             print(nx1, ny1)
#                             # print(word_puz[nx1][ny1])
#                             cur_room_w += 1
#                             # print(cur_room_w)
#                     else:  # 퍼즐 밖으로 나가면 반복문 종료
#                         break
#                 # print(cur_room_w)
#             if cur_room_w+1 == K:
#                 max_val += 1
#             for len_x, len_y in len_d:  # 이렇게 하면 0, 1 / 0, -1 이 순서대로 들어간다
#                 cur_room_l = 0
#                 for dist2 in range(N):  # 반복을 할건데 어디서 하든 어차피 N보다 작으니까 N만큼 반복해보죠
#                     nx2 = i + len_x * dist2  # 다음에 움직일 x위치
#                     ny2 = j + len_y * dist2  # 다음에 움직일 y위치
#                     if 0 <= nx2 < N and 0 <= ny2 < N:  # 다음에 움직일 위치가 퍼즐 안에 있으면
#                         cur_room_l += 1
#                     else:  # 퍼즐 밖으로 나가면 반복문 종료
#                         break
#             if cur_room_l == K:
#                 max_val += 1
#     print(f'#{tc} {max_val}')

# T = int(input())
# dxy = [[0, 1], [1, 0]]

# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(N)]
#     result = 0

#     for i in range(N):
#         for j in range(N):
#             empty_cnt = 0
#             for dx, dy in dxy:
#                 for k in range(1,N+1):
#                     nx = i + dx * k
#                     ny = j + dy * k
#                     print(f'nx={nx} ny={ny}')
#                     if 0 <= nx < N and 0 <= ny < N:
#                         if grid[nx][ny] == 1:
#                             print(f'grid[nx][ny]={grid[nx][ny]}')
#                             empty_cnt += 1
#                             print(empty_cnt)
#                             if nx <= N-1 and ny <= N-1 and empty_cnt == K:
#                                 print(empty_cnt, K)
#                                 result += 1
#                                 print(result)
#                                 empty_cnt = 0
#                         if grid[nx][ny] == 0 and empty_cnt != K:
#                             empty_cnt = 0
#     print(f'#{tc} {result}')
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 가로 확인
    for i in range(N):
        empty_cnt = 0
        for j in range(N):
            if grid[i][j] == 1:
                empty_cnt += 1
            else:  # 다음 칸이 1이 아닌데
                if empty_cnt == K:  # 카운트가 K랑 같으면
                    result += 1
                empty_cnt = 0  # 카운트 초기화
        if empty_cnt == K:  # 마지막까지 1이여서 끝까지 갔을 때 카운트가 K면
            result += 1

    # 세로 확인
    for j in range(N):
        empty_cnt = 0
        for i in range(N):
            if grid[i][j] == 1:
                empty_cnt += 1
            else:
                if empty_cnt == K:
                    result += 1
                empty_cnt = 0
        if empty_cnt == K:  # 마지막 칸 체크
            result += 1

    print(f'#{tc} {result}')
