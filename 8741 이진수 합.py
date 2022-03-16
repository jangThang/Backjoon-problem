k = int(input())

# 1부터 2^k -1까지의 합
n = 2**k-1
res = n*(n+1)//2

# 이진수로 출력
print(bin(res)[2:])
