# 입력
N = int(input())

# 2의 제곱 판별
num = 1
while True:
    # 2의 제곱이면 1 출력
    if num == N:
        print(1)
        break

    # 2의 제곱이 아니면 0 출력
    elif num > N:
        print(0)
        break
    num *= 2
