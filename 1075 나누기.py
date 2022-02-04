N = int(input())
F = int(input())

# 뒤 두자리 제거 (N은 100이상)
N //= 100
N *= 100

# 1씩 올리면서, 나누어 떨어지는지 확인
for i in range(100):
    #나누어 떨어지는 경우
    if (N+i) % F == 0:
        print(f"{i:02d}")
        break
