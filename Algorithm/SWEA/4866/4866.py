"""

주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.

입력
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.

출력
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력                                  출력

3
print('{} {}'.format(1, 2))          #1 1
N, M = map(int, input().split())     #2 1
print('#{} {}'.format(tc, find())    #3 0

"""
# # 괄호가 제대로 짝이 맞는 지를 확인하는 함수
# def check_match(expression):
#     # 짝이 맞는 지를 볼 때는 어떤 자료구조를 쓴다고 했어요 ?
#     # Stack => 후입 선출
#     stack = []  # 빈 리스트로 초기화
#     # key => 닫힌 괄호
#     # value => 열린 괄호
#     # key 로 접근하면, 그거에 매칭되어야 할 value를 반환해준다.
#     matching_dict = {
#         ')': '(',
#         '}': '{',
#         ']': '['
#     }
#
#     # 주어진 문자열(expression)을 순회하면서, 괄호의 종류에 따라 push, pop을 진행하면서 비교
#     for char in expression:
#         # 여는 괄호가 나오면, 바로 스택에 넣는다.
#         if char in matching_dict.values():
#             stack.append(char)
#         # 닫힌 괄호가 나오면, 스택에 pop 하고 같은 괄호인 지 비교한다.
#         elif char in matching_dict.keys():
#             # 스택에서 꺼낸다....! 그리고 비교한다..!
#             # 스택이 비어있으면 끝낸다.
#             if not stack:
#                 return False
#
#             # 비어있지 않으니까 꺼냈어요.
#             # 짝이 맞는지 확인해야한다.
#             # 현재 여기서 char는 닫힌 괄호에요 => key 값으로 넣으면
#             # => 이 닫힌 괄호에 매칭되어야 하는 여는 괄호가 나옵니다.
#             if stack[-1] != matching_dict[char]:
#                 return False
#
#             # 스택이 비어있지도 않고,짝도 맞는 경우
#             stack.pop()
#
#     if not stack:  # 스택이 안 비었어? 그러면 .. 열린 괄호가 짝이 없다는 소리에요
#         return True
#
#     return False
#
# examples = ["print('{} {}'.format(1, 2))", "N, M = map(int, input().split())", "print('#{} {}'.format(tc, find())"]
# for ex in examples:
#     if check_match(ex):
#         print(f"{ex} 는 올바른 괄호")
#     else:
#         print(f"{ex} 는 올바르지 않은 괄호")

# T = int(input())

# for tc in range(1, T + 1):
#     # s = list(map(str, input().strip()))
#     s = list(input().strip())
#     sum_num = 0
#     result = 0
#     for i in range(0, len(s)):
#         if s[i] == '(' or s[i] == '{' or s[i] == '[':
#             sum_num += 1
#         elif s[i] == ')' or s[i] == '}' or s[i] == ']':
#             sum_num -= 1
#     if sum_num == 0:
#         result = 1
#     else:
#         result = 0
#     print(f'#{tc} {result}')

# T = int(input())

# for tc in range(1, T + 1):
#     s = list(input().strip())
#     stack = []
#     result = 1  # 기본값: 올바르다고 가정

#     # 괄호 짝 정의
#     pair = {')': '(', '}': '{', ']': '['}

#     for ch in s:
#         if ch in '({[':  # 여는 괄호면 스택에 push
#             stack.append(ch)
#         elif ch in ')}]':  # 닫는 괄호면
#             if not stack or stack[-1] != pair[ch]:  # 스택이 비었거나 짝이 안 맞으면
#                 result = 0
#                 break
#             stack.pop()  # 짝 맞으면 pop
    
#     # 다 돌고 나서 스택이 비어있지 않으면 올바르지 않음
#     if stack:
#         result = 0

#     print(f'#{tc} {result}')
# T = int(input())

# for tc in range(1, T + 1):
#     sentence = list(input().strip())
#     stack = []
#     result = 1  # 올바르다고 가정
#     match = {')':'(', '}':'{', ']':'['}  # 딕셔너리에 맞는 짝끼리 맺어줌

#     for i in sentence:
#         if i in '({[':  # 여는 괄호가 들어오면 스택에다 append, 맨 뒤로 들어감
#             stack.append(i)
#         elif i in ')}]':  # 닫는 괄호가 들어올 때
#             if not stack or stack[-1] != match[i]:  # 스택이 비어있거나, 마지막에 들어온 여는 괄호랑 방금 들어온 닫는 괄호의 value가 다르다면
#                 result = 0  # 올바르지 않은 문장이니 0 하고 탈출
#                 break
#             stack.pop()  # 아니라면 마지막에 들어온 여는 괄호 뽑아내기

#     if stack:  # 끝까지 했는데 스택에 값이 남아있으면 올바르지 않으니 0
#         result = 0
#     print(f'#{tc} {result}')


# T = int(input())

# for tc in range(1, T + 1):
#     s = list(input().strip())
#     stack = []
#     result = 1
#     match = {')' : '(', '}' : '{', ']' : '['}

#     for i in s:
#         if i in '({[':
#             stack.append(i)
#         elif i in ')}]':
#             if not stack or stack[-1] != match[i]:
#                 result = 0
#                 break
#             stack.pop()
#     if stack:
#         result = 0
#     print(f'#{tc} {result}')


# T = int(input())
#
# for tc in range(1, T + 1):
#     sentence = list(input().strip())
#     stack = []
#     result = 1
#     match = {')' : '(', '}' : '{', ']' : '['}
#
#     for i in sentence:
#         if i in '({[':
#             stack.append(i)
#         elif i in ')}]':
#             if not stack or stack[-1] != match[i]:
#                 result = 0
#                 break
#             stack.pop()
#     if stack:
#         result = 0
#     print(f'#{tc} {result}')

# T = int(input())
#
# for tc in range(1, T + 1):
#     input_text = list(input().strip())
#     stack = []
#     result = 1
#     match_dict = {')': '(', '}': '{', ']': '['}
#     for i in input_text:
#         if i in '({[':
#             stack.append(i)
#         elif i in ')}]':
#             if not stack or stack[-1] != match_dict[i]:
#                 result = 0
#                 break
#             stack.pop()
#     if stack:
#         result = 0
#     print(f'#{tc} {result}')

T = int(input())

for tc in range(1, T + 1):
    input_text = list(input().strip())
    stack = []
    result = 1
    match_dict = {')': '(', '}': '{', ']': '['}

    for i in input_text:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack or stack[-1] != match_dict[i]:
                result = 0
                break
            stack.pop()
    if stack:
        result = 0
    print(f'#{tc} {result}')


















