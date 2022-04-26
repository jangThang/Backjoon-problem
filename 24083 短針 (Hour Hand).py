# 입력
a = int(input())
b = int(input())

# 출력
hour = (a+b) % 12
print(hour if hour != 0 else 12)
