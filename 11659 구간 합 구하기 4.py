import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
numlist = list(map(int, input().split()))

# 구간합 구하기
sumlist = [0]
_sum = 0
for i in range(N):
    _sum += numlist[i]
    sumlist.append(_sum)

# 구간합 출력
for _ in range(M):
    start, end = map(int, input().split())
    print(sumlist[end] - sumlist[start-1])
