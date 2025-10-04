# T = int(input())
# dxy = [[0, 1], [1, 0]]
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     word_list = [list(map(str, input().strip())) for _ in range(N)]
#     # print(word_list)
#     for i in range(N):
#         for j in range(N):
#             new_list = [None] * M
#             new_list[i] = word_list[i][j]
#             for dx, dy in dxy:
#                 for dist in range(1, M+1):
#                     nx = i + dx * dist
#                     ny = j + dy * dist
#                     if 0 <= nx < N and 0 <= ny < N:
#                         new_list[nx][ny] = word_list[nx][ny]
#         # print(new_list)
# T = int(input())
#
# for tc in range(1, T + 1):
#     n, m = map(int, input().split())
#     word_list = []
#     for _ in range(n):
#         word_list.append(input())
#     print(word_list)
#
#     ans_word = ""
#     for i in range(n):  # 가로 확인
#         wid_word = ""
#         for j in range(0, n - m + 1):  # 글자판 밖으로 안나가게
#             wid_word = word_list[i][j:j + m]  # 문자열 길이만큼 넣어주기
#             if wid_word == wid_word[::-1]:  # 회문인지 검사
#                 ans_word = wid_word  # 회문이면 답에다가 저장
#                 break
#         if ans_word:  # 회문을 찾았다면 break
#             break
#
#     if not ans_word:  # 세로 확인
#         for i in range(n):
#             for j in range(0, n - m + 1):
#                 len_word = ""
#                 for k in range(j, j + m):
#                     len_word += word_list[k][i]
#                 if len_word == len_word[::-1]:
#                     ans_word = len_word
#                     break
#             if ans_word:
#                 break
#
#     print(f"#{tc} {ans_word}")

# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     word_list = []
#     for _ in range(N):
#         word_list.append(input())
#     # print(word_list)
#     answer_word = ""
#     for i in range(N):
#         wid_word = ""
#         for j in range(0, N - M + 1):
#             wid_word = word_list[i][j:j+M]
#             if wid_word == wid_word[::-1]:
#                 answer_word = wid_word
#                 break
#         if answer_word:
#             break
#
#     if not answer_word:
#         for i in range(N):
#             for j in range(0, N - M + 1):
#                 len_word = ""
#                 for k in range(j, j + M):
#                     len_word += word_list[k][i]
#                 if len_word == len_word[::-1]:
#                     answer_word = len_word
#                     break
#             if answer_word:
#                 break
#     print(f"#{tc} {answer_word}")

# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     word_list = []
#     for _ in range(N):
#         word_list.append(input())
#
#     answer_word = ""
#     for i in range(N):
#         wid_word = ""
#         for j in range(0, N - M + 1):
#             wid_word = word_list[i][j:j+M]
#             if wid_word == wid_word[::-1]:
#                 answer_word = wid_word
#                 break
#         if answer_word:
#             break
#
#     if not answer_word:
#         for i in range(N):
#             for j in range(0, N - M + 1):
#                 len_word = ""
#                 for k in range(j, j + M):
#                     len_word += word_list[k][i]
#                 if len_word == len_word[::-1]:
#                     answer_word = len_word
#                     break
#             if answer_word:
#                 break
#
#     print(f'#{tc} {answer_word}')

# T = int(input())

# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     word_list = []
#     for _ in range(N):
#         word_list.append(input())
#     result = ""

#     for i in range(N):
#         wid_word = ""
#         for j in range(0, N - M + 1):
#             wid_word = word_list[i][j:j+M]
#             if wid_word == wid_word[::-1]:
#                 result = wid_word
#                 break
#         if result:
#             break

#     if not result:
#         for i in range(N):
#             for j in range(0, N-M+1):
#                 len_word = ""
#                 for k in range(j, j+M):
#                     len_word += word_list[k][i]
#                 if len_word == len_word[::-1]:
#                     result = len_word
#                     break
#             if result:
#                 break
#     print(f'#{tc} {result}')


# def brute_force(N, M, grid):

#     result = ()
#     for i in range(N):
#         for j in range(N - M + 1):
#             word = grid[i][j:j+M]
#             if word == word[::-1]:
#                 result = ''.join(word)
#                 return result
    
#     for j in range(N):
#         for i in range(N - M + 1):
#             word = []
#             for k in range(M):
#                 word.append(grid[i+k][j])
#             if word == word[::-1]:
#                 result = ''.join(word)
#                 return result
#     return -1


# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     grid = [list(input().strip()) for _ in range(N)]
#     result = brute_force(N, M, grid)
#     print(f'#{tc} {result}')


def brute_force(N, M, grid):
    result = ()

    for i in range(N):
        for j in range(N - M + 1):
            word = grid[i][j:j+M]
            if word == word[::-1]:
                result = ''.join(word)
                return result
    
    for j in range(N):
        for i in range(N - M + 1):
            word = []
            for k in range(M):
                word.append(grid[i+k][j])
            if word == word[::-1]:
                result = ''.join(word)
                return result
    return -1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    result = brute_force(N, M, grid)
    print(f'#{tc} {result}')
