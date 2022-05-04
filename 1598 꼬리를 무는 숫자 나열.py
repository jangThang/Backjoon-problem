import sys
input = sys.stdin.readline

# 입력
a, b = map(int, input().split())

# 직각 거리 계산
row = abs(((b-1)//4 + 1) - ((a-1)//4 + 1))
col = abs(((b-1)%4) - ((a-1)%4))

print(row+col)
