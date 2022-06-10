# 입력
n = int(input())

# 불꽃의 개수와 같아지는 K 탐색
for i in range(10000):
    if n == 1+i+i**2:
        print(i)
        break
