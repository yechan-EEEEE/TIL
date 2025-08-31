'''
2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
3
3 8 
7 7 
369 123  
#1 <
#2 =
#3 >
'''
T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())
    result = []
    if A > B:
        result.append('>')
    elif A == B:
        result.append('=')
    elif A < B:
        result.append('<')
    answer = ''.join(result)
    print(f'#{tc} {answer}')