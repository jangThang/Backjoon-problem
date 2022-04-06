import sys
input = sys.stdin.readline

# 입력
N = int(input())
numlist = []
for _ in range(N):
    numlist.append(int(input()))

# 정렬
numlist.sort(reverse=True)

# 출력
for i in numlist:
    print(i)
