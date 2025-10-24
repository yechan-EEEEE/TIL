"""
8x8 평면 글자판에서 제시된 길이를 가진 회문의 개수를 구하라.
각 칸의 들어가는 글자는 'A', 'B', 'C' 중 하나이다.

ABA도 회문이며, ABBA도 회문이다. A 또한 길이 1짜리 회문이다.

가로 또는 세로로 이어진 회문의 개수만 센다.
총 10개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이가 주어지며, 다음 줄에 8x8 크기의 글자판이 주어진다.
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 개수를 출력한다.

4
CBBCBAAB
CCCBABCB
CAAAACAB
BACCCCAC
AABCBBAC
ACAACABC
BCCBAABC
ABBBCCAA
            #1 12
4
BCBBCACA
BCAAACAC
ABACBCCB
AACBCBCA
ACACBAAA
ACCACCCB
AACAAABA
CACCABCB
            #2 10

오른쪽이랑 아래로 4개씩 확인해서 회문이면 카운트 1 하면 되네
스택에 넣는게 나은가
스택에 넣고 길이 반 만큼
아예 슬라이싱 이구만
"""
T = 10
len_arr = 8
for tc in range(1, T + 1):
    len_pal = int(input())
    arr = [list(map(str, input().strip())) for _ in range(len_arr)]
    cnt = 0

    for i in range(len_arr):
        for j in range(len_arr):
            if j + len_pal <= len_arr:
                check_pal_w = arr[i][j : j + len_pal]
                if check_pal_w == check_pal_w[::-1]:
                    cnt += 1
            if i + len_pal <= len_arr:
                check_pal_h = ""
                for k in range(len_pal):
                    check_pal_h += arr[i + k][j]
                if check_pal_h == check_pal_h[::-1]:
                    cnt += 1
    print(f'#{tc} {cnt}')
