import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = float(input())
    price = round(n*0.8, 2)
    print(f"${price:.2f}")
