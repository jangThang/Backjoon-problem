N = int(input())
# 위 삼각형
for i in range(1, N+1):
    print(" "*(N-i) + "*"*i)

# 아래 삼각형
for i in range(1, N):
    print(" "*i + "*"*(N-i))
