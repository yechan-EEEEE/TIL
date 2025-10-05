import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    heap = []
    for i in numbers:
        heapq.heappush(heap, i)
    result = 0
    node = N

    while True:
        parent_node = node // 2
        result += heap[parent_node-1]
        node = parent_node
        if node == 1:
            break
    
    print(f'#{tc} {result}')
