A = int(input())
B = int(input())
C = int(input())

res = A*B*C
num = [0]*10
while(res != 0):
    tmp = res%10
    num[tmp] += 1
    res = res//10
for i in num:
    print(i)
