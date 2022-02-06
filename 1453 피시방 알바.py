N = int(input())
numlist = list(map(int, input().split()))

refused = 0
pcRoom = [0]*101
for i in numlist:
    if pcRoom[i] == 1:
        refused += 1
    else:
        pcRoom[i] = 1
print(refused)
