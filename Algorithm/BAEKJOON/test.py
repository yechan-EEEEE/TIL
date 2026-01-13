H, M = map(int, input().split())
if M == 45:
    result_M = 0
else:
    result_M = M - 45
if result_M < 0:
    if H == 0:
        H = 23
    else:
        H -= 1
print(H, result_M + 60)