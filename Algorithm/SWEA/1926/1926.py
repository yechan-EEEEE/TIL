'''
3 6 9 게임을 프로그램으로 제작중이다.게임 규칙은 다음과 같다.
1. 숫자 1부터 순서대로 차례대로 말하되, “3” “6” “9” 가 들어가 있는 수는 말하지 않는다.

1 2 - 4 5 - 7 8 - …

2. "3" "6" "9" 가 들어가있는 수를 말하지 않는대신, 박수를 친다.이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야한다.
예를들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야한다.

입력으로 정수 N이 주어졌을 때, 1~N까지의 숫자를 게임 규칙에 맞게 출력하는 프로그램을 작성하라.

박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.

여기서 주의해야 할 것은 박수 한 번 칠 때는 - 이며, 박수를 두 번 칠 때는 - - 가 아닌 -- 이다.

[제약사항]
N은 10 이상 1, 000 이하의 정수이다.(10 ≤ N ≤ 1, 000)

[입력]

입력으로 정수 N이 주어진다.

[출력]
1 ~ N까지의 숫자를 게임 규칙에 맞게 출력한다.
# '''
# string = [] # 빈 칸 만들어두고
# N = int(input()) # 입력을 받고
# for i in range(1, N + 1): # 1부터 입력받은 수까지 반복
#     a = str(i) # 입력받은 수를 str로 바꾸고
#     b = ' '.join(a) # str이 2글자 이상이면 숫자 사이에 ' ' 를 넣어주고
#     c = b.count('3') # b 안에 3이 있으면 d + 1
#     d = b.count('6') # b 안에 6이 있으면 e + 1
#     e = b.count('9') # b 안에 9가 있으면 f + 1
#     f = c + d + e
#     if f == 1: # 3개 합쳐서 1이면 3,6,9 중에 하나만 있으니까 - 출력
#         string.append('-') # 처음 만든 빈 리스트 안에 - 넣어주기
#     elif f == 2: # 3개 합쳐서 2면 3,6,9 중에 2개가 있는 거니까 -- 출력
#         string.append('--') # 처음 만든 빈 리스트에 -- 넣어주기
#     elif f == 3: # 3개 합쳐서 3이면 세자리 수가 다 3,6,9인 거니까 --- 출력
#         string.append('---') # 처음 만든 빈 리스트에 --- 넣어주기
#     elif f == 0: # 3개 합쳐서 0이면 아무 것도 아니니깐
#         string.append(str(i)) # 지금 자기 숫자 빈 리스트에 추가
# result = " ".join(string) # 숫자들 사이에 ' ' 넣어주기
# print(result)
# N = int(input())

# for i in range(1, N+1):
#     if '3' in str(i) or '6' in str(i) or '9' in str(i):
#         clap_count = str(i).count('3') + str(i).count('6') + str(i).count('9')
#         print('-' * clap_count, end=' ')
#     else:
#         print(i, end=' ')
'''
        if d==
    for e in d :
        if d == 1:
            print('-')
        elif d == 2:
            print('--')
        elif d == 3:
            print('---')
        else:
            print(i)
    print(d)

    for x in str(i):
        a = int(x)
        if a == 3 or a == 6 or a == 9:
            print("-")
n = str(N)
print(n[0],n[1])


    count_num = 0
num = list(map(int,input().split()))
num1 = ' '.join(num)
if 3 in num:
    print('-')
x = [13]
' '.join(x)
if 3 in x:
    print('-')
y = x.split
M = ((x.count(3))+(x.count(6))+(x.count(9)))
print(x)
num = str(input())
print(num[0],num[1])
' '.join(x)' '.join(x)
X = int(input())
print(X)
x = str(X)
print(x)
a = ' '.join(x)
print(a[0])
print(type(a[0]))
b = int(a[0])
c = int(a[0][0])
d = int(a[2])
print(type(b))
if b == 3 or b == 6 or b == 9:
    print('-')
    if c == 3 or c == 6 or c == 9:
        print('--')
print(f'{a}')
'''
N = int(input())
for i in range(1, N+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')
        print('-' * cnt, end=' ')
    else:
        print(i, end=' ')