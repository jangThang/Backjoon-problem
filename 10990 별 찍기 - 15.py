N = int(input())
# 첫 줄
print(" "*(N-1) + "*")

# 두 번째 줄부터 끝까지
for i in range(2, N+1):
    print(" "*(N-i) + "*" + " "*(2*(i-2)+1) + "*")
