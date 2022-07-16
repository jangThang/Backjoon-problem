import sys
input = sys.stdin.readline

n, k = map(int, input().split())
score = list(map(int, input().split()))
score.sort()
print(score[n-k])
