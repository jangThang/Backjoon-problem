# 입력
n = int(input())
k = int(input())

# 계산
cost = 0
cheap = k+60  # 1500에 살 수 있는 양

if n <= cheap:
    print(n*1500)
else:
    print(cheap*1500 + (n-cheap)*3000)
