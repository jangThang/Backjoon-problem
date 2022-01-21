N = int(input())
cnt = 1
AB = N

while(True):
    CD = AB//10 + AB%10
    BD = (AB%10)*10 + CD%10
    if BD == N:
        break
    cnt += 1
    AB = BD
print(cnt)
