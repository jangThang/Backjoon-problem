from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(n):
    subarr = combinations(arr, i+1)
    for j in subarr:
        if sum(j) == s:
            cnt += 1
            
print(cnt)
