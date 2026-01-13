H, M = map(int, input().split())
result_H, result_M = H, M
if M < 45:
    result_M = M - 45 + 60
    if H == 0:
        result_H = 23
    else:
        result_H = H - 1
else:
    result_M = M - 45
print(result_H, result_M)