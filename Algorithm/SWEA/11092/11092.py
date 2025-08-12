'''
N개의 양의 정수가 첫번째부터 N번째까지 주어진다. 최대값의 위치와 최소값의 위치의 차이를 절대값으로 출력 하시오. 단, 가장 작은 수가 여러 개이면 먼저 나오는 위치로 하고 가장 큰 수가 여러 개이면 마지막으로 나오는 위치로 한다.
예를 들어, {1, 1, 2, 3, 3} 가 주어지면 최대값의 위치는 5이고, 최소값의 위치는 1이다. 따라서 두 값 차이의 절대값은 4이다.

[입력]
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 10 )
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 100 )
다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 10 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력                        출력
3
5
1 1 2 3 3                   #1 4
10
3 10 5 5 8 3 9 1 3 3        #2 6

'''

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    input_num = list(map(int,input().split()))
    max_num = 0  # 최대값
    min_num = 10  # 최소값
    max_loc = 0  # 최대값 위치의 절대값
    min_loc = 0  # 최소값 위치의 절대값
    for i in range(1,N+1): 
        cur_num = 0
        cur_loc = i  # 현재 위치
        cur_num = input_num[i-1]  # 현재 값
        if cur_num >= max_num:  # 현재 값이 max_num보다 크거나 같으면
            max_num = cur_num  # max_num을 현재 값으로 바꿔주고
            max_loc = cur_loc  # max_loc을 현재 위치로 바꿈
        if cur_num < min_num:  # 현재 값이 min_num보다 작으면
            min_num = cur_num  # min_num을 현재 값으로 바꿔주고
            min_loc = cur_loc  # min_loc을 현재 위치로 바꿈
        # print(cur_num)
        # print(cur_loc)
        # print(max_num)
        # print(max_loc)
        # print(min_num)
        # print(min_loc)
    # print(cur_num)
    # print(cur_loc)
    # print(max_num)
    # print(max_loc)
    # print(min_num)
    # print(min_loc)
    result = abs(max_loc-min_loc)  # abs 절대값 함수
    print(f'#{tc} {result}')
