N, M = map(int, input().split())
matrix = []
#행렬 A입력
for i in range(N):
    matrix.append(list(map(int, input().split())))

#행렬 B덧셈
for i in range(N):
    b = list(map(int, input().split()))
    for j in range(M):
        matrix[i][j] += b[j]

#행렬 출력
for i in range(N):
    row = ''
    for j in range(M):
        row += str(matrix[i][j]) + " "
    print(row[:-1])
