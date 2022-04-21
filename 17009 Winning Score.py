apple = 0
banana = 0

# 입력
for i in range(3, 0, -1):
    apple += int(input())*i

for i in range(3, 0, -1):
    banana += int(input())*i

# 비교 후 출력
if apple > banana:
    print('A')
elif apple < banana:
    print('B')
else:
    print('T')
