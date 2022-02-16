_sum, sub = map(int, input().split())
# A + B = _sum
# A - B = sub (단, A > B)
# 따라서 A = (_sum + sub)/2, B = _sum - A

A = (_sum + sub)//2
B = _sum - A
# -1인 경우
if A < 0 or B < 0 or A*2 != _sum + sub:
    print(-1)
else:
    print(A, B)
