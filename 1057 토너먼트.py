import sys
input = sys.stdin.readline

# 입력
N, a, b = map(int, input().split())

# 토너먼트
cnt = 0
while a != b:
    a -= a // 2
    b -= b // 2
    cnt += 1
print(cnt)
