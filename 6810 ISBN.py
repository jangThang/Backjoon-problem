# 입력
isbn = "9780921418"
for _ in range(3):
    isbn += input()

# 계산
res = 0
for idx, i in enumerate(isbn):
    if idx % 2 == 1:
        res += int(i)*3
    else:
        res += int(i)
print(f"The 1-3-sum is {res}")
