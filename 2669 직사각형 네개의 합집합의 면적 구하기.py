import sys
input = sys.stdin.readline

# 입력
board = [[0]*101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

# 출력
res = 0
for i in board:
    res += sum(i)
print(res)
