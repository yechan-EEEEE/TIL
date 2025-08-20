# T = int(input())

# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     station_num = list(map(int, input().split()))
#     # station = []
#     cur_fuel = K
#     charge_cnt = 0
#     cur_num = 0
#     # possible = 1
#     # recharge = []
#     # for _ in station_num:
#     #     recharge.append(_)
    
#     for i in range(1, N+1):
#         cur_num += 1
#         cur_fuel -= 1
#         if cur_fuel < 0:
#             charge_cnt = 0
#             break
#         if cur_num + cur_fuel < ? and i in station_num
#             cur_fuel = K
#             charge_cnt += 1
#     # if possible == 0:
#     #     charge_cnt = 0
    
#     print(f'#{tc} {charge_cnt}')
T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    station_num = list(map(int, input().split()))

    cur_fuel = K
    charge_cnt = 0
    cur_num = 0  # 지금 위치

    for i in range(1, N+1):  # 한 칸 갈때마다
        cur_num += 1
        cur_fuel -= 1
        if cur_fuel < 0:  # 연료가 0보다 작아지면 전진 불가능
            charge_cnt = 0  # 0 출력
            break

        # 가장 가까운 충전소 찾기
        next_station = N  # 충전소는 종점보다 앞에 있으니까 종점으로 설정
        for s in station_num:
            if s > i:  # 현재 위치보다 충전소의 위치가 더 멀면 가장 가까운 충전소
                next_station = s
                break

        if i in station_num and i + cur_fuel < next_station:
            # 현재 위치가 충전소가 있는 정류장이고, 현재위치 + 연료가 다음 충전소보다 작다면(충전소까지 도착 못한다면) 충전
            cur_fuel = K
            charge_cnt += 1

    print(f'#{tc} {charge_cnt}')
