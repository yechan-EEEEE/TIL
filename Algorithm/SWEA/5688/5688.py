"""
양의 정수 N에 대해 N = X3가 되는 양의 정수X 를 구하여라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1≤N≤10^18) 이 주어진다.

[출력]
각 테스트 케이스마다 첫 번째 줄에는 #T(T는 테스트케이스 번호를 의미하며 1부터 시작한다.)를 출력하고, N = X3가 되는 양의 정수 X를 출력한다.
만약 이런 X가 존재하지 않으면 -1을 출력한다.
"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    low, high = 1, 10**6
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2
        cube = mid * mid * mid

        if cube == N:
            ans = mid
            break
        elif cube > low:
            low = mid + 1
        else:
            high = mid - 1
    print(f'#{tc} {ans}')
