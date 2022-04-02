import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
numlist = list(map(int, input().split()))
numlist.extend(list(map(int, input().split())))

# 정렬
numlist.sort()

# 출력
for i in numlist:
    print(i, end=' ')
