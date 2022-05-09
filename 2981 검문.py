import sys
input = sys.stdin.readline

# 입력
N = int(input())
numlist = []
for _ in range(N):
    numlist.append(int(input()))
numlist.sort()

# 유클리드 호제법
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a %= b
        a, b = b, a
    return a

# gcd 찾기
res_gcd = numlist[1] - numlist[0]
for i in range(1, N-1):
    res_gcd = gcd(res_gcd, numlist[i+1] - numlist[i])

# gcd의 약수 찾기
divisor = set()
for i in range(1, int(res_gcd**0.5) + 1):
    if res_gcd % i == 0:
        divisor.add(i)
        divisor.add(res_gcd // i)
divisor.discard(1)

# 출력
print(" ".join(map(str, sorted(divisor))))
