# 입력
A, B = map(int, input().split())
C = int(input())

# 치킨 구매 가능
if A+B >= C*2:
    print(A+B-C*2)
else:
    print(A+B)
