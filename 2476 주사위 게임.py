import sys
input = sys.stdin.readline

N = int(input())
maxReward = 0
for i in range(N):
    reward = 0
    a, b, c = map(int, input().split())
    # 같은 눈 3개
    if a == b == c:
        reward += 10000 + a*1000

    # 같은 눈 2개
    elif a == b or b == c:
        reward += 1000 + b*100
    elif a == c:
        reward += 1000 + a*100

    # 모두 다른 눈
    else:
        reward += max(a,b,c)*100

    if maxReward < reward:
        maxReward = reward
print(maxReward)
