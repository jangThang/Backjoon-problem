import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
matrixA = []
for _ in range(N):
    matrixA.append(list(map(int, input().split())))

M, K = map(int, input().split())
matrixB = []
for _ in range(M):
    matrixB.append(list(map(int, input().split())))

# 행렬 곱셈
def mul_matrix(mat1, mat2):
    res = [[0]*K for _ in range(N)]
    for i in range(N):
        for j in range(K):
            for z in range(M):
                # c11 = a11*b11 + a12*b21
                res[i][j] += mat1[i][z] * mat2[z][j]
    return res

# 출력
result = mul_matrix(matrixA, matrixB)
for row in result:
    for col in row:
        print(col, end=" ")
    print()
