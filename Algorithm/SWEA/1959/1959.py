# T = int(input())

# for num in range(1, T + 1):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))

#     # A가 더 짧은 쪽이 되도록 정렬
#     if N > M:
#         A, B = B, A
#         N, M = M, N

#     max_sum = 0

#     for i in range(M - N + 1):
#         temp_sum = 0
#         for j in range(N):
#             temp_sum += A[j] * B[i + j]
#         max_sum = max(max_sum, temp_sum)

#     print(f"#{num} {max_sum}")

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int,input().split())
#     Ai = list(map(int,input().split()))
#     Bj = list(map(int,input().split()))
#     max_sum  = 0
#     if N > M :  # M, Bj 를 무조건 큰 값으로 바꾸기
#         N, M = M, N
#         Ai, Bj = Bj, Ai
#     for i in range(M-N+1):  # 긴 쪽 - 짧은쪽 만큼 반복(위치 옮기기)
#         cur_sum = 0
#         for j in range(N):  # 짧은 쪽 길이만큼 서로 곱하기 반복
#             cur_sum += Ai[j] * Bj[i+j]
#         max_sum = max(max_sum, cur_sum)
#     print(f'#{tc} {max_sum}')

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    max_sum = 0

    if N > M:
        N, M = M, N
        Ai, Bj = Bj, Ai

    for i in range(M-N+1):
        cur_sum = 0
        for j in range(N):
            cur_sum += Ai[j] * Bj[i+j]
        max_sum = max(max_sum, cur_sum)
    
    print(f'#{tc} {max_sum}')