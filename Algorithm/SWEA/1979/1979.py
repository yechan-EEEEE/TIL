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
mov_right = [[0, 1]]
mov_left = [0, -1]
mov_up = [-1, 0]
mov_down = [1, 0]
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    word_puz = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0  # 최대값
    for i in range(N):
        for j in range(N):
            cur_room = 0  # 지금 있는 칸의 크기
            for rx, ry in mov_right:  # 이렇게 하면 rx, ry에 0,1이 들어가요
                for dist_r in range(i, N):  # 반복을 할건데
                    nxr = i + rx * dist_r
                    nyr = j + ry * dist_r
                    if 0 <= nxr < N and 0 <= nyr < N and word_puz[nxr][nyr] == 1:  # 움직일 위치가 퍼즐 안이고 값이 1이라면
                        cur_room += 1
                    else:
                        break
                if cur_room == K:
                    max_value += 1
            for lx, ly in mov_left:  # 이렇게 하면 rx, ry에 0,1이 들어가요
                for dist_r in range(i, N):  # 반복을 할건데
                    nxl = i + lx * dist_r
                    nyl = j + ly * dist_r
                    if 0 <= nxr < N and 0 <= nyr < N and word_puz[nxr][nyr] == 1:  # 움직일 위치가 퍼즐 안이고 값이 1이라면
                        cur_room += 1
                    else:
                        break
                if cur_room == K:
                    max_value += 1
            for ux, uy in mov_up:  # 이렇게 하면 rx, ry에 0,1이 들어가요
                for dist_r in range(i, N):  # 반복을 할건데
                    nxu = i + ux * dist_r
                    nyu = j + uy * dist_r
                    if 0 <= nxr < N and 0 <= nyr < N and word_puz[nxr][nyr] == 1:  # 움직일 위치가 퍼즐 안이고 값이 1이라면
                        cur_room += 1
                    else:
                        break
                if cur_room == K:
                    max_value += 1
            for dx, dy in mov_down:  # 이렇게 하면 rx, ry에 0,1이 들어가요
                for dist_r in range(i, N):  # 반복을 할건데
                    nxd = i + dx * dist_r
                    nyd = j + dy * dist_r
                    if 0 <= nxr < N and 0 <= nyr < N and word_puz[nxr][nyr] == 1:  # 움직일 위치가 퍼즐 안이고 값이 1이라면
                        cur_room += 1
                    else:
                        break
                if cur_room == K:
                    max_value += 1
    print(f'#{tc} {max_value}')



