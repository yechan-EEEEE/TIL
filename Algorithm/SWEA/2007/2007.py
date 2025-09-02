# T = int(input())

# for tc in range(1, T + 1):
#     arr = str(input())
#     cnt = 0
#     arr_test = []
#     while True:
#         for i in arr:
#             arr_test.append(i)
#         for i in arr_test:
#             start_word = []
#             if start_word[0] == arr_test[i]:

T = int(input())

for tc in range(1, T + 1):
    arr = list(input().strip())   # 문자열을 리스트로 변환
    result = 0

    for i in range(1,11):
        pattern = arr[:i]    # 후보 마디

        repeated = []
        # 30 이상 길이가 되도록 패턴 반복
        while len(repeated) < 30:
            repeated.extend(pattern)

        # 앞 30글자만 잘라 비교
        if repeated[:30] == arr:
            result = i
            break

    print(f"#{tc} {result}")
T = int(input())
for tc in range(1, T + 1):
    string = list(input())
    s = ''
     
    for i in range(30):
        if string[0:i+2] == string[i+2:i+4+i] :
             
            s = string[0:i+2]
            break
         
    print(f"#{tc} {len(s)}")