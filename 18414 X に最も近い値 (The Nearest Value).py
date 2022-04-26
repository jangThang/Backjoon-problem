# 입력
X, L, R = map(int, input().split())

# X가 L보다 작을 경우
if X < L:
    print(L)

# X가 R보다 큰 경우
elif X > R:
    print(R)

# X가 L과 R 사이인 경우
else:
    print(X)
