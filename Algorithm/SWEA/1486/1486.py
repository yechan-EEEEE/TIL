"""
부분집합을 구하는 문제다 
DFS(깊이 우선 탐색)
"""
# T = int(input())
# for test_case in range(1, T + 1):
#     # N: 사람 수, B: 목표 높이
#     N, B = map(int, input().split())
#     # 각 사람의 키를 입력받아 리스트로 저장
#     arr = list(map(int, input().split()))
#
#     min_height = float('INF')
#
#     # idx: 현재 탐색 중인 직원의 인덱스
#     # h_sum: 내가 선택해온 직원들의 키의 합
#     def dfs(idx, h_sum):  # 재귀적으로 안으로 파고들면서, 점원들의 키의 합 중에서 B를 넘고, 가장 작은 값을 구하는 함수
#         global min_height
#
#         # 여태까지 선택한 직원들의 키의 합이.. 이미 우리가 선정한 최소값보다 커졌으면
#         # 더 이상 진행할 필요가 없습니다.
#         # 가지치기 => 백트래킹 기법
#         if h_sum >= min_height:
#             return
#
#         # 모든 직원들에 대해서 선택이 끝났다는 거에요.
#         if idx == N:
#             if h_sum >= B:
#                 min_height = min(min_height, h_sum)
#             return
#
#         # idx에 해당하는 직원을 "선택"한 경우
#         dfs(idx+1, h_sum + arr[idx])
#
#         # idx에 해당하는 직원을 "선택하지 않은" 경우
#         dfs(idx+1, h_sum)
#
#     dfs(0, 0)
#
#     print(f"#{test_case} {min_height - B}")

"""
    재귀함수의 파라미터
    DFS => 스택  => 재귀 
    1. 재귀함수를 종료하기 위한 변수 
    - 점원들을 모두 선택(포함하든/안하든) 했을 때
    - 현재 선택한 점원의 인덱스  
    2. 누적해서 가져가고 싶은 값
    - 우리가 포함한 점원들 키의 합 
"""


'''
10
5 16
3 1 3 5 6
2 10
7 7
3 120
83 64 36
4 416
299 239 116 128
5 1535
351 228 300 623 954
10 2780
268 61 201 535 464 168 491 275 578 153
10 1162
73 857 502 826 923 653 168 396 353 874
15 8855
3711 576 9081 3280 1413 6818 5142 2981 1266 484 5757 2451 6961 4862 2086
15 57209
8903 5737 3749 8960 724 6295 1240 4325 8023 3640 2223 639 4161 5330 4260
20 78988
3811 2307 3935 5052 4936 3473 6432 7032 1560 1992 5332 7000 4020 9344 2732 8815 9924 8998 9540 4640
'''
# T = int(input())

# for tc in range(1, T + 1):
#     N, B = map(int, input().split())
#     N_lst = list(map(int, input().split()))

#     v_lst = [1] + [0] * sum(N_lst)   # 만들 수 있는 키 합 여부 체크
#     ans_lst = [0]                    # 현재까지 가능한 키 합 리스트

#     for i in N_lst:
#         temp_lst = []
#         for j in ans_lst:
#             if v_lst[i + j] == 0:
#                 v_lst[i + j] = 1
#                 print(f'v_list={v_lst}')
#                 temp_lst.append(i + j)
#                 print(f'temp_lst={temp_lst}')
#         ans_lst.extend(temp_lst)
#         print(f'ans_lst={ans_lst}')

#     # B 이상이 되는 최소 키 찾기
#     for k in range(B, len(v_lst)):
#         if v_lst[k] == 1:
#             ans = k
#             break

#     print(f"#{tc} {ans - B}")

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    h_list = list(map(int, input().split()))
    min_height = N * 10000

    def dfs(idx, h_sum):
        global min_height

        if h_sum >= min_height:
            return

        if idx == N:
            if h_sum >= B:
                min_height = min(min_height, h_sum)
            return
        dfs(idx+1, h_sum + h_list[idx])

        dfs(idx+1, h_sum)

    dfs(0, 0)
    print(f'#{tc} {min_height - B}')
