import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
cheap_package = 2000 # 가장 싼 패키지 가격
cheap_single = 2000 # 가장 싼 싱글 가격
for _ in range(M):
    p, s = map(int, input().split())
    cheap_package = min(p, cheap_package)
    cheap_single = min(s, cheap_single)

cost = min(cheap_package*(N//6) + cheap_single*(N%6), cheap_package*(N//6+1), cheap_single*N)
print(cost)
