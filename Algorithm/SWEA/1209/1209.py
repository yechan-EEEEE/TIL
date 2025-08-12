"""
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
다음과 같은 5X5 배열에서 최댓값은 29이다.

[제약 사항]
총 10개의 테스트 케이스가 주어진다.
배열의 크기는 100X100으로 동일하다.
각 행의 합은 integer 범위를 넘어가지 않는다.
동일한 최댓값이 있을 경우, 하나의 값만 출력한다.

[입력]
각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

[출력]
# 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.


입력                  출력
1
4 4 3 2 1
2 2 1 6 5
3 5 4 6 7
4 2 5 9 7
8 1 9 5 6            #1 29
"""
for num in range(1,11):
    T = int(input())
    N = [list(map(int,input().split()))for _ in range(100)]
# print(N)
    max_sum = 0  # 행 최대값
    sum_num = 0  # 각 행마다 더한 값, 뒤에서 초기화
    max_sum1 = 0  # 열 최대값
    sum_num1 = 0  # 각 열마다 더한 값, 뒤에서 초기화
    max_sum2 = 0  # 정 대각선 값
    max_sum3 = 0  # 역 대각선 값
    for i in range(100):  # 행 더하는 곳
        for j in range(100):
            sum_num += N[i][j]
        if sum_num > max_sum:
            max_sum = sum_num
            sum_num=0
        elif sum_num < max_sum:
            sum_num=0
    for k in range(100):  # 열 더하는 곳
        for l in range(100):
            sum_num1 += N[l][k]
            # print(sum_num1)
        if sum_num1 > max_sum1:
            max_sum1 = sum_num1
            # print(max_sum1)
            sum_num1 = 0
        elif sum_num1 < max_sum1:
            sum_num1 = 0
    for m in range(100):  # 정 대각선 더하는 곳
        max_sum2 += N[m][m]
    for n in range(100):  # 역 대각선 더하는 곳
        max_sum3 += N[n][99-n]
    result1 = max(max_sum, max_sum1)
    result2 = max(result1,max_sum2)
    result = max(result2,max_sum3)
    print(f'#{T} {result}')
    print(max_sum)
    print(max_sum1)
    print(max_sum2)
    print(max_sum3)