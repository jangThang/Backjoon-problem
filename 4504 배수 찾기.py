# 입력
n = int(input())

# 배수 확인
while True:
    x = int(input())
    if x == 0:
        break  # 종료

    if x % n == 0:
        print(f"{x} is a multiple of {n}.")
    else:
        print(f"{x} is NOT a multiple of {n}.")
