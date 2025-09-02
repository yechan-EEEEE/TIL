T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    wi.sort(reverse=True)  # 무거운 컨테이너부터
    ti.sort(reverse=True)  # 큰 트럭부터

    used = [False] * N  # 컨테이너 사용 여부 체크
    max_weight = 0

    for t in ti:  # 각 트럭에 대해
        for i in range(N):
            if not used[i] and wi[i] <= t:  # 아직 안 썼고, 트럭이 감당 가능
                max_weight += wi[i]
                used[i] = True
                break  # 한 트럭엔 하나만 싣기

    print(f'#{tc} {max_weight}')