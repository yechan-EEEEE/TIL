# for tc in range(1, 11):
#     N = int(input())
#     height = list(map(int, input().split()))
#     view_point = 0
#
#     for i in range(2, N-2):
#         top_height = 0
#         if i-2 < 0 and i+2 < N:
#             for j in range(5):
#                 print(height[i-j], height[i])
#                 if height[i-j] != height[i] and height[i-j] < height[i]:
#                     a = height[i-j]
#                     print(a)
#                     top_height = max(top_height, a)
#                     print(top_height)
#                 b = height[i] - top_height
#                 print(height[i], top_height)
#             view_point += b
#     print(f'#{tc} {view_point}')
for tc in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))
    view_point = 0

    for i in range(2, N-2):  # 왼쪽 오른쪽 2칸은 0이니깐 제외
        side_height = max(height[i-2], height[i-1], height[i+1], height[i+2])  # 옆 2칸 애들의 높이 중 가장 높은 값
        if side_height < height[i]:  # 지금 높이가 옆 높이보다 높으면
            view_point += height[i] - side_height  # 차이 만큼 view_point 확보

    print(f'#{tc} {view_point}')
