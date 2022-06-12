# 입력
a, b = map(int, input().split())
c, d = map(int, input().split())

# 가장 큰 값 출력
array = [a/c+b/d, c/d+a/b, d/b+c/a, b/a+d/c]
print(array.index(max(array)))
