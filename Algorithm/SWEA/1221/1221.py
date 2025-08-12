'''
숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

[입력]
입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백 문자 후 테스트 케이스의 길이가 주어진다.
테스트 케이스의 길이란, 문자열의 글자수가 아닌 단어의 갯수를 말한다.
그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.

'''

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(str, input().split()))
    input_num = []
    input_num = list(map(str, input().split(' ')))
    arr_num = [0]*10
    for i in range(int(M)):
        if input_num[i] == 'ZRO':
            arr_num[0] += 1
        elif input_num[i] == 'ONE':
            arr_num[1] += 1
        elif input_num[i] == 'TWO':
            arr_num[2] += 1
        elif input_num[i] == 'THR':
            arr_num[3] += 1
        elif input_num[i] == 'FOR':
            arr_num[4] += 1
        elif input_num[i] == 'FIV':
            arr_num[5] += 1
        elif input_num[i] == 'SIX':
            arr_num[6] += 1
        elif input_num[i] == 'SVN':
            arr_num[7] += 1
        elif input_num[i] == 'EGT':
            arr_num[8] += 1
        elif input_num[i] == 'NIN':
            arr_num[9] += 1
    print(N)
    print('ZRO ' * arr_num[0], end='')
    print('ONE ' * arr_num[1], end='')
    print('TWO ' * arr_num[2], end='')
    print('THR ' * arr_num[3], end='')
    print('FOR ' * arr_num[4], end='')
    print('FIV ' * arr_num[5], end='')
    print('SIX ' * arr_num[6], end='')
    print('SVN ' * arr_num[7], end='')
    print('EGT ' * arr_num[8], end='')
    print('NIN ' * arr_num[9], end='')
    print()





