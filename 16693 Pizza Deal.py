from math import pi

# 입력
A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())

# 비교
if A1/P1 > (R1**2)*pi/P2:
    print("Slice of pizza")
else:
    print("Whole pizza")
