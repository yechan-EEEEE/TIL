def fibonacci(n):
    if n < 2:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 사용 예시
print(fibonacci(10)) 

"""
-------------------------------------
"""
def fibo1(n):
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

num = 10
memo = [0] * (num+1)  
memo[0] = 0  
memo[1] = 1  

result = fibo1(num)  
print(f"피보나치 수열의 {num}번째 수는 {result}") 

"""
----------------------
"""
def fibo_dp(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1  

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print(fibo_dp(10))  

"""
---------------------------
"""
def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

n = 5
k = 2
print(f"binomial_coefficient({n}, {k}) = {binomial_coefficient(n, k)}")  # 출력: 10

"""
----------------
"""

def bino(n, k):
    B = [[0 for _ in range(k + 1)] for _ in range(n + 1)] 

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]  

    return B[n][k]

n = 5 
k = 2
print(f"bino({n}, {k}) = {bino(n, k)}") 
