# 입력
p1, q1, p2, q2 = map(int, input().split())

# 삼각형의 면적
res = p1*p2/q1/q2/2

# 면적이 정수?
if res.is_integer():
    print(1)
else:
    print(0)
