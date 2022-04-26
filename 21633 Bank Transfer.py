# 입력
k = int(input())

# 수수료 계산
fees = 25 + k*0.01

if fees < 100:
    print(100)
elif fees > 2000:
    print(2000)
else:
    print(fees)
