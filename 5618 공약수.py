# 입력
n = int(input())
numlist = list(map(int, input().split()))

# 최소공약수 찾기
def find_gcd(a, b):
    if a < b:
        a, b = b, a

    while a != 0:
        b %= a
        a, b = b, a
    return b

gcd = numlist[0]  # 최대 공약수 찾기
for i in numlist:
    gcd = find_gcd(gcd, i)

# 약수 찾기
divisor = set()
for i in range(1, int(gcd**0.5)+1):
    if gcd % i == 0:
        divisor.add(i)
        divisor.add(gcd // i)

# 출력
for i in sorted(divisor):
    print(i)
