
T = int(input())

for tc in range(1, T + 1):
    arr = list(map(str, input()))
    result = []
    r_1 = []
    r2 = ''
    mirror_dic = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}
    for i in arr:
        result.append(i)
    for j in range(len(arr)):
        a = result.pop()
        b = mirror_dic[a]
        r_1.append(b)

    r2 = (''.join(r_1))
    print(f'#{tc} {r2}')
