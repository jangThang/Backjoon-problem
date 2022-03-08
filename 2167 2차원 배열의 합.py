import sys
input = sys.stdin.readline

#입력
N, M = map(int, input().split())
numlist = []
for _ in range(N):
    numlist.append(list(map(int, input().split())))

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    res = 0
    for row in range(i-1, x):
        for col in range(j-1, y):
            res += numlist[row][col]
    print(res)
