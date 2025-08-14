
T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    score_num = list(map(int, input().split()))
    max_team = 0  # 최고 팀일 때 인원 수
    score_num.sort()  # 크기순으로 정렬하고
    score_num.reverse()  # 뒤집어서 큰 애부터 정렬
    # print(score_num)
    for i in range(N):
        cur_team = 1  # 팀 셀 때 자기도 팀에 들어가니까 1
        for j in range(1, N-i):  # 자기 다음 사람부터 해야하니까 1부터, 전체 인원 - 자기 위치만큼 반복
            # print(N)
            # print(i+1)
            # print(score_num[i], score_num[i+1])
            if i+j < N:  # 다음 사람이 리스트를 넘어가버리면 안돼요
                a = score_num[i] - score_num[i+j]
                # print(i, a)
                if a <= K:  # 자기랑 다음 사람 점수 차가 K 이하면
                    cur_team += 1  # 팀을 할 수 있다
                    # print(cur_team)
        max_team = max(max_team, cur_team)
        # print(max_team)

    print(f'#{tc} {max_team}')
