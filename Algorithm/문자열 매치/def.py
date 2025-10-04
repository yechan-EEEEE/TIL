def brute_force(text, pattern):
    M, N = len(text), len(pattern)

    i, j = 0, 0

    while i < M and j < N:
        if text[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == N:
        return 1
    else:
        return 0


"""
---------------------------------------------------------------------
"""


def rabin_karp_rolling_hash(text, pattern):
    n = len(text)
    m = len(pattern)
    prime = 101  
    base = 256   

    def calculate_hash(str):
        hash_value = 0
        for i, char in enumerate(str):
            hash_value += ord(char) * pow(base, m-1-i, prime)
        return hash_value % prime

    pattern_hash = calculate_hash(pattern)
    window_hash = calculate_hash(text[:m])

    highest_power = pow(base, m-1, prime)


    for i in range(n - m + 1):
        if window_hash == pattern_hash:
            if text[i:i+m] == pattern:
                print(f"패턴: {i} - {i + m - 1}")

        if i < n - m:
            window_hash = window_hash - (ord(text[i]) * highest_power) % prime
            window_hash = (window_hash + ord(text[i + m])) % prime

# 테스트
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(f"텍스트: {text}")
print(f"패턴: {pattern}")
rabin_karp_rolling_hash(text, pattern)


"""
---------------------------------------------------------------------
"""


def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0 or n == 0 or m > n:
        return []

    skip_table = {}
    for i in range(m - 1):  # 마지막 문자(m-1)는 규칙에서 제외
        skip_table[pattern[i]] = m - 1 - i

    i = 0 
    found_indexes = []

    while i <= n - m:
        j = m - 1 

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            found_indexes.append(i)
            i += 1
        else:
            bad_char = text[i + j]
            
            shift = skip_table.get(bad_char, m)
            i += shift
            
    return found_indexes

text = "a pattern matching algorithm"
pattern = "rithm"
result = boyer_moore_search(text, pattern)

if result:
    print(f"패턴이 발견된 위치: {result}")
else:
    print("패턴을 찾지 못했습니다")


"""
---------------------------------------------------------------------
"""


def get_lps(pattern):
    lps = [0] * len(pattern) 
    j = 0 
    i = 1  

    while i < len(pattern): 
        if pattern[j] == pattern[i]:
            j += 1
            lps[i] = j
            i += 1

        else:
            if j == 0:
                lps[i] = 0
                i += 1

            else:
                j = lps[j - 1]
    return lps


def kmp(text, pattern):
    M = len(pattern)
    N = len(text)
    lps = get_lps(pattern)  

    i = 0 
    j = 0  

    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == M:
            print(f"패턴 {i - j}에서 발견")
            j = lps[j - 1]

        elif i < N and pattern[j] != text[i]:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp(text, pattern)
