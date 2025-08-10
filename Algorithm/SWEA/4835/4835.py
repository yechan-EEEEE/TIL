'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
v 1 2 3 4 5

이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
답은 12와 6의 차인 6을 출력한다.

입력
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

출력
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력                                                                                                      출력
3                       T
10 3                    N이 정수의 개수 M이 이웃한 값들 몇개를 더할 건가
1 2 3 4 5 6 7 8 9 10                                                                                    #1 21
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821                                                        #2 11088
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176     #3 1090

N은 리스트 갯수고 M은 어떻게 써줘야 할까
M이 i라고 치면 range(m) 반복해서 그 값들 더해줘야 할까?
이걸 처음부터 한칸씩 올라가고
max랑 min 변수 만들어두고 맨 처음 더한 값을 거기 넣어두고 뒤로 가면서 비교해서 크면 max에 넣고 작으면 min에 넣은다음
마지막에 T랑 max - min 출력하기
그러면 일단 둘째 줄에 들어온 친구를 저장해야 하는데 N=정수로 넣어두고 M은 map 써서 나눠둬야겠지?
아 N 정수로 두고 빈 리스트 * N 하는거였지'
for 문으로 리스트 0번 칸부터
'''
'''
T = int(input())
for test_case in range(1,T+1):
    N, M = list(map(int,input().split()))
    # list_num = [0]*N
    # print(list_num)
    input_num = list(map(int,input().split()))
    print(input_num)
    first_num = 0
    for num in range(M):
        first_num += input_num[num]
    max_num = first_num
    min_num = first_num
    print(max_num)
    print(min_num)

    for j in range(N-M+1): # 7 8 9까지 해야되니까 이 자리엔 8이 들와야함 N-M+1 하면 8 20 19일때 1~20까지 더한 값이 들와야되니까
        print(j) # 0~7까지 잘 나와요 그러면 0일 때 0~2,1일 때 1~3 ... 이걸 반복해야 하는데 j일때 j+2까지 근데 다른 경우면 안되니깐
        sum_num = 0
        for k in range(j,j+M): #j=0이고 k는 0 1 2가 될거니깐 sum_num에다가 list_num[k]를 차례대로 더해요?
            sum_num += input_num[k]
        if sum_num > max_num:
            max_num = sum_num
        if sum_num < min_num:
            min_num = sum_num
    result = max_num - min_num
    print(f'#{test_case} {result}', end=" ")
    print()
            #           # 다 더한 값 0으로 해두고 일단
    #         sum_num += input_num[j]
    #         print(sum_num)
    #     if sum_num > max_num:
    #         max_num = sum_num
    #         print(max_num)
    #     if sum_num < min_num:
    #         min_num = sum_num
    #         print(min_num)
    #     # 자 이게 뭐냐 한번 써보면 j가 0일때 0 1 2를 더해야 된단 말이죠? 그리고 이걸 sum에다 넣어보고
    #     # j + M만큼 까지 더해야해요 j일때 j~j+M 까지 더하기
    #     # 0부터 M-1만큼씩 더하기 N-M+1만큼 반복
    #     # list_num[j]부터 list_num[j+M?]까지 더하기 sum_num += 0,1,2
    #     # for k in range(M): #0~M-1까지 반복해서 더해줄거에요 아 여기 바꿔야 되는데 012,123,234,345
    #     #     sum_num = 0
    #     #     sum_num += list_num[k]
    #     #     if sum_num > max_num:
    #     #         max_num = sum_num
    #     #     if sum_num < min_num:
    #     #         min_num = sum_num
    #     result = max_num - min_num
    # print(f'#{test_case} {result}',end=" ")
    # print()
'''
'''
0 1 2 더하려면 
        for j in range(M): # list_num[0]~[M-1] 까지 더해야한다
        j에다가 M의 range만큼 M이 3이면 0 1 2 세번
            sum_num = 0
            더한 값을 일단 0으로 해두고
            for k in range(M): #0~M-1까지 반복해서 더해줄거에요
            k도 0 1 2 세번
            sum_num += list_num[j]
            
            if sum_num > max_num:
                max_num = sum_num
            if sum_num < min_num:
                min_num = sum_num
        result = max_num - min_num
        print(f'#{test_case} {result}',end=" ")

012 하고 123으로 넘어가야 되는데 그러면 어디서 조건을 추가하나
그럼 위에 0~9까지 하는 반복문이 있어야겠네
0~9까지 반복:
지금 위치 +2까지 더하는 걸 반복:
이 값을 max랑 min에다 넣어두고
더한 값이 max보다 크면 max에 넣고
min 보다 작으면 min에다 넣기
그럼 처음에 넣는 건 어디다 쓰지

    0~9까지 반복 :
    그럼 여기다가 첫 max, min을 넣어둬야겠네
        지금 위치 +2까지 더하기 반복 :
        여기 나온 값을 max, min에 입력
result = max - num 하고
밖에다가 출력

'''
# import sys
# sys.stdin = open("input.txt","r")
T = int(input()) # 테스트케이스 개수 입력
for test_case in range(1,T+1): # 테스트 케이스 수 만큼 반복하기
    N, M = list(map(int,input().split())) # 몇개의 수, 구간을 몇개로 할지 받아서 정수로 바꾸고 리스트에다 저장
    input_num = list(map(int,input().split())) # 입력받은 정수들을 쭉 정수로 바꾸고 리스트에다 저장
    first_num = 0
    for num in range(M):
        first_num += input_num[num] # 맨 앞 숫자부터 정해진 구간까지의 첫번째 합을 저장해둠
    max_num = first_num # 첫번째 합을 가장 큰 값, 가장 작은 값이라고 저장
    min_num = first_num 

    for j in range(N-M+1): # 구간을 튀어나가면 안되니까 반복 횟수를 정해줌 1번 케이스에선 10개니깐 6 7 8 9 10 이렇게 6번까지만 반복되게
        sum_num = 0 # 구간합 변수를 0으로 저장해둠 여기다 둬야 구간합 반복이 끝나고 0으로 초기화됨
        for k in range(j,j+M): # 
            sum_num += input_num[k]
        if sum_num > max_num:
            max_num = sum_num
            # max_num = max(max_num,sum_num) # 맥스는 이렇게 쓰면 좋음 비교 안하고
        if sum_num < min_num:
            min_num = sum_num
            # min_num = min(min_num,sum_num) # min도 이렇게 쓰기 비교 안쓰고
    result = max_num - min_num
    print(f'#{test_case} {result}', end=" ")
    print()












