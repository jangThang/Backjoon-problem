K = int(input())
numlist = []

for i in range(K):
    n = int(input())
    if n == 0:
        numlist.pop()
    else:
        numlist.append(n)
print(sum(numlist))
