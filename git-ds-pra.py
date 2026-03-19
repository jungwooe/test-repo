이정우, 202503694, 컴퓨터공학부
hello
# 코드트리 prefixSum - 두가지버전

import time, random

# O(n^2) 시간 알고리즘
def prefixSum1(X, n):
    S = [0] * n
    for i in range(n):
        for j in range(i + 1):
            S[i] += X[j]
    return S

# O(n) 시간 알고리즘 
def prefixSum2(X, n):
    S = [0] * n
    S[0] = X[0]
    for i in range(1, n):
        S[i] = S[i - 1] + X[i]
    return S

random.seed() # random 함수 초기화
n = int(input())
X = []

for i in range(n):
    X.append(random.randint(-999, 999))

before = time.process_time()
prefixSum1(X, n)
after = time.process_time()
prefixSum2(X, n)
last = time.process_time()

# time1 = after - before
# time2 = last - after

# print(f"O(n^2)의 수행시간 : {time1:.7f}")
# print(f"O(n)의 수행시간 : {time2:.7f}")

print(f"O(n^2)의 수행시간 : {after - before:.8f}")

print(f"O(n)의 수행시간 : {last - after:.8f}")
