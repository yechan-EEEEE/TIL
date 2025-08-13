total_candy = 20 # 총 주어진 마이쮸 개수

queue = []  # 사람들이 줄 서는 큐

# queue 에 어떤 데이터가 필요한지
# 누가 받을지(사람 번호)
# 몇 개 받을지(받을 개수)
queue.append((next_preson, 1))
last_person = None


