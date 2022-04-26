# 입력
# x: 공원에 있는 눈의 양, k: 이미 만든 눈뭉치의 양
x, k = map(int, input().split())

# k가 가장 맨 위에 올라갈 눈뭉치인 경우
if k*7 <= x:
    print(k*7000)

# k가 중간에 위치할 눈뭉치인 경우
elif k*3.5 <= x:
    print(k*3500)

# k가 가장 아래 위치한 눈뭉치인 경우
elif k*1.75 <= x:
    print(k*1750)

# 만들지 못하는 경우
else:
    print(0)
