T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    result = 0

    for i in B:
        l, r = 0, N - 1
        dir = 0
        found = False
        valid = True

        while l <= r:
            m = (l+r) // 2
            if A[m] == i:
                found = True
                break
            elif A[m] < i:
                new_dir = 1
                if dir == new_dir:
                    valid = False
                    break
                dir = new_dir
                l = m + 1
            else:
                new_dir = -1
                if dir == new_dir:
                    valid = False
                    break
                dir = new_dir
                r = m - 1
        
        if found and valid:
            result += 1
    
    print(f'#{tc} {result}')
