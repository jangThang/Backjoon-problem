import sys
input = sys.stdin.readline

#입력
N, M = map(int, input().split())
numlist = list(map(int, input().split()))

#부분합
sumlist = [0]
sub_sum = 0
for i in numlist:
    sub_sum += i
    sumlist.append(sub_sum)

#M이 되는 경우의 수 찾기
res = 0 #M이 되는 경우
for i in range(N+1):
    for j in range(i):
        if sumlist[i] - sumlist[j] == M:
            res += 1
print(res)
