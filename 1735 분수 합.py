a, b = map(int, input().split())
c, d = map(int, input().split())

numerator = a*d + b*c #분자
denominator = b*d #분모

# 유클리드 호제법을 통한 최대공약수
x = numerator
y = denominator
while x != y:
    if x > y:
        x -= y
    else:
        y -= x
print(numerator//x, denominator//x)
