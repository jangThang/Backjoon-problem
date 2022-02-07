import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
row = []
for i in range(N):
    row.append(input().rstrip())

def chess(row, N, M):
    white = 0  # 첫 칸이 흰색일 경우 다시 칠해야하는 정사각형 수
    black = 0  # 첫 칸이 검은색일 경우 다시 칠해야하는 정사각형 수
    for i in range(N, N+8):
        for j in range(M, M+8):
            #짝수칸
            if (i+j) % 2 == 0:
                if row[i][j] == 'W':
                    black += 1
                elif row[i][j] == 'B':
                    white += 1
            #홀수칸
            if (i+j) % 2 == 1:
                if row[i][j] == 'W':
                    white += 1
                elif row[i][j] == 'B':
                    black += 1
    return min(white, black)

res = 65 #결과값
for i in range(N-7):
    for j in range(M-7):
        sub = chess(row, i, j)
        if sub < res:
            res = sub
print(res)
