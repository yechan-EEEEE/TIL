# # 1. 노드 클래스
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#
# # 2. 부모-자식 정보
# T = int(input())
# for tc in range(1, T + 1):
#
#     # nums = [2, 1, 2, 5, 1, 6, 5, 3, 6, 4]  # 입력 예시
#     nums = list(map(int, input().split()))  # 나중에 입력으로 바꿀 수도 있음
#     n = max(nums)  # 노드 번호 최대값 (루트 번호도 포함)
#
#     # 3. 트리 연결을 위한 리스트
#     tree = [[] for _ in range(n + 1)]
#
#     # 부모-자식 정보 기록
#     for i in range(0, len(nums), 2):
#         parent = nums[i]
#         child = nums[i + 1]
#         tree[parent].append(child)
#
#     # 4. 노드 객체 생성
#     nodes = [None] + [Node(i) for i in range(1, n + 1)]
#
#     # 5. 실제 트리 연결 (왼쪽, 오른쪽 구분)
#     for parent in range(1, n + 1):
#         kids = tree[parent]
#         if len(kids) >= 1:
#             nodes[parent].left = nodes[kids[0]]
#         if len(kids) == 2:
#             nodes[parent].right = nodes[kids[1]]
# 1. 노드 클래스
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.children = []  # 자식 몇 개든 추가 가능
#
#
# # 2. 부모-자식 정보
# nums = list(map(int, input().split()))  # 입력 예시
# n = max(nums)  # 노드 번호 최대값
#
# # 3. 노드 객체 생성
# nodes = [None] + [Node(i) for i in range(1, n+1)]
#
# # 4. 부모-자식 연결
# for i in range(0, len(nums), 2):
#     parent = nums[i]
#     child = nums[i+1]
#     nodes[parent].children.append(nodes[child])
#
# # 5. 루트 노드 (예제에서는 2가 루트)
# root = nodes[2]
#
# # 확인: root의 자식 번호 출력
# print("루트 자식:", [child.val for child in root.children])


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
