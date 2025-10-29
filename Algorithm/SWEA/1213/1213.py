T = 10
for _ in range(1, T + 1):
    tc = int(input())
    find_sentence = ""
    find_sentence += input()
    sentence = ""
    sentence += input()
    cnt = 0

    for i in range(len(sentence)):
        if sentence[i:i + len(find_sentence)] == find_sentence:
            cnt += 1
    print(f'#{tc} {cnt}')
