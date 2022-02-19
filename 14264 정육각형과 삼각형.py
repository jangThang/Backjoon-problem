import math
L = int(input()) # 변의 길이

# 두 변과 끼인 각으로 삼각형 넓이 구하기
res = 0.5 * L * L * math.sin(math.radians(120))
print(res)
