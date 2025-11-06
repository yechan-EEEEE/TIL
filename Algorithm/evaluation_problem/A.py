"""
import copy
import sys
# 재귀 깊이 제한을 늘려줍니다.
sys.setrecursionlimit(2000)

def solution(N, initial_board):
    # 전역 최대 포획 개수
    max_captures = 0
    
    # 초기 포의 위치 찾기 (포는 1개만 있다는 전제)
    start_r, start_c = -1, -1
    for r in range(N):
        for c in range(N):
            if initial_board[r][c] == 2:
                start_r, start_c = r, c
                break
        if start_r != -1:
            break

    # 4방향 (상, 하, 좌, 우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 포의 이동 규칙에 따라 다음 이동 가능한 위치와 포획 여부를 계산하는 함수
    def get_next_moves(board, current_r, current_c):
        moves = []
        
        for i in range(4): # 4방향 탐색
            # 1. 첫 번째 상대 말(1) 찾기
            r, c = current_r, current_c
            first_enemy_r, first_enemy_c = -1, -1
            r += dr[i]
            c += dc[i]
            
            while 0 <= r < N and 0 <= c < N:
                if board[r][c] == 1:
                    first_enemy_r, first_enemy_c = r, c
                    break
                # 다른 포(2)를 만나면 뛰어넘을 수 없으므로 탐색 종료
                if board[r][c] == 2:
                    break
                r += dr[i]
                c += dc[i]
            
            # 이동하려는 방향에 상대 말이 없으면 이 방향으로는 이동 불가능
            if first_enemy_r == -1:
                continue
            
            # 2. 첫 번째 말을 뛰어넘은 뒤부터 이동 가능한 위치 기록
            r, c = first_enemy_r + dr[i], first_enemy_c + dc[i]
            
            while 0 <= r < N and 0 <= c < N:
                if board[r][c] == 1:
                    # 두 번째 상대 말을 만나면 그 말을 잡을 수 있음 (포획)
                    moves.append((r, c, True))
                    break # 포획하면 그 뒤로는 이동 불가
                elif board[r][c] == 0:
                    # 빈 공간으로는 이동 가능 (포획 아님)
                    moves.append((r, c, False))
                elif board[r][c] == 2:
                    # 다른 포를 만나면 이동 종료
                    break
                
                r += dr[i]
                c += dc[i]
            
        return moves

    # DFS (Depth First Search) 함수
    def dfs(current_r, current_c, moves_left, captures, current_board):
        nonlocal max_captures
        
        # 현재까지 잡은 말의 개수를 최대값과 비교하여 업데이트 (이동 횟수 3번 이전에 종료되어도 최대값 비교)
        max_captures = max(max_captures, captures)
        
        # 이동 횟수가 0이면 탐색 종료
        if moves_left == 0:
            return

        # 현재 위치에서 이동 가능한 모든 다음 위치와 포획 여부 계산
        possible_moves = get_next_moves(current_board, current_r, current_c)

        # 모든 가능한 다음 이동에 대해 재귀 호출
        for next_r, next_c, is_capture in possible_moves:
            
            # 보드 상태를 깊은 복사하여 다음 상태로 전달 (백트래킹 용이)
            next_board = copy.deepcopy(current_board)

            # 1. 이전 포의 위치를 빈 공간(0)으로 만듦
            next_board[current_r][current_c] = 0
            
            next_captures = captures
            
            if is_capture:
                # 2-1. 상대 말을 잡는 경우: 포획 개수 증가
                next_captures += 1
                # 잡은 말의 위치(1) 위에 포(2)를 놓음 (1이 0이 된 후 2가 됨)
                next_board[next_r][next_c] = 2 
            else:
                # 2-2. 빈 공간으로 이동하는 경우: 빈 공간(0) 위에 포(2)를 놓음
                next_board[next_r][next_c] = 2
                
            # 다음 상태로 DFS 호출
            dfs(next_r, next_c, moves_left - 1, next_captures, next_board)


    # DFS 시작
    dfs(start_r, start_c, 3, 0, initial_board)
    
    return max_captures

# --- 메인 실행 로직 ---
if __name__ == "__main__":
    try:
        # N 입력
        N = int(sys.stdin.readline().strip())
        
        # 보드 상태 입력 (N줄, 각 줄 공백 구분)
        board_data = []
        for _ in range(N):
            # sys.stdin.readline()을 사용하여 빠르게 입력 처리
            line = list(map(int, sys.stdin.readline().strip().split())) 
            board_data.append(line)
            
        # 입력 확인 및 DFS 실행
        if N > 0 and len(board_data) == N and all(len(row) == N for row in board_data):
            result = solution(N, board_data)
            print(result)
        else:
            print("유효하지 않은 입력 형식입니다.")

    except Exception as e:
        # 입력이 제공되지 않은 경우, 예시 데이터로 실행합니다.
        # print(f"입력 처리 중 오류 발생 또는 입력 없음: {e}")
        
        N_example = 7
        board_example = [
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 2, 0, 1, 0, 1], # 포(2) 시작 위치: (3, 2)
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0]
        ]
        
        print(f"\n--- 예시 데이터 ({N_example}x{N_example}) 실행 결과 ---")
        result_example = solution(N_example, board_example)
        print(f"최대 3번 이동으로 잡을 수 있는 상대 말의 최대 개수: {result_example}")
"""


