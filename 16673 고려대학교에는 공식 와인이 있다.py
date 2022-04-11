import sys
input = sys.stdin.readline

# 입력
C, K, P = map(int, input().split())

# 출력
res = 0  # 와인 수
for i in range(1, C+1):
    res += K*i + P*i**2
print(res)
