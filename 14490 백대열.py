n, m = map(int, input().split(':'))

#유클리드 호제법
def gcd(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        x %= y
        x, y = y, x
    return x

gcd = gcd(n, m)
print(f"{n//gcd}:{m//gcd}")
