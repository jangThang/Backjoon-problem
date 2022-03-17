import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
sumlist = []  # 누적 합
for _ in range(N):
    row = list(map(int, input().split()))
    tmp = []
    _sum = 0
    for num in row:
        _sum += num
        tmp.append(_sum)
    sumlist.append(tmp)

# 출력
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = 0
    for i in range(x2-x1+1):
        if y1-2 == -1:
            res += sumlist[x1+i-1][y2-1]
        else:
            res += sumlist[x1+i-1][y2-1] - sumlist[x1+i-1][y1-2]
    print(res)
