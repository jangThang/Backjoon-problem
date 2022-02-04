N = int(input())
problems = list(map(int, input().split()))

res = 0 #점수
cnt = 0 #연속으로 맞은 횟수
for i in problems:
    if i == 1:
        cnt += 1
        res += cnt
    else:
        cnt = 0
print(res)
