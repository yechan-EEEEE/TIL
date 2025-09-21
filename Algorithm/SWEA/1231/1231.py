def in_order(root):  # LVR
    stack = []      # 방문할 노드를 담아둘 스택
    node = root     # 현재 노드 = 루트부터 시작
    result = []

    while stack or node:
        if node:
            # 왼쪽 끝까지 내려가기 위해 현재 노드를 스택에 저장
            stack.append(node)

            # 왼쪽 자식이 있으면 계속 왼쪽으로 이동
            if len(tree[node]) >= 3:
                node = int(tree[node][2])  # 문자열 형식으로 들와있어서 int로 바꿔줘야함
            else:
                node = None
        else:
            # 더 이상 왼쪽 자식이 없으면 스택에서 꺼내 방문
            node = stack.pop()
            result.append(tree[node][1])

            # 오른쪽 자식이 있으면 오른쪽으로 이동
            if len(tree[node]) >= 4:
                node = int(tree[node][3])
            else:
                node = None
    return ''.join(result)


for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    for i in range(1, N+1):
        # tree[i].extend(input().split())  # 1 W 2 3 처럼 여러 형식 동시에 들어와서 그냥 집어넣기
        tree[i] = input().split()
    print(f'#{tc} {in_order(1)}')