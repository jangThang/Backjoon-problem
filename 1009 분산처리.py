import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split()) #데이터의 개수는 a^b
    a1 = a % 10

    if a1 == 0:  # 패턴 1개
        print(10)
    elif a1 in [1, 5, 6]:
        print(a1)
    elif a1 in [4, 9]:  # 패턴 2개
        b1 = b % 2
        if b1 == 0:
            print(a1 * a1 % 10)
        else:
            print(a1)
    else:  # 패턴 4개
        b1 = b % 4
        if b1 == 0:
            print(a1 ** 4 % 10)
        else:
            print(a1 ** b1 % 10)