"""
**[문제] K-구간 최대 합**

N개의 정수로 이루어진 수열 A와 양의 정수 K가 주어진다.
이 수열 A에서 연속된 K개의 숫자들의 합을 구해 새로운 '부분합 수열' B를 만든다.

예를 들어, A = [1, 2, 3, 4, 5, 6] 이고 K = 2 라면,
B = [ (1+2), (2+3), (3+4), (4+5), (5+6) ] = [ 3, 5, 7, 9, 11 ] 이 된다.

이때, '부분합 수열' B의 원소 두 개를 선택하여 더하려 한다.
단, 선택한 두 원소가 참조한 원래 수열 A의 구간이 겹쳐서는 안 된다.

예를 들어, B의 3번째 원소(7)는 A의 3, 4번 원소(인덱스 2, 3)를 참조했고, B의 5번째 원소(11)는 A의 5, 6번 원소(인덱스 4, 5)를 참조했다. 이 두 구간 [2, 3] 과 [4, 5]는 겹치지 않으므로, 이 두 원소의 합 7 + 11 = 18은 유효한 합이다.

하지만 B의 4번째 원소(9)는 A의 4, 5번 원소(인덱스 3, 4)를 참조했고, B의 5번째 원소(11)는 A의 5, 6번 원소(인덱스 4, 5)를 참조했다. 이 두 구간 [3, 4] 와 [4, 5]는 인덱스 4에서 겹치므로, 이 두 원소의 합 9 + 11 = 20은 유효하지 않다.

'부분합 수열' B에서 겹치지 않는 두 원소를 선택하여 더한 값 중 최댓값을 찾는 프로그램을 작성하라.

**[제약 사항]**

1.  총 10개의 테스트 케이스가 주어진다. ( T = 10 )
2.  N의 범위는 2 \* K \<= N \<= 100,000 이다.
3.  K의 범위는 1 \<= K \<= (N/2의 내림) 이다.
4.  수열 A의 각 원소는 1 이상 1,000 이하의 정수이다.

**[입력]**
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 N과 K가 공백으로 구분되어 주어진다.
두 번째 줄에는 수열 A를 나타내는 N개의 정수가 공백으로 구분되어 주어진다.

**[출력]**
각 테스트 케이스마다 \#t (t는 테스트 케이스 번호, 1부터 시작)를 출력하고, 한 칸을 띄운 후 계산된 최대 합을 출력한다.

-----

**[입력 예시 (10개 테스트 케이스)]**

```
10
6 2
4 4 1 1 5 4
6 2
1 2 3 4 5 6
10 3
1 1 1 10 10 10 1 1 1 1
8 2
10 9 8 7 6 5 4 3
7 3
5 5 5 5 5 5 5
4 2
1 2 3 4
15 3
1 5 2 8 3 9 4 10 5 1 6 2 7 3 8
10 2
1 1 1 1 1 1 1 1 100 100
10 2
100 100 1 1 1 1 1 1 1 1
12 3
1 1 1 1 1 100 100 100 1 1 1 1
```

**[출력 예시]**

```
#1 17
#2 18
#3 33
#4 34
#5 30
#6 10
#7 41
#8 202
#9 202
#10 303
```
"""