# 입력
N = int(input())

"""
 n = 1: 5
 n = 2: 12 (7)
 n = 3: 22 (10)
 n = 4: 35 (13)
"""

# 출력
res = 5
plus = 7
for i in range(N-1):
    res += plus
    plus += 3
    res %= 45678
print(res)
