numlist = list(map(int, input().split()))
numlist.sort()
print(abs(numlist[0]+numlist[3]-numlist[1]-numlist[2]))
