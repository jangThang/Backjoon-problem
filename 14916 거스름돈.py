from collections import deque
import sys
input = sys.stdin.readline

# 입력
n = int(input())

# DP
if n == 1:
    print(-1)
elif n == 2:
    print(1)
elif n == 3:
    print(-1)
elif n == 4:
    print(2)
else:
    dp = [100000] * (n + 1)
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1

    for i in range(5, n+1):
        dp[i] = min(dp[i], dp[i-2]+1, dp[i-5]+1)

    print(-1 if dp[n] == 100000 else dp[i])
