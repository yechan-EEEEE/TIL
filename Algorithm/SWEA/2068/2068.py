'''
10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.


[제약 사항]

각 수는 0 이상 10000 이하의 정수이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
'''
T = int(input())

for tc in range(1, T + 1):
    num_list = list(map(int, input().split()))
    max_num = 0
    for i in num_list:
        if i > max_num:
            max_num = i
    print(f'#{tc} {max_num}')