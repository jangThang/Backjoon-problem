import sys
input = sys.stdin.readline

while True:
    a,b,c = map(int, input().split())
    if a+b+c == 0:
        break
    if 2*max(a,b,c)**2 == a**2 + b**2 + c**2:
        print("right")
    else:
        print("wrong")
