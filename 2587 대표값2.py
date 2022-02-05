numlist = []
for i in range(5):
    numlist.append(int(input()))
print(sum(numlist)//5) #평균

numlist.sort()
print(numlist[2]) #중앙값
