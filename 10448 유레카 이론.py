from itertools import product
import sys
input = sys.stdin.readline

#삼각수
triangle_num = []
total = 0
for i in range(1, 9999):
    total += i
    triangle_num.append(total)

    # 최대 K는 1000
    if total > 1000:
        break

# 중복조합을 이용한 세 삼각수의 합
case = set(sum(x) for x in product(triangle_num, repeat=3))
case = sorted(case)

#입력
T = int(input())
for _ in range(T):
    K = int(input())
    for i in case:
        #세 삼각수 합과 같으면 1
        if K == i:
            print(1)
            break
            
        #세 삼각수 합을 넘어서면 0
        if K < i:
            print(0)
            break
