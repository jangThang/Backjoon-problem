from collections import Counter

numlist = []
for i in range(10):
    numlist.append(int(input()))
print(sum(numlist)//10) #평균
print(Counter(numlist).most_common(1)[0][0]) #최빈값
