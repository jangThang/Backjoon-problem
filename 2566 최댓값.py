import sys
input = sys.stdin.readline

max = -1
xy = []
for i in range(9):
    numlist = list(map(int, input().split()))
    for j in range(9):
        if numlist[j] > max:
            max = numlist[j]
            xy = [i+1, j+1]
print(max)
print(xy[0], xy[1])
