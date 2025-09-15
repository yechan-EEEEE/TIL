n = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(n+1)]  # 1부터 붙이려고 n+1
print(f'tree={tree}')

for i in range(0, len(nums), 2):  # 부모 자식 순서로 나오니까 2칸씩
    idx = nums[i]  # 부모 정점
    val = nums[i+1]  # 자식노드 왼쪽 오른쪽
    tree[idx].append(val)  # 부모 칸에다 왼쪽 오른쪽 넣어주기
print(f'tree={tree}')


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


nodes = [None] + [TreeNode(i) for i in range(1, n+1)]
print(f'nodes={nodes}')

for idx in range(1, n+1):
    kids = tree[idx]
    print(f'kids={kids}')
    if len(kids) >= 1:  # 왼쪽
        nodes[idx].left = nodes[kids[0]]
    if len(kids) == 2:  # 오른쪽
        nodes[idx].right = nodes[kids[1]]


def pre_ans(root):  # 전위
    if root:
        print(root.val, end=' ')
        pre_ans(root.left)
        pre_ans(root.right)


def cen_ans(root):  # 중위
    if root:
        cen_ans(root.left)
        print(root.val, end=' ')
        cen_ans(root.right)


def pos_ans(root):  # 후위
    if root:
        pos_ans(root.left)
        pos_ans(root.right)
        print(root.val, end=' ')


root = nodes[1]

pre_ans(root)
print()
cen_ans(root)
print()
pos_ans(root)
print()