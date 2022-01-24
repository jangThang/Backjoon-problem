N = int(input())
res = -1
five = 0

while(five * 5 <= N):
    if (N - five*5)%3 == 0:
        res = five + (N - five*5)//3
    five += 1
print(res)
