T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    small_sequence = []
    big_sequence = []
    sort_list = []

    ai.sort()
    for _ in ai:
        small_sequence.append(_)
    ai.sort(reverse=True)
    for _ in ai:
        big_sequence.append(_)
    for x in range(N):
        sort_list.append(big_sequence[x])
        sort_list.append(small_sequence[x])
        if len(sort_list) == 10:
            break
    
    print(f'#{tc}',*sort_list)
# print(sort_list)
# print(ai)
# print(small_sequence, big_sequence)
