# 입력
B = int(input())

# 출력
res = 5*B - 400
print(res)

if res < 100:
    print(1)
elif res == 100:
    print(0)
else:
    print(-1)
