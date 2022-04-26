# 입력
a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

# 1번째 옵션
A = a
if T > 30:
    A += (T-30)*x*21

# 2번째 옵션
B = b
if T > 45:
    B += (T-45)*y*21

print(A, B)
