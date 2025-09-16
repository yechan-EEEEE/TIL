V = int(input())
edges = list(map(int, input().split()))

tree = [[] for _ in range(V+1)]
for i in range(0, len(edges), 2):
    tree[edges[i]].append(edges[i+1])

# 스택으로 하기
def pre_order(root):  # 전위 VLR
    stack = [root]
    while stack:
        node = stack.pop()
        print(node, end=' ')
        # 오른쪽 자식 먼저 넣고 왼쪽 자식 나중에 넣음
        if len(tree[node]) >= 2:
            stack.append(tree[node][1])
        if len(tree[node]) >= 1:
            stack.append(tree[node][0])


def in_order(root):  # 중위 LVR
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = tree[node][0] if len(tree[node]) >= 1 else None
        else:
            node = stack.pop()
            print(node, end=' ')
            node = tree[node][1] if len(tree[node]) >= 2 else None


def post_order(root):  # 후위 LRV
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if len(tree[node]) >= 1:
            stack1.append(tree[node][0])
        if len(tree[node]) >= 2:
            stack1.append(tree[node][1])
    while stack2:
        print(stack2.pop(), end=' ')

root = 1
pre_order(root)
print()
in_order(root)
print()
post_order(root)



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

