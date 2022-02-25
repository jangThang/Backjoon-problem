N, K = input().split()
time = [0, 0, 0] #hour, minute, sec
res = 0
while time != [int(N)+1, 0, 0]:
    #k가 포함되면 res+1
    if K in str(time):
        res += 1
    #K가 0이고 1의 자리이면 res+1
    elif K == '0' and (time[0] < 10 or time[1] < 10 or time[2] < 10):
        res += 1
    time[2] += 1 #1초 지남

    if time[2] == 60:
        time[2] = 0
        time[1] += 1

    if time[1] == 60:
        time[1] = 0
        time[0] += 1
print(res)
