# 입력
c = int(input())

# C(n)이 1이 되면 break
for n in range(1, 100001):
    if c == 1:
        print(n)
        break

    # 짝수일 때
    if c % 2 == 0:
        c //= 2

    # 홀수일 때
    else:
        c = 3*c + 1
