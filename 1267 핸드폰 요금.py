N = int(input())
call = list(map(int, input().split()))

y = 0 #영식 요금제
m = 0 #민식 요금제
for i in call:
    y += (i//30+1)*10
    m += (i//60+1)*15

#출력
if y > m:
    print("M", m)
elif y == m:
    print("Y M", m)
else:
    print("Y", y)
