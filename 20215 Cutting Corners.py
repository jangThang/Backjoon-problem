# 입력
w, h = map(int, input().split())

# 출력
diagonal = (w**2 + h**2) ** 0.5
print(w+h-diagonal)
