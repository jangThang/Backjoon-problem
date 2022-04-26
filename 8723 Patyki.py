# 입력
a, b, c = map(int, input().split())

# 판별 후 출력
if a == b == c:  # 정삼각형 유무
    print(2)

# 직각 삼각형 유무
elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
    print(1)

# 모두 불가능
else:
    print(0)
