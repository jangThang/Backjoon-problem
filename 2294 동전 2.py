import sys
input = sys.stdin.readline

# 입력
n, k = map(int, input().split())
coin = set()  # 가치가 같은 동전 배제
for _ in range(n):
    coin.add(int(input()))

# DP
cache = [10001]*(k+1)
for cost in range(k+1):
    for c in coin:
        if cost == c:
            cache[cost] = 1
        elif cost-c >= 0:
            cache[cost] = min(cache[cost], cache[cost-c]+1)

# 출력
if cache[k] == 10001:
    print(-1)
else:
    print(cache[k])
