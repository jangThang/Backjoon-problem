numlist = []
for i in range(6):
    numlist.append(int(input()))
score = sum(numlist[0:4]) - min(numlist[0:4]) + max(numlist[4:6])
print(score)
