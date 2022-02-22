N = int(input())
X = list(map(int, input().split()))

setX = set(X) #중복값 제거
setX = sorted(setX) #정렬

dictX = {}
for i in range(len(setX)):
    dictX[setX[i]] = i

for i in X:
    print(dictX[i], end=" ")
