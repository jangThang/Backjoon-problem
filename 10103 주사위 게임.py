n = int(input())
ch = 100 # 창영 점수
s = 100 # 상덕 점수
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        s -= a
    elif a < b:
        ch -= b
print(ch)
print(s)
