import sys
input = sys.stdin.readline

#입력
X, Y = input().split()

#두 수를 거꾸로 더하기
res = int(X[::-1]) + int(Y[::-1])

#맨 뒤가 0이면 제거하기
while res % 10 == 0:
    res //= 10

#거꾸로 출력하기
print(str(res)[::-1])
