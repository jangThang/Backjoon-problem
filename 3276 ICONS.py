# 입력
n = int(input())

# 행과 열을 1개씩 늘림
row = 0
col = 0

while True:
    if row * col >= n:
        break
    row += 1

    if row * col >= n:
        break
    col += 1
print(row, col)
