# 입력
T = int(input())

for _ in range(T):
    total, divide = map(int, input().split())
    print(f"You get {total//divide} piece(s) and your dad gets {total%divide} piece(s).")
