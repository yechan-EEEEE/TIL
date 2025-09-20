V = int(input())
edges = list(map(int, input().split()))

tree = [[] for _ in range(V+1)]
for i in range(0, len(edges), 2):
    tree[edges[i]].append(edges[i+1])


# 스택으로 하기
def pre_order(root):  # VLR
    stack = [root]  # 루트부터 시작
    while stack:
        node = stack.pop()  # 현재 노드 꺼내기
        print(node, end=' ')  # 현재 노드 방문

        # 오른쪽 자식이 있으면 스택에 넣기
        if len(tree[node]) >= 2:
            stack.append(tree[node][1])

        # 왼쪽 자식이 있으면 스택에 넣기
        if len(tree[node]) >= 1:
            stack.append(tree[node][0])


def in_order(root):  # LVR
    stack = []      # 방문할 노드를 담아둘 스택
    node = root     # 현재 노드 = 루트부터 시작

    while stack or node:
        if node:
            # 왼쪽 끝까지 내려가기 위해 현재 노드를 스택에 저장
            stack.append(node)

            # 왼쪽 자식이 있으면 계속 왼쪽으로 이동
            if len(tree[node]) >= 1:
                node = tree[node][0]
            else:
                node = None
        else:
            # 더 이상 왼쪽 자식이 없으면 스택에서 꺼내 방문
            node = stack.pop()
            print(node, end=' ')

            # 오른쪽 자식이 있으면 오른쪽으로 이동
            if len(tree[node]) >= 2:
                node = tree[node][1]
            else:
                node = None


def post_order_two_stack(root):  # LRV
    stack1 = [root]   # 첫 번째 스택: 노드를 담고 탐색용
    stack2 = []       # 두 번째 스택: 후위 순회를 위해 역순으로 저장

    # 첫 번째 스택이 빌 때까지 반복
    while stack1:
        node = stack1.pop()   # stack1에서 맨 위 노드 꺼내기
        stack2.append(node)   # 꺼낸 노드를 stack2에 넣음

        # 왼쪽 자식이 있으면 stack1에 추가
        if len(tree[node]) >= 1:
            stack1.append(tree[node][0])

        # 오른쪽 자식이 있으면 stack1에 추가
        if len(tree[node]) >= 2:
            stack1.append(tree[node][1])

    # stack2에는 후위 순회 결과의 역순이 들어 있음
    while stack2:
        print(stack2.pop(), end=' ')


root = 1
pre_order(root)
print()
in_order(root)
print()
post_order_two_stack(root)


# def pre_ans(root):  # 전위
#     if root:
#         print(root.val, end=' ')
#         pre_ans(root.left)
#         pre_ans(root.right)


# def cen_ans(root):  # 중위
#     if root:
#         cen_ans(root.left)
#         print(root.val, end=' ')
#         cen_ans(root.right)


# def pos_ans(root):  # 후위
#     if root:
#         pos_ans(root.left)
#         pos_ans(root.right)
#         print(root.val, end=' ')


# # 전위
# def pre_rec(node):
#     if node:
#         print(node, end=' ')
#         if len(tree[node]) >= 1:
#             pre_rec(tree[node][0])
#         if len(tree[node]) >= 2:
#             pre_rec(tree[node][1])


# # 중위
# def in_rec(node):
#     if node:
#         if len(tree[node]) >= 1:
#             in_rec(tree[node][0])
#         print(node, end=' ')
#         if len(tree[node]) >= 2:
#             in_rec(tree[node][1])


# # 후위
# def post_rec(node):
#     if node:
#         if len(tree[node]) >= 1:
#             post_rec(tree[node][0])
#         if len(tree[node]) >= 2:
#             post_rec(tree[node][1])
#         print(node, end=' ')

