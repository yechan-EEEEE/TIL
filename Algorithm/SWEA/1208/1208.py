import sys
sys.stdin = open("input (11).txt", "r")

for tc in range(1, 11):
    dump = int(input())
    box_height = list(map(int, input().split()))
    result = 0

    for i in range(dump):
        box_height.sort()
        box_height[0] += 1
        box_height[-1] -= 1
        box_height.sort()
        if box_height[-1] - box_height[0] == 0 or box_height[-1] - box_height[0] == 1:
            break

    result = box_height[-1] - box_height[0]
    print(f'#{tc} {result}')



