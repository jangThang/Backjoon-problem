# 입력
a, b, c = map(int, input().split())

# 출력
print(sum((a, b, c)) - min(a, b, c))
