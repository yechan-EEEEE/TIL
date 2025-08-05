'''
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

input:
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
output:
#1 630739
#2 740510
#3 838110


'''
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1): # 1부터 T만큼 반복
#     x = int(input()) # 입력한 양수의 개수를 int형으로 x에 넣는다
#     a = list(map(int,input().split()))
#     # input으로 받으면 str임, split을 해서 하나씩 나눠줌, list(map(int)) 나눠준 애들을 int로 바꾸고 list에 넣음
#     max_num = a[0] # a의 첫번째 값 max_num에 넣기
#     min_num = a[0] # a의 첫번째 값 min_num에 넣기

#     for n in a: # n이라는 임의변수에다가 a 값 넣는 걸 반복
#         if n > max_num: # a의 첫번째 값이 max_num 보다 크면
#             max_num = n # a의 첫번째 값을 max_num 에 넣기
#         if n < min_num: # a의 첫번째 값이 min_num 보다 작으면
#             min_num = n # a의 첫번째 값을 min_num 에 넣기
#     Answer = max_num - min_num # Answer 에 위 if 문으로 만든 최대값 - 최소값 결과 넣기
#     print(f'#{test_case} {Answer}') # f스트링으로 
# a = input()
# b = (input().split())
# c = list(map(int,input().split()))
# print(a)
# print(b)
# print(c)
# 위에 안보고 만들어보자

'''
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
'''
T = int(input())

for test_case in range(1,T+1):
    Number = int(input())






























