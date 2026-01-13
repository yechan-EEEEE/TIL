A, B = map(int, input().split())
C = int(input())
result_H, result_M = 0, 0

result_H = A + ((B + C) // 60)
if result_H > 23:
    result_H -= 24
result_M = (B + C) % 60

print(result_H, result_M)