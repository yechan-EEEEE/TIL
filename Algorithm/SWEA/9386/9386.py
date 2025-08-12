
# T = int(input())
#
# for test_case in range(1,T+1):
#     N = int(input())
#     line_num = list(map(int,input().strip()))
#     # print(line_num)
#     con_num = 0 #이어지고 있는 1의 수
#     max_num = 0 #1이 이어진 경우 최대값
#     for i in range(N):
#         # print(i)
#         if line_num[i] == 1: #들어온 리스트 i번이 1이면
#             con_num += 1    #이어지고 있던 1의 수에다 1씩 더해줘요
#             if con_num > max_num: #이 수가 최대값보다 크면?
#                 max_num = con_num #최대값을 갱신해줘요
#             # print(con_num)
#         elif line_num[i] == 0: #i번이 0이면?
#             if  con_num > max_num: #0인데 지금까지 이어졌던 1의 값이 max에 들어있던 값보다 크면
#                 max_num = con_num #max_num을 갱신해주고
#             # print(max_num)
#             con_num = 0 #con을 초기화해주고 다시 반복을 시작해요
#
#     print(f'#{test_case} {max_num}')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     input_num = list(input().strip(' '))
#     # print(input_num)
#     # print(type(input_num[0]))
#     max_sum = 0
#     for i in range(N):
#         sum_num = 0
#         for j in range(N):
#             if input_num[j] == '1':
#                 sum_num += 1
#                 print(sum_num)
#                 max_sum = sum_num
#                 print(max_sum)
#             elif input_num[j] == '0':
#                 sum_num = 0
#     print(f'#{tc} {max_sum}')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    input_num = list(input().strip(' '))
    print(input_num)
    # print(type(input_num[0]))
    max_sum = 0
    sum_num = 0
    for i in range(N):
        if input_num[i] == '1':
            sum_num += 1
            if sum_num > max_sum:
                max_sum = sum_num
            # print(max_sum)
        elif input_num[i] == '0':
            sum_num = 0
    print(f'#{tc} {max_sum}')
































