import bisect

def change_with_array(change, coins):
    result = []
    for c in coins:  # 큰 단위부터 순회
        cnt, change = divmod(change, c)
        result.append(cnt)
    return result


def change_with_binary_search(change, coins):
    coins = sorted(coins)  # 오름차순 정렬 필요
    result = [0] * len(coins)

    while change > 0:
        # N 이하인 가장 큰 코인 찾기
        idx = bisect.bisect_right(coins, change) - 1
        c = coins[idx]
        cnt, change = divmod(change, c)
        result[idx] = cnt
    return result


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    # N 이하의 가장 큰 key 찾기
    def find_le(self, N):
        node, res = self.root, None
        while node:
            if node.key <= N:
                res = node.key
                node = node.right
            else:
                node = node.left
        return res


def change_with_bst(change, coins):
    bst = BST()
    for c in coins:
        bst.insert(c)

    result = [0] * len(coins)   # 리스트 초기화

    while change > 0:
        c = bst.find_le(change)      # N 이하 최대 화폐 단위
        cnt, change = divmod(change, c)
        idx = coins.index(c)    # 해당 화폐의 인덱스 찾기
        result[idx] = cnt
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    
    # 예전 방법 함수로 만든 거
    result = change_with_array(N, money)
    print(f'#{tc}')
    for i in result:
        print(i, end= " ")
    print()

    # 이진 탐색
    result1 = change_with_binary_search(N, money)
    print(f'#{tc}')
    for j in range(1, len(result1) + 1):
        print(result1[-j], end=" ")
    print()

    result2 = change_with_bst(N, money)
    print(f'#{tc}')
    for k in result2:
        print(k, end=" ")
    print()

    # 예전에 했던 방법
    M = len(money)
    result3 = [0] * M
    for l in range(M):
        result3[l] = N // money[l]
        N %= money[l]
    print(f'#{tc}')
    for m in result3:
        print(m, end=" ")
    print()
"""
bisect 모듈에는 보통 이 4개를 많이 씁니다:

bisect_left(a, x)
    정렬된 리스트 a에서 값 x를 넣을 가장 왼쪽 인덱스 반환
    즉, x와 같거나 큰 값이 처음 등장하는 위치

bisect_right(a, x) (bisect 만 써도 됨)
    정렬된 리스트 a에서 값 x를 넣을 가장 오른쪽 인덱스 반환
    즉, x보다 큰 값이 처음 등장하는 위치

insort_left(a, x)
    정렬된 리스트 a에 x를 왼쪽 규칙대로 삽입

insort_right(a, x)
    정렬된 리스트 a에 x를 오른쪽 규칙대로 삽입
"""
