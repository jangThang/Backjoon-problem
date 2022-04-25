# 입력
win = 0
for _ in range(6):
    if input() == 'W':
        win += 1

# 출력
if win == 0:
    print(-1)
elif win <= 2:
    print(3)
elif win <= 4:
    print(2)
else:
    print(1)
