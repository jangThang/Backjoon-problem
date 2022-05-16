import sys
input = sys.stdin.readline

# 입력
A, B, N = map(int, input().split())

# 출력
A %= B
for i in range(N-1):
    A = (A*10) % B

print((A * 10)//B)
