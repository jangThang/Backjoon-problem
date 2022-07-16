# 입력
T = int(input())
for _ in range(T):
    N = int(input())
    numlist = list(map(int, input().split()))
    print(min(numlist), max(numlist))
