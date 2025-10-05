import heapq

T = int(input())
for x in range(1, T + 1):
    N = int(input())
    heap = []
    result = []

    for i in range(N):
        function_input = list(map(int, input().split()))

        if len(function_input) == 2:
            heapq.heappush(heap, -function_input[1])
        if len(function_input) == 1:
            if heap:
                a = str(-heapq.heappop(heap))
                result.append(a)
            elif not heap:
                result.append('-1')

    print(f'#{x}', end=' ')
    print(*result)
