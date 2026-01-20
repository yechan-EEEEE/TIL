"""
🔑 1. 하루 = BFS/DFS 한 번의 전체 탐색
“하루”마다 모든 나라를 탐색
하루 동안:
아직 방문 안 한 칸에서
BFS 또는 DFS로 연합 하나를 찾음
👉 즉,
while True:
   하루 진행
    더 이상 연합이 없으면 종료
🔑 2. visited는 "하루마다 초기화"
지금 visited를 한 번만 만들었는데 ❌
👉 매 하루마다 새로 만들어야 함
visited = [[False]*N for _ in range(N)]
🔑 3. BFS로 "연합" 찾기
한 칸에서 시작해서:
상하좌우 탐색
조건:
L <= abs(countries[nx][ny] - countries[x][y]) <= R
✔ 만족하면 같은 연합
✔ 연합에 포함된 좌표들을 리스트에 저장
힌트 구조:
queue = [(x, y)]
union = [(x, y)]
population_sum = countries[x][y]
🔑 4. 연합 크기가 2 이상이면 인구 이동 발생
이게 중요한 종료 조건 힌트야 👇
연합에 2칸 이상 들어갔다면
→ 인구 이동 발생한 것
하루 동안 단 하나라도 이런 연합이 생기면
→ 그날은 count + 1
🔑 5. 연합 처리
BFS 끝나면:
new_pop = population_sum // len(union)
for x, y in union:
    countries[x][y] = new_pop
🔑 6. 종료 조건
하루를 다 돌았는데:
연합 크기 ≥ 2 인 경우가 한 번도 없었다
→ 인구 이동 종료
전체 흐름 요약 (의사코드 힌트)
day = 0
while True:
    visited 초기화
    moved = False

    모든 칸 순회:
        방문 안 했으면:
            BFS로 연합 찾기
            연합 크기 ≥ 2:
                인구 재분배
                moved = True

    if moved == False:
        break
    day += 1
"""
