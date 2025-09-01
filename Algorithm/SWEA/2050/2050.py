'''
알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.
'''
alphabet = str(input())
result = []
for i in alphabet:
    if i == 'A':
        result.append('1')
    if i == 'B':
        result.append('2')
    if i == 'C':
        result.append('3')
    if i == 'D':
        result.append('4')
    if i == 'E':
        result.append('5')
    if i == 'F':
        result.append('6')
    if i == 'G':
        result.append('7')
    if i == 'H':
        result.append('8')
    if i == 'I':
        result.append('9')
    if i == 'J':
        result.append('10')
    if i == 'K':
        result.append('11')
    if i == 'L':
        result.append('12')
    if i == 'M':
        result.append('13')
    if i == 'N':
        result.append('14')
    if i == 'O':
        result.append('15')
    if i == 'P':
        result.append('16')
    if i == 'Q':
        result.append('17')
    if i == 'R':
        result.append('18')
    if i == 'S':
        result.append('19')
    if i == 'T':
        result.append('20')
    if i == 'U':
        result.append('21')
    if i == 'V':
        result.append('22')
    if i == 'W':
        result.append('23')
    if i == 'X':
        result.append('24')
    if i == 'Y':
        result.append('25')
    if i == 'Z':
        result.append('26')
answer = " ".join(result)
print(answer)