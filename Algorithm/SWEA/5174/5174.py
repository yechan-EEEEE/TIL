T = int(input())

<<<<<<< HEAD
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    idx = list(map(int, input().split()))
    m = max(idx)
    tree = [[] for _ in range(m+1)]
    nod_cnt = 1

    for i in range(0, len(idx), 2):
        tree[idx[i]].append(idx[i+1])

    stack = [N]
    nod_cnt = 0

    while stack:
        node = stack.pop()
        nod_cnt += 1
        stack.extend(tree[node])

    print(f'#{tc} {nod_cnt}')
=======

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# 입력
nums = list(map(int, input().split()))
edges = [(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]
print(edges)
# 모든 노드 번호 모아서 딕셔너리 생성
all_nodes = set()
for p, c in edges:
    all_nodes.add(p)
    all_nodes.add(c)

nodes = {v: TreeNode(v) for v in all_nodes}
print(nodes)

# 간선(부모-자식 관계) 처리
for p, c in edges:
    if nodes[p].left is None:       # 왼쪽 비었으면 왼쪽
        nodes[p].left = nodes[c]
    else:                           # 아니면 오른쪽
        nodes[p].right = nodes[c]
print(nodes)

# 루트 찾기 (부모로만 등장한 노드 - 자식으로만 등장한 노드)
parents = {p for p, _ in edges}
print(parents)
children = {c for _, c in edges}
print(children)
root_candidates = parents - children
print(root_candidates)
root = nodes[root_candidates.pop()]
print(root)

# 확인용 출력 (전위 순회)
def preorder(node):
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)

print("Preorder:", preorder(root))
>>>>>>> 260e1bad911139d7de0143f47d19937a7a6be4a8
